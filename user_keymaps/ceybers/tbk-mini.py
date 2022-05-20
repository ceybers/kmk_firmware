from kb import KMKKeyboard
from kmk.keys import KC
from kmk.handlers.ascii_keys import send_ascii
from kmk.handlers.sequences import send_string, simple_key_sequence
from kmk.extensions.media_keys import MediaKeys
from kmk.modules.combos import Combos, Chord, Sequence
from kmk.modules.layers import Layers
from kmk.modules.modtap import ModTap
from kmk.modules.oneshot import OneShot
from kmk.modules.slowmods import SlowMods
from kmk.modules.split import Split
from kmk.modules.smartnumpad import SmartNumPad
from kmk.modules.sticky_mod import StickyMod
from kmk.modules.toggle_mods import ToggleMods

keyboard = KMKKeyboard()
keyboard.debug_enabled = False
keyboard.tap_time = 150

keyboard.extensions.append(MediaKeys())
 
modtap = ModTap()
modtap.tap_time = 150
keyboard.modules.append(modtap)

keyboard.modules.append(Split())
keyboard.modules.append(OneShot())
keyboard.modules.append(SlowMods())
keyboard.modules.append(Layers())
keyboard.modules.append(SmartNumPad(layer=1))
keyboard.modules.append(StickyMod())
keyboard.modules.append(ToggleMods())

combos = Combos()

# Override when SlowMods disabled

# KC.SSFT = KC.LSFT.clone()
# KC.SCTL = KC.LCTL.clone()
# KC.SALT = KC.LALT.clone()
# KC.SGUI = KC.LGUI.clone()
# KC.SCS = KC.LSFT.clone()

# Aliases for VS Code highlighting
_______ = KC.TRNS
XXXXX   = KC.NO
MRY_ACT = KC.TRNS

# Selection aliases
SEL_HOME = KC.LSFT(KC.HOME)
SEL_PGUP = KC.LSFT(KC.PGUP)
SEL_WLFT = KC.LCTL(KC.LSFT(KC.LEFT))
SEL_LEFT = KC.LSFT(KC.LEFT)
SEL_DOWN = KC.LSFT(KC.DOWN)
SEL_UP   = KC.LSFT(KC.UP)
SEL_RGHT = KC.LSFT(KC.RGHT)
SEL_WRGT = KC.LCTL(KC.LSFT(KC.RGHT))
SEL_PGDN = KC.LSFT(KC.PGDN)
SEL_END  = KC.LSFT(KC.END)

# Column up/down select - differs in VSCode and N++
# N++ can't change it, so change VSCode instead
COL_DOWN = KC.LCTL(KC.LSFT(KC.LALT(KC.DOWN))) # cursorColumnSelectDown
COL_UP   = KC.LCTL(KC.LSFT(KC.LALT(KC.UP)))   # cursorColumnSelectUp

# Aliases for delete word forward/back
CTL_BSPC = KC.LCTL(KC.BSPC)
CTL_DEL  = KC.LCTL(KC.DEL)

# Aliases for Copy/Paste/Undo etc.
C_UNDO = KC.SCTL(KC.Z)
C_CUT  = KC.SCTL(KC.X)
C_COPY = KC.SCTL(KC.C)
C_PSTE = KC.SCTL(KC.V)
C_REDO = KC.SCTL(KC.Y)
C_SAVE = KC.SCTL(KC.S)
C_SALL  = KC.SCTL(KC.A)
C_FINDN = KC.F3
C_REPL  = KC.SCTL(KC.H)
C_FINDP = KC.SSFT(KC.F3)
C_INDNT = KC.SCTL(KC.LBRC)
C_OTDNT = KC.SCTL(KC.RBRC)

# Aliases for tile manager/multimonitor hotkeys
TM_LHS = KC.LGUI(KC.LEFT)
TM_RHS = KC.LGUI(KC.RGHT)
TM_UP  = KC.LGUI(KC.UP)
TM_DN  = KC.LGUI(KC.DOWN)
MM_LHS = KC.LGUI(KC.LSFT(KC.LEFT))
MM_RHS = KC.LGUI(KC.LSFT(KC.RGHT))
MM_CAT = KC.LCTL(KC.LALT(KC.TAB)) # Alt+Tab that stays open
TSKMN =  KC.LCTL(KC.LSFT(KC.ESC))
ALT_F4 = KC.LALT(KC.F4)
ALT_TL = KC.SM(KC.TAB, KC.LSFT(KC.LALT))
ALT_TR = KC.SM(KC.TAB, KC.LALT)
ALT_T1 = KC.LALT(KC.TAB)

# Browser aliases
BR_NEW = KC.SCTL(KC.T)
BR_CLS = KC.SCTL(KC.W)
BR_OLD = KC.SCS(KC.T)
BR_INC = KC.SCS(KC.N)
BR_HISL = KC.SALT(KC.LEFT)
BR_HISR = KC.SALT(KC.RGHT)
BR_TABL = KC.SCS(KC.TAB)
BR_TABR = KC.SCTL(KC.TAB)
BR_ADDY = KC.SCTL(KC.L)
BR_NEWW = KC.SCTL(KC.N)

# Definitely my bank account PIN
CE_PIN = send_string("0000\n")


# Auto-shift for symbols/punctuation on base layer
# Re-arranged based on frequency of use
ac_hold_time = 100
AC_SCLN = KC.MT(KC.SCLN, KC.LSFT(KC.SCLN), prefer_hold=False, tap_time=ac_hold_time) # 
AC_MINS = KC.MT(KC.MINS, KC.LSFT(KC.MINS), prefer_hold=False, tap_time=ac_hold_time) #-_-_
AC_QUOT = KC.MT(KC.LSFT(KC.QUOT), KC.QUOT, prefer_hold=False, tap_time=ac_hold_time) # ' " changed to " '
AC_COMM = KC.MT(KC.COMM, KC.LSFT(KC.N9),   prefer_hold=False, tap_time=ac_hold_time) # , < changed to , (
AC_DOT  = KC.MT(KC.DOT,  KC.LSFT(KC.N0),   prefer_hold=False, tap_time=ac_hold_time) # . > changed to . )
AC_SLSH = KC.MT(KC.QUES, KC.LSFT(KC.EQL),  prefer_hold=False, tap_time=ac_hold_time) # / ? changed to ? +
AC_EQL  = KC.MT(KC.EXLM, KC.EQL,           prefer_hold=False, tap_time=ac_hold_time) # = + changed to ! =

# Select Word by Rafael Romão
# Src: https://github.com/rafaelromao/keyboards/blob/main/docs/navigation.md#select-word
SEL_WRD = simple_key_sequence((KC.RGHT, KC.LEFT, KC.LCTL(KC.LEFT), KC.LSFT(KC.LCTL(KC.RGHT)),))

# Pontuation Keys
# By Rafael Romão
PN_COMM = simple_key_sequence((KC.END, KC.COMM,))
PN_SCLN = simple_key_sequence((KC.END, KC.SCLN,))
PN_DOT  = simple_key_sequence((KC.END, KC.DOT,))

# Left-most column on a 3x6+3 LHS board
# Use KC.LCTL(KC.Z) because SlowMod/SCTL doesn't work with ModTap/KC.MT
LHS_1 = KC.MT(KC.PSCR, KC.LCTL(KC.X), prefer_hold=False) 
LHS_2 = KC.MT(KC.ESC,  KC.LCTL(KC.C), prefer_hold=False)
LHS_3 = KC.MT(KC.TAB,  KC.LCTL(KC.V), prefer_hold=False)

# Thumb buttons tab & hold
THM_L1 = KC.TL(2, KC.LSFT, prefer_hold=True)
THM_L2 = KC.SPC
THM_L3 = KC.LT(3, KC.DEL, prefer_hold=True)
THM_R1 = KC.BSPC
THM_R2 = KC.ENT
THM_R3 = KC.TL(1, KC.LCTL, prefer_hold=True)

