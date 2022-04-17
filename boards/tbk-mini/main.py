from kb import KMKKeyboard
from kmk.keys import KC
from kmk.modules.split import Split, SplitSide

keyboard = KMKKeyboard()

split = Split(split_side=SplitSide.LEFT)
keyboard.modules.append(split)
 
_______ = KC.TRNS
XXXXX   = KC.NO

keyboard.keymap = [
    [ 
        KC.LGUI,  KC.Q,    KC.W,    KC.F,    KC.P,    KC.B,       KC.J,    KC.L,    KC.U,    KC.Y,    KC.SCLN, KC.MINS,
        KC.ESC,   KC.A,    KC.R,    KC.S,    KC.T,    KC.G,       KC.M,    KC.N,    KC.E,    KC.I,    KC.O,    KC.QUOT,
        KC.TAB,   KC.Z,    KC.X,    KC.C,    KC.D,    KC.V,       KC.K,    KC.H,    KC.COMM, KC.DOT,  KC.SLSH, KC.EQL,
        XXXXX,   XXXXX,   XXXXX,    KC.LSFT, KC.LSFT, KC.NO,      KC.BSPC, KC.ENT,  KC.DEL,  XXXXX,   XXXXX,   XXXXX   ],
]

if __name__ == '__main__':
    keyboard.go()