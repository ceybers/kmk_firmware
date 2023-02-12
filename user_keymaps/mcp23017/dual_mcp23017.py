'''
Firmware for a split keyboard using an MCP23017 I/O expander for each half, 
and a central RP2040 board to run KMK on. The expanders are connected to the
RP2040 board via 4-pin wires, and handle both columns and rows.
'''

import board
import busio

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.scanners.mcpscanner import MCPScanner

i2c = busio.I2C(scl=board.GP1, sda=board.GP0, frequency=400000)

keyboard = KMKKeyboard()
keyboard.matrix = [
    MCPScanner( # LHS MCP23017 I/O Expander
        row_pins = [0, 1, 2, 3],
        col_pins = [8, 9, 10, 11, 12, 13],
        i2c = i2c,
        i2c_address = 0x20,
        offset = 0
    ),
    MCPScanner( # RHS MCP23017 I/O Expander
        row_pins = [0, 1, 2, 3],
        col_pins = [8, 9, 10, 12, 11, 13],
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

keyboard.keymap = [
    [
        KC.LALT, KC.Q,    KC.W,    KC.F,    KC.P,    KC.B,       KC.J,    KC.L,    KC.U,    KC.Y,    KC.SCLN, KC.MINS,
        KC.ESC,  KC.A,    KC.R,    KC.S,    KC.T,    KC.G,       KC.M,    KC.N,    KC.E,    KC.I,    KC.O,    KC.QUOT, 
        KC.TAB,  KC.Z,    KC.X,    KC.C,    KC.D,    KC.V,       KC.K,    KC.H,    KC.COMM, KC.DOT,  KC.BSLS, KC.EXLM, 
        KC.NO,   KC.NO,   KC.NO,   KC.LSFT, KC.SPC,  KC.LCTL,    KC.BSPC, KC.ENT,  KC.DEL,  KC.NO,   KC.NO,   KC.NO, 
    ],
]

if __name__ == '__main__':
    keyboard.go()