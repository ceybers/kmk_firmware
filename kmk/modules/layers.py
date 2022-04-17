'''One layer isn't enough. Adds keys to get to more of them'''
from kmk.handlers.stock import passthrough
from micropython import const # type: ignore

from kmk.key_validators import layer_key_validator
from kmk.keys import make_key, make_argumented_key
from kmk.modules.holdtap import ActivationType, HoldTap


def layer_key_validator(layer, kc=None):
    '''
    Validates the syntax (but not semantics) of a layer key call.  We won't
    have access to the keymap here, so we can't verify much of anything useful
    here (like whether the target layer actually exists). The spirit of this
    existing is mostly that Python will catch extraneous args/kwargs and error
    out.
    '''
    return LayerKeyMeta(layer, kc)


    LT = const(0)
    TT = const(1)
    TL = const(2) # Tap/Layer, inverse of LT (i.e. TG(n) on tap instead of MO(n) on hold)
    TH = const(3) # Tap/Hold, TT but uses hold instead of 3x tapdance


def layer_key_validator_tt(layer, prefer_hold=True, **kwargs):
    return HoldTapKeyMeta(
        tap=KC.TG(layer), hold=KC.MO(layer), prefer_hold=prefer_hold, **kwargs
    )


class LayerKeyMeta:
    def __init__(self, layer, kc=None):
        self.layer = layer
        self.kc = kc


