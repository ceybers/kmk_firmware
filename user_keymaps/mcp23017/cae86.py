'''
cae86
Fri 17 February 2023
'''

#region
import board
import busio

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.scanners.mcpscanner import MCPScanner

from kmk.modules.combos import Combos, Chord, Sequence
from kmk.modules.layers import Layers
from kmk.modules.modtap import ModTap
from kmk.modules.oneshot import OneShot
from kmk.modules.slowmods import SlowMods

i2c = busio.I2C(scl=board.GP1, sda=board.GP0, frequency=400000)

keyboard = KMKKeyboard()
keyboard.matrix = [
    MCPScanner( # LHS MCP23017 I/O Expander
        row_pin_numbers = [0, 1, 2, 3],
        col_pin_numbers = [8, 9, 10, 11, 12, 13],
        i2c = i2c,
        i2c_address = 0x20,
        offset = 0
    ),
    MCPScanner( # RHS MCP23017 I/O Expander
        row_pin_numbers = [0, 1, 2, 3],
        col_pin_numbers = [8, 9, 10, 12, 11, 13],
        i2c = i2c,
        i2c_address = 0x24,
        offset = 24
    )
]

keyboard.debug_enabled = False
keyboard.diode_orientation = DiodeOrientation.COL2ROW
keyboard.coord_mapping = [
    0,   1,  2,  3,  4,  5,     24, 25, 26, 27, 28, 29,
    6,   7,  8,  9, 10, 11,     30, 31, 32, 33, 34, 35,
    12, 13, 14, 15, 16, 17,     36, 37, 38, 39, 40, 41,
    18, 19, 20, 21, 22, 23,     42, 43, 44, 45, 46, 47
    ]

modtap = ModTap()
modtap.tap_time = 150
keyboard.modules.append(modtap)
keyboard.modules.append(Layers())
combos = Combos()
keyboard.modules.append(combos)
keyboard.modules.append(OneShot())
keyboard.modules.append(SlowMods())
#endregion

#region Aliases
# Aliases for VS Code highlighting
_______ = KC.TRNS

CE_CUT = KC.SL(KC.X, KC.LCTL)
CE_CPY = KC.SL(KC.C, KC.LCTL)
CE_PST = KC.SL(KC.V, KC.LCTL) 
CE_SAVE = KC.SL(KC.S, KC.LCTL)
SEL_ALL = KC.SL(KC.A, KC.LCTL)
CE_UNDO = KC.SL(KC.Z, KC.LCTL)

# Left-most column on a 3x6+3 LHS board
# Use KC.LCTL(KC.Z) because SlowMod/SCTL doesn't work with ModTap/KC.MT
LHS_1 = KC.MT(KC.PSCR, CE_CUT, prefer_hold=False) 
LHS_2 = KC.MT(KC.ESC,  CE_CPY, prefer_hold=False)
LHS_3 = KC.MT(KC.TAB,  CE_PST, prefer_hold=False)

# Thumb buttons tab & hold
THM_L1 = KC.LSFT
THM_L2 = KC.SPC
THM_L3 = KC.LT(1, KC.OS(KC.LCTL), prefer_hold=True)
THM_R1 = KC.BSPC
THM_R2 = KC.ENT
THM_R3 = KC.LT(1, KC.DEL, prefer_hold=True)

# https://github.com/KMKfw/kmk_firmware/blob/master/docs/en/modtap.md
# Home row mods on numpad
MR_P4   = KC.MT(KC.P4,   KC.LCTL, prefer_hold=False, tap_interrupted=False, tap_time=100)
MR_P5   = KC.MT(KC.P5,   KC.LSFT, prefer_hold=False, tap_interrupted=False, tap_time=100)
MR_P6   = KC.MT(KC.P6,   KC.LALT, prefer_hold=False, tap_interrupted=False, tap_time=100)
MR_PAST = KC.MT(KC.PAST, KC.LGUI, prefer_hold=False, tap_interrupted=False, tap_time=100)

# Auto-shift on RHS punctuation
CE_SCLN = KC.MT(KC.SCLN, KC.COLN)
CE_MINS = KC.MT(KC.MINS, KC.UNDS)
CE_QUOT = KC.MT(KC.QUOT, KC.DQUO)
CE_COMM = KC.MT(KC.COMM, KC.LPRN, prefer_hold=False, tap_interrupted=False, tap_time=100)
CE_DOT  = KC.MT(KC.DOT,  KC.RPRN, prefer_hold=False, tap_interrupted=False, tap_time=100)
CE_BSLS = KC.MT(KC.QUES, KC.SLSH)
CE_EXLM = KC.MT(KC.EXLM, KC.BSLS)

# Random aliases
CE_AF4  = KC.LALT(KC.F4)
CE_TMAN = KC.LCTL(KC.LSFT(KC.ESC))
#endregion

