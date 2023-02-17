from kmk.keys import KC, make_argumented_key
from kmk.modules import Module


class SlowModMeta:
    def __init__(self, kc, mod):
        self.kc = kc
        self.mod = mod


class SlowMods(Module):
    def __init__(self):
        self._shifted_numbers = range(KC.EXCLAIM.code, KC.QUESTION.code)

        make_argumented_key(
            names=('SL',),
            validator=SlowModMeta,
            on_press=self.sl_pressed,
            on_release=self.sl_released,
        )

    def during_bootup(self, keyboard):
        return

    def before_matrix_scan(self, keyboard):
        return

    def process_key(self, keyboard, key, is_pressed, int_coord):
        if key.code in self._shifted_numbers:
            if KC.LSFT.code in key.has_modifiers:
                keyboard.process_key(KC.LSFT, is_pressed)
                keyboard._send_hid()
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

    def release_key(self, keyboard, key):
        return

    def sl_pressed(self, key, keyboard, *args, **kwargs):
        keyboard.process_key(key.meta.mod, True)
        keyboard._send_hid()
        keyboard.process_key(key.meta.kc, True)
        keyboard._send_hid()
        return

    def sl_released(self, key, keyboard, *args, **kwargs):
        keyboard.process_key(key.meta.kc, False)
        keyboard._send_hid()
        keyboard.process_key(key.meta.mod, False)
        keyboard._send_hid()
        return