# Lots and lots of chords
combos.combos = [
    Chord((KC.DEL,  KC.BSPC), KC.TG(3)), 

# LHS Chords
    Chord((LHS_1,   KC.Q),    C_UNDO),   # C12 R1
    Chord((KC.Q,    KC.W),    C_REDO),   # C23 R1
    Chord((LHS_2,   KC.A),    C_SALL),   # C12 R2
    Chord((LHS_3,   KC.Z),    C_SAVE),   # C12 R3
    Chord((LHS_2,   LHS_3),   KC.LGUI),  # C1 R23
    Chord((KC.A,    KC.Z),    KC.LALT),  # C2 R23

    Chord((KC.P,    KC.B),    BR_NEW),   # C56 R1
    Chord((KC.T,    KC.G),    BR_OLD),   # C56 R2
    Chord((KC.D,    KC.V),    BR_CLS),   # C56 R3
    Chord((KC.B,    KC.V),    BR_INC),   # C6 R13
    Chord((KC.P,    KC.T),    BR_HISL),  # C5 R12
    Chord((KC.B,    KC.G),    BR_HISR),  # C6 R12
    Chord((KC.T,    KC.D),    BR_TABL),  # C5 R12
    Chord((KC.G,    KC.V),    BR_TABR),  # C6 R12

# RHS Chords
    Chord((KC.J,    KC.L),    BR_ADDY),  # C12 R1
    Chord((KC.M,    KC.N),    BR_NEWW),  # C12 R2
    Chord((KC.K,    KC.H),    ALT_T1),   # C12 R3
    Chord((KC.J,    KC.M),    C_FINDN),  # C1 R12
    Chord((KC.J,    KC.K),    C_REPL),   # C1 R13
    Chord((KC.M,    KC.K),    C_FINDP),  # C1 R23 

    Chord((AC_SCLN, AC_MINS), KC.BSLS),  # C56 R1
    Chord((KC.O,    AC_QUOT), KC.PIPE),  # C56 R2
    Chord((AC_SLSH, AC_EQL),  KC.SLSH),  # C56 R3

    Chord((AC_MINS, AC_QUOT), KC.TILD),   #C6 R12
    Chord((AC_MINS, AC_EQL),  KC.TG(4)),  #C6 R13
    Chord((AC_QUOT, AC_EQL),  KC.GRV),    #C6 R23

# Contraction Sequences
    Sequence((AC_QUOT, KC.M), send_string("'m"),  timeout=200),
    Sequence((AC_QUOT, KC.S), send_string("'s"),  timeout=200),
    Sequence((AC_QUOT, KC.D), send_string("'d"),  timeout=200),
    Sequence((AC_QUOT, KC.T), send_string("'t"),  timeout=200),
    Sequence((AC_QUOT, KC.L), send_string("'ll"), timeout=200),
    Sequence((AC_QUOT, KC.R), send_string("'re"), timeout=200),
    Sequence((AC_QUOT, KC.V), send_string("'ve"), timeout=200),

# Accent Sequences
    Sequence((AC_SCLN, KC.A), send_ascii("ä"), timeout=200),
    Sequence((AC_SCLN, KC.E), send_ascii("ë"), timeout=200),
    Sequence((AC_SCLN, KC.I), send_ascii("ï"), timeout=200),
    Sequence((AC_SCLN, KC.O), send_ascii("ö"), timeout=200),
    Sequence((AC_SCLN, KC.U), send_ascii("ü"), timeout=200),
]

keyboard.modules.append(combos)

# Some extra ASCII characters
ASC_DEG = send_ascii("°")
ASC_BUL = send_ascii("·")
ASC_STR = send_ascii("ø")
ASC_MUL = send_ascii("×")

SLOW_MOD = KC.SLOWMODS