#region Combos
combos.combos = [
    Chord((LHS_1, KC.Q,), CE_SAVE, match_coord=False),
    Chord(( 6,  7), SEL_ALL, match_coord=True),
    Chord((12, 13), CE_UNDO, match_coord=True),
    Chord(( 6, 12), KC.LGUI, match_coord=True),

    Chord(( 4,  5), KC.MO(3), match_coord=True), # Fn
    Chord((10, 11), KC.TG(1), match_coord=True), # Nav
    #Chord((KC.D, KC.V), KC.MT(KC.TG(2), KC.MO(2), prefer_hold=True, tap_interrupted=False, tap_time=100)), # Sym 
    Chord((16, 17), KC.MO(2), match_coord=True), # Sym

    Chord((24, 25), KC.LALT, match_coord=True),
    Chord((30, 31), KC.LSFT, match_coord=True),
    Chord((36, 37), KC.LCTL, match_coord=True),

    Chord((28, 29), KC.EQL, match_coord=True),
    #Chord((KC.O,    CE_QUOT), KC.NO),
    Chord((40, 41), KC.PIPE, match_coord=True),

    #Chord((CE_COMM, CE_DOT), KC.TG(2), timeout=30), # Sym
]
#endregion

#region Keymap
# https://github.com/KMKfw/kmk_firmware/blob/master/docs/en/keycodes.md
keyboard.keymap = [
    [ #0 Base layer
        LHS_1,   KC.Q,    KC.W,    KC.F,    KC.P,    KC.B,       KC.J,    KC.L,    KC.U,    KC.Y,    CE_SCLN, CE_MINS,
        LHS_2,   KC.A,    KC.R,    KC.S,    KC.T,    KC.G,       KC.M,    KC.N,    KC.E,    KC.I,    KC.O,    CE_QUOT, 
        LHS_3,   KC.Z,    KC.X,    KC.C,    KC.D,    KC.V,       KC.K,    KC.H,    CE_COMM, CE_DOT,  CE_BSLS, CE_EXLM, 
        _______, _______, _______, THM_L1,  THM_L2,  THM_L3,     THM_R1,  THM_R2,  THM_R3,  _______, _______, _______, 
    ], 
    [ #1 Nav on LHS, Numbers on RHS
        KC.TG(1),KC.HOME, KC.PGUP, KC.PGDN, KC.END,  KC.INS,     KC.TG(1),KC.P7,   KC.P8,   KC.P9,   KC.PERC, KC.NLCK, 
        KC.ESC,  KC.LEFT, KC.UP,   KC.DOWN, KC.RGHT, KC.ENT,     KC.PDOT, MR_P4,   MR_P5,   MR_P6,   MR_PAST, KC.PSLS, 
        KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,      KC.P0,   KC.P1,   KC.P2,   KC.P3,   KC.PPLS, KC.PMNS, 
        _______, _______, _______, KC.TRNS, KC.TRNS, KC.TRNS,    KC.TRNS, KC.TRNS, KC.TRNS, _______, _______, _______, 
    ],
    [ #2 Nav on LHS, Symbols on RHS
        KC.TG(2),KC.HOME, KC.PGUP, KC.PGDN, KC.END,  KC.NO,      KC.TG(2),KC.AMPR, KC.ASTR, KC.TILD, KC.LCBR, KC.RCBR,
        KC.TG(2),KC.LEFT, KC.UP,   KC.DOWN, KC.RGHT, KC.NO,      KC.PLUS, KC.DLR,  KC.PERC, KC.CIRC, KC.LBRC, KC.RBRC,
        KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,      KC.EQL,  KC.GRV,  KC.AT,   KC.HASH, KC.LABK, KC.RABK,
        _______, _______, _______, KC.TRNS, KC.TRNS, KC.TRNS,    KC.TRNS, KC.TRNS, KC.TRNS, _______, _______, _______, 
    ],
    [ #3 Home row mods on LHS, Fn on RHS
        KC.TG(3),KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,      CE_AF4,  KC.F7,   KC.F8,   KC.F9,   KC.F12,  KC.CAPS,
        KC.TG(3),KC.LGUI, KC.LALT, KC.LSFT, KC.LCTL, KC.NO,      CE_TMAN, KC.F4,   KC.F5,   KC.F4,   KC.F11,  KC.SLCK,
        KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,      KC.APP,  KC.F1,   KC.F2,   KC.F3,   KC.F10,  KC.PAUS,
        _______, _______, _______, KC.TRNS, KC.TRNS, KC.TRNS,    KC.TRNS, KC.TRNS, KC.TRNS, _______, _______, _______, 
    ],
]
#endregion

if __name__ == '__main__':
    keyboard.go()