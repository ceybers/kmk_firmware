import board # type: ignore

from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.scanners import DiodeOrientation

class KMKKeyboard(_KMKKeyboard):
    diode_orientation = DiodeOrientation.COL2ROW
    # LHS
    col_pins  = (board.GP21, board.GP20, board.GP19, board.GP18, board.GP17, board.GP16)
    row_pins  = (board.GP22, board.GP26, board.GP27, board.GP28)
    data_pin  = board.GP13
    data_pin2 = board.GP12
    # RHS
    # col_pins  = (board.GP11, board.GP10, board.GP9,  board.GP8,  board.GP7,  board.GP6)
    # row_pins  = (board.GP12, board.GP13, board.GP14, board.GP15)
    # data_pin  = board.GP0
    # data_pin2 = board.GP1