# Actual keymap
keyboard.keymap = [
    [ #0 Base
        LHS_1,   KC.Q,    KC.W,    KC.F,    KC.P,    KC.B,       KC.J,    KC.L,    KC.U,    KC.Y,    AC_SCLN, AC_MINS, # U  Y  ;: -_ \ ~
        LHS_2,   KC.A,    KC.R,    KC.S,    KC.T,    KC.G,       KC.M,    KC.N,    KC.E,    KC.I,    KC.O,    AC_QUOT, # E  I  O  "' | 
        LHS_3,   KC.Z,    KC.X,    KC.C,    KC.D,    KC.V,       KC.K,    KC.H,    AC_COMM, AC_DOT,  AC_SLSH, AC_EQL,  # ,( .) ?+ != / `
        XXXXX,   XXXXX,   XXXXX,   THM_L1,  THM_L2,  THM_L3,     THM_R1,  THM_R2,  THM_R3,  XXXXX,   XXXXX,   XXXXX   ],

    [ #1 Num
        KC.TO(0),KC.LPRN, KC.NO,   KC.NO,   KC.RPRN, KC.NO,      KC.NLCK, KC.P7,   KC.P8,   KC.P9,   KC.EQL,  KC.LLOCK,
        KC.NO,   KC.TGUI, KC.TALT, KC.TSFT, KC.TCTL, KC.NO,      KC.PDOT, KC.P4,   KC.P5,   KC.P6,   KC.PSLS, KC.PAST,
        KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,      KC.P0,   KC.P1,   KC.P2,   KC.P3,   KC.PMNS, KC.PPLS,
        XXXXX,   XXXXX,   XXXXX,    _______,_______, _______,    _______, _______, MRY_ACT, XXXXX,   XXXXX,   XXXXX   ],

    [ #2 Nav
        KC.TO(0),KC.HOME, KC.PGUP, KC.PGDN, KC.END,  KC.INS,     KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,
        LHS_2,   KC.LEFT, KC.UP,   KC.DOWN, KC.RGHT, KC.ENT,     SEL_WRD, KC.TCTL, KC.TSFT, KC.TALT, KC.TGUI, KC.NO,
        SEL_HOME,SEL_WLFT,COL_UP,  COL_DOWN,SEL_WRGT,SEL_END,    MM_CAT,  ALT_TL,  MM_LHS,  MM_RHS,  ALT_TR,  KC.NO,
        XXXXX,   XXXXX,   XXXXX,   MRY_ACT, _______, _______,    _______, _______, _______, XXXXX,   XXXXX,   XXXXX   ],

    [ #3 RHS Symbols and Brackets
        KC.TO(0),KC.NO,   KC.NO,   KC.NO,   KC.LPRN, KC.RPRN,    ASC_DEG, KC.AMPR, KC.ASTR, KC.NO,   KC.LABK, KC.RABK,
        KC.NO,   CTL_BSPC,KC.BSPC, KC.DEL,  CTL_DEL, ASC_MUL,    ASC_BUL, KC.DLR,  KC.PERC, KC.CIRC, KC.LCBR, KC.RCBR,
        SLOW_MOD,C_INDNT, KC.NO,   KC.NO,   C_OTDNT, KC.LLOCK,   ASC_STR, KC.EXLM, KC.AT,   KC.HASH, KC.LBRC, KC.RBRC,
        XXXXX,   XXXXX,   XXXXX,   KC.TG(3),_______, MRY_ACT,    _______, CE_PIN,  KC.TG(3),XXXXX,   XXXXX,   XXXXX   ],
    [ #4 RHS Fn keys
        KC.TO(0),TM_LHS,  TM_DN,   TM_UP,   TM_RHS,  TSKMN,      ALT_F4,  KC.F7,   KC.F8,   KC.F9,   KC.F12,  KC.CAPS,
        KC.NO,   KC.LGUI, KC.LALT, KC.LSFT, KC.LCTL, KC.NO,      KC.NO,   KC.F4,   KC.F5,   KC.F6,   KC.F11,  KC.SLCK,
        KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.LLOCK,   KC.APP,  KC.F1,   KC.F2,   KC.F3,   KC.F10,  KC.PAUS,
        XXXXX,   XXXXX,   XXXXX,   KC.LSFT, _______, _______,    _______, _______, KC.LCTL, XXXXX,   XXXXX,   XXXXX   ],
]

if __name__ == '__main__':
    keyboard.go()