class Layers(HoldTap):
    '''Gives access to the keys used to enable the layer system'''

    def __init__(self):
        # Layers
        super().__init__()
        self._is_locked = False
        make_key(
            names=('LLOCK',),
            on_press=self._llock_pressed,
            on_release=passthrough,
        )
        make_argumented_key(
            validator=layer_key_validator,
            names=('MO',),
            on_press=self._mo_pressed,
            on_release=self._mo_released,
        )
        make_argumented_key(
            validator=layer_key_validator,
            names=('DF',),
            on_press=self._df_pressed,
        )
        make_argumented_key(
            validator=layer_key_validator,
            names=('LM',),
            on_press=self._lm_pressed,
            on_release=self._lm_released,
        )
        make_argumented_key(
            validator=layer_key_validator,
            names=('TG',),
            on_press=self._tg_pressed,
        )
        make_argumented_key(
            validator=layer_key_validator,
            names=('TO',),
            on_press=self._to_pressed,
        )
        make_argumented_key(
            validator=layer_key_validator_lt,
            names=('LT',),
            on_press=self.ht_pressed,
            on_release=self.ht_released,
        )
        make_argumented_key(
            validator=layer_key_validator_tt,
            names=('TT',),
            on_press=curry(self.ht_pressed, key_type=LayerType.TT),
            on_release=curry(self.ht_released, key_type=LayerType.TT),
        )
        make_argumented_key(
            validator=layer_key_validator,
            names=('TL',),
            on_press=curry(self.ht_pressed, key_type=LayerType.TL),
            on_release=curry(self.ht_released, key_type=LayerType.TL),
        )
        make_argumented_key(
            validator=curry(layer_key_validator, prefer_hold=True),
            names=('TH',),
            on_press=curry(self.ht_pressed, key_type=LayerType.TH),
            on_release=curry(self.ht_released, key_type=LayerType.TH),
        )

    def _df_pressed(self, key, keyboard, *args, **kwargs):
        '''
        Switches the default layer
        '''
        keyboard.active_layers[-1] = key.meta.layer
        self._print_debug(keyboard)

    def _mo_pressed(self, key, keyboard, *args, **kwargs):
        '''
        Momentarily activates layer, switches off when you let go
        '''
        keyboard.active_layers.insert(0, key.meta.layer)
        self._print_debug(keyboard)

    #@staticmethod
    def _mo_released(self, key, keyboard, *args, **kwargs):
        # remove the first instance of the target layer
        # from the active list
        # under almost all normal use cases, this will
        # disable the layer (but preserve it if it was triggered
        # as a default layer, etc.)
        # this also resolves an issue where using DF() on a layer
        # triggered by MO() and then defaulting to the MO()'s layer
        # would result in no layers active
        if self._is_locked:
            pass
        else:
            try:
                del_idx = keyboard.active_layers.index(key.meta.layer)
                del keyboard.active_layers[del_idx]
            except ValueError:
                pass

    def _lm_pressed(self, key, keyboard, *args, **kwargs):
        '''
        As MO(layer) but with mod active
        '''
        # Sets the timer start and acts like MO otherwise
        keyboard.add_key(key.meta.kc)
        self._mo_pressed(key, keyboard, *args, **kwargs)

    def _lm_released(self, key, keyboard, *args, **kwargs):
        '''
        As MO(layer) but with mod active
        '''
        if self._is_locked:
            pass
        else:
            keyboard.hid_pending = True
            keyboard.keys_pressed.discard(key.meta.kc)
            self._mo_released(key, keyboard, *args, **kwargs)

    def _tg_pressed(self, key, keyboard, *args, **kwargs):
        '''
        Toggles the layer (enables it if not active, and vise versa)
        '''
        # See mo_released for implementation details around this
        self._is_locked = False
        keyboard.keys_pressed = set()
        try:
            del_idx = keyboard.active_layers.index(key.meta.layer)
            del keyboard.active_layers[del_idx]
        except ValueError:
            keyboard.active_layers.insert(0, key.meta.layer)

    def _to_pressed(self, key, keyboard, *args, **kwargs):
        '''
        Activates layer and deactivates all other layers
        '''
        self._is_locked = False
        keyboard.keys_pressed = set()
        keyboard.active_layers.clear()
        keyboard.active_layers.insert(0, key.meta.layer)

    def ht_activate_hold(self, key, keyboard, *args, **kwargs):
        key_type = kwargs['key_type']
        if key_type == LayerType.LT:
            self._mo_pressed(key, keyboard, *args, **kwargs)
        elif key_type == LayerType.TT:
            self._tg_pressed(key, keyboard, *args, **kwargs)
        elif key_type == LayerType.TL:
            keyboard.hid_pending = True
            keyboard.keys_pressed.add(key.meta.kc)
        elif key_type == LayerType.TH:
            self._mo_pressed(key, keyboard, *args, **kwargs)
            pass

    def ht_deactivate_hold(self, key, keyboard, *args, **kwargs):
        key_type = kwargs['key_type']
        if key_type == LayerType.LT:
            self._mo_released(key, keyboard, *args, **kwargs)
        elif key_type == LayerType.TT:
            self._tg_pressed(key, keyboard, *args, **kwargs)
        elif key_type == LayerType.TL:
            keyboard.hid_pending = True
            keyboard.keys_pressed.discard(key.meta.kc)
        elif key_type == LayerType.TH:
            self._mo_released(key, keyboard, *args, **kwargs)

    def ht_activate_tap(self, key, keyboard, *args, **kwargs):
        key_type = kwargs['key_type']
        if key_type == LayerType.LT:
            keyboard.hid_pending = True
            keyboard.keys_pressed.add(key.meta.kc)
        elif key_type == LayerType.TT:
            self._tg_pressed(key, keyboard, *args, **kwargs)
        elif key_type == LayerType.TL:
            self._tg_pressed(key, keyboard, *args, **kwargs)
        elif key_type == LayerType.TH:
            self._tg_pressed(key, keyboard, *args, **kwargs)

    def ht_deactivate_tap(self, key, keyboard, *args, **kwargs):
        key_type = kwargs['key_type']
        if key_type == LayerType.LT:
            keyboard.hid_pending = True
            keyboard.keys_pressed.discard(key.meta.kc)
        elif key_type == LayerType.TL:
            pass
        elif key_type == LayerType.TH:
            pass

    def _llock_pressed(self, key, keyboard, *args, **kwargs):
        self._is_locked = True