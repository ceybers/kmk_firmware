from kmk.keys import KC, ModifierKey, make_key
from kmk.modules import Module


class ToggleMods(Module):
    def __init__(self, cg_swap_enable=False):
        make_key(
            names=('TSFT',),
        )
        make_key(
            names=('TCTL',),
        )
        make_key(
            names=('TALT',),
        )
        make_key(
            names=('TGUI',),
        )
        self._tm_mapping = {
            KC.TSFT: KC.LSFT,
            KC.TCTL: KC.LCTL,
            KC.TALT: KC.LALT,
            KC.TGUI: KC.LGUI,
        }

    def during_bootup(self, keyboard):
        return

    def matrix_detected_press(self, keyboard):
        return keyboard.matrix_update is None

    def before_matrix_scan(self, keyboard):
        return

    def process_key(self, keyboard, key, is_pressed, int_coord):
        if key in (KC.TSFT, KC.TCTL, KC.TALT, KC.TGUI,):
            mod_key =  self._tm_mapping.get(key)
            if is_pressed:
                keyboard.process_key(mod_key, not mod_key in keyboard.keys_pressed)
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
