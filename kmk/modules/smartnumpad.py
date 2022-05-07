'''
Automatically deactivate a numpad layer when pressing a non-numpad key, or after timeout.
Based on CapsWord module.
'''

from kmk.keys import FIRST_KMK_INTERNAL_KEY, KC, ModifierKey, make_key
from kmk.modules import Module
from kmk.key_validators import LayerKeyMeta


class SmartNumPad(Module):
    def __init__(self, layer=1, timeout=3000):
        self._numpad = range(KC.KP_SLASH.code, KC.KP_COMMA.code)
        self.keys_sustain = [
            KC.DOT,
            KC.COMMA,
        ]
        self.layer = layer
        self._timeout_key = False
        self._snp_active = False
        self.timeout = timeout
        self._active_layers = None
        self._debug_enabled = False
        self._coordkeys_pressed = None
        
    def during_bootup(self, keyboard):
        self._active_layers = keyboard.active_layers
        self._coordkeys_pressed = keyboard._coordkeys_pressed
        self._debug_enabled = keyboard.debug_enabled
        return

    def before_matrix_scan(self, keyboard):
        return

    def process_key(self, keyboard, key, is_pressed, int_coord):
        continue_snp = False
        if self._snp_active:
            if (
                key.code in self._numpad
                or isinstance(key, ModifierKey)
                or key in self.keys_sustain
                or key.code
                >= FIRST_KMK_INTERNAL_KEY  # user defined keys are also ignored
            ):
                if self._debug_enabled:
                    print('SmartNumPad: Sustaining')
                continue_snp = True

        if isinstance(key.meta, LayerKeyMeta):
            if (key.meta.layer == self.layer):
                if is_pressed:
                    self._snp_active = True
                    if self._debug_enabled:
                        print('SmartNumPad: Activated by layer activation')
                    continue_snp = True
            else:
                if self._debug_enabled:
                    print('SmartNumPad: Layer not in active_layers')

        if continue_snp:
            self.discard_timeout(keyboard)
            self.request_timeout(keyboard)
        else:
            if self._snp_active:
                if self._debug_enabled:
                    print('SmartNumPad: Deactivating by keypress')
                self.discard_timeout(keyboard)
                self.process_timeout()

        return key

    def before_hid_send(self, keyboard):
        return

    def after_hid_send(self, keyboard):
        return

    def on_powersave_enable(self, keyboard):
        return

    def on_powersave_disable(self, keyboard):
        return

    def after_matrix_scan(self, keyboard):
        return

    def process_timeout(self):
        for key_idx in self._coordkeys_pressed:
            key = self._coordkeys_pressed[key_idx]
            if key is not None:
                if isinstance(key.meta, LayerKeyMeta):
                    if key.meta.layer == self.layer:
                        return
        if self._debug_enabled:
            print('SmartNumPad: Deactivated')        
        if (len(self._active_layers) > 1):
            if (self.layer in self._active_layers):
                self._active_layers.remove(self.layer)
        else:
            if self._debug_enabled:
                print('SmartNumPad: Insufficient layers active to deactivate')       
        self._snp_active = False
        self._timeout_key = False

    def request_timeout(self, keyboard):
        if self._snp_active:
            if self.timeout:
                self._timeout_key = keyboard.set_timeout(
                    self.timeout, lambda: self.process_timeout()
                )

    def discard_timeout(self, keyboard):
        if self._timeout_key:
            if self.timeout:
                keyboard.cancel_timeout(self._timeout_key)
            self._timeout_key = False
