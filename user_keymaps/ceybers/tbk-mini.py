from kb import KMKKeyboard
from kmk.keys import KC
from kmk.handlers.sequences import send_string, simple_key_sequence
from kmk.extensions.media_keys import MediaKeys
from kmk.modules.combos import Combos, Chord, Sequence
from kmk.modules.layers import Layers
from kmk.modules.modtap import ModTap
from kmk.modules.oneshot import OneShot
from kmk.modules.slowmods import SlowMods
from kmk.handlers.ascii_keys import send_ascii
from kmk.modules.split import Split, SplitSide

keyboard = KMKKeyboard()
keyboard.debug_enabled = False
keyboard.tap_time = 150

keyboard.extensions.append(MediaKeys())

split = Split(split_side=SplitSide.LEFT)
keyboard.modules.append(split)
 
modtap = ModTap()
modtap.tap_time = 150
keyboard.modules.append(modtap)

keyboard.modules.append(OneShot())
keyboard.modules.append(SlowMods())
keyboard.modules.append(Layers())

combos = Combos()
keyboard.modules.append(combos)

# Aliases for VS Code highlighting
_______ = KC.TRNS
XXXXX   = KC.NO

# Aliases for brackets using Slow-Shift for RDP/VM
SS_LPRN = KC.LSFT(KC.N9)
SS_RPRN = KC.LSFT(KC.N0)
SS_LABK = KC.LSFT(KC.COMM)
SS_RABK = KC.LSFT(KC.DOT)
SS_LCBR = KC.LSFT(KC.LBRC)
SS_RCBR = KC.LSFT(KC.RBRC)
SS_LSBR = send_string('[')
SS_RSBR = send_string(']')

# Selection aliases
SEL_HOME = KC.LSFT(KC.HOME)
SEL_LEFT = KC.LCTL(KC.LSFT(KC.LEFT))
COL_DOWN = KC.LSFT(KC.LALT(KC.DOWN))
COL_UP   = KC.LSFT(KC.LALT(KC.UP))
SEL_RGHT = KC.LCTL(KC.LSFT(KC.RGHT))                           
SEL_END  = KC.LSFT(KC.END)
SEL_ALL  = KC.LCTL(KC.A)

# Aliases for delete word forward/back
CTL_BSPC = KC.LCTL(KC.BSPC)
CTL_DEL  = KC.LCTL(KC.DEL)

# Aliases for Copy/Paste/Undo etc.
C_UNDO = KC.SCTL(KC.Z)
C_CUT  = KC.SCTL(KC.X)
C_COPY = KC.LCTL(KC.C)
C_PSTE = KC.SCTL(KC.V)
C_REDO = KC.SCTL(KC.Y)
C_SAVE = KC.SCTL(KC.S)

# Aliases for tile manager/multimonitor hotkeys
TM_LHS = KC.LGUI(KC.LEFT)
TM_RHS = KC.LGUI(KC.RGHT)
TM_UP  = KC.LGUI(KC.UP)
TM_DN  = KC.LGUI(KC.DOWN)
MM_LHS = KC.LGUI(KC.LSFT(KC.LEFT))
MM_RHS = KC.LGUI(KC.LSFT(KC.RGHT))
MM_CAT = KC.LCTL(KC.LALT(KC.TAB)) # Alt+Tab that stays open
TSKMN =  KC.LCTL(KC.LSFT(KC.ESC))

# Browser aliases
BR_NEW = KC.SCTL(KC.T)
BR_CLS = KC.SCTL(KC.W)
BR_OLD = KC.SCS(KC.T)
BR_INC = KC.SCS(KC.N)
BR_PRV = KC.SALT(KC.LEFT)
BR_NXT = KC.SALT(KC.RGHT)

# Definitely my bank account PIN
CE_PIN = send_string("0000\n")

# Auto "Caps" tap & hold for symbols on base layer
# /? is changed to ?!
ac_hold_time = 100
AC_SCLN = KC.MT(KC.SCLN, KC.LSFT(KC.SCLN), prefer_hold=False, tap_time=ac_hold_time)
AC_MINS = KC.MT(KC.MINS, KC.LSFT(KC.MINS), prefer_hold=False, tap_time=ac_hold_time)
AC_QUOT = KC.MT(KC.LSFT(KC.QUOT), KC.QUOT, prefer_hold=False, tap_time=ac_hold_time)
AC_COMM = KC.MT(KC.COMM, KC.LSFT(KC.N9),   prefer_hold=False, tap_time=ac_hold_time)
AC_DOT  = KC.MT(KC.DOT,  KC.LSFT(KC.N0),   prefer_hold=False, tap_time=ac_hold_time)
AC_SLSH = KC.MT(KC.QUES, KC.LSFT(KC.EQL),  prefer_hold=False, tap_time=ac_hold_time)
AC_EQL  = KC.MT(KC.EXLM, KC.EQL,           prefer_hold=False, tap_time=ac_hold_time)

# Select Word by Rafael Romão https://github.com/rafaelromao/keyboards/blob/main/docs/navigation.md#select-word
SEL_WRD = simple_key_sequence((KC.RGHT, KC.LEFT, KC.LCTL(KC.LEFT), KC.LSFT(KC.LCTL(KC.RGHT)),))

# 
LHS_1 = KC.MT(KC.PSCR, KC.LCTL(KC.Z)) #KC.LM(3, KC.LSFT1235) # KC.TL(3,      KC.NO,  prefer_hold=True)  #KC.MO(3)
LHS_2 = KC.MT(KC.ESC, KC.LGUI, prefer_hold=False)
LHS_3 = KC.MT(KC.TAB, KC.LALT, prefer_hold=False) #KC.LT(4, KC.TAB, prefer_hold=False, tap_time=300)   

# Thumb buttons tab & hold
MRY_L1 = KC.TL(1, KC.LSFT, prefer_hold=True)
MRY_L2 = KC.SPC
MRY_L3 = KC.TL(2, KC.LCTL, prefer_hold=True)

MRY_R1 = KC.BSPC      
MRY_R2 = KC.ENT
MRY_R3 = KC.MT(KC.DEL, KC.LCTL, prefer_hold=True)

# Lots and lots of chords
combos.combos = [
    Chord((LHS_1,   KC.Q),    C_CUT),
    Chord((LHS_2,   KC.A),    C_COPY),
    Chord((LHS_3,   KC.Z),    C_PSTE),
    Chord((KC.Q,    KC.Z),    SEL_ALL),

    Chord((LHS_1,   LHS_2),   C_SAVE),
    Chord((LHS_2,   LHS_3),   KC.LM(3, KC.LSFT)),
    Chord((KC.A,    KC.Z),    KC.MO(4)),
   
    Chord((KC.P,    KC.B),    BR_NEW),
    Chord((KC.T,    KC.G),    BR_OLD),
    Chord((KC.D,    KC.V),    BR_CLS),
    Chord((KC.B,    KC.V),    BR_INC),
    # Chord((KC.P,    KC.T),    BR_PRV),
    # Chord((KC.T,    KC.D),    BR_NXT),
   
    Chord((KC.J,    KC.L),    KC.MPRV),
    Chord((KC.M,    KC.N),    KC.MPLY),
    Chord((KC.K,    KC.H),    KC.MNXT),
    Chord((KC.J,    KC.M),    KC.VOLU),
    # Chord((KC.J,    KC.K),    KC.MUTE),
    # Chord((KC.M,    KC.K),    KC.VOLD),
    
    Chord((AC_SCLN, AC_MINS), KC.BSLS),
    Chord((KC.O,    AC_QUOT), KC.PIPE),
    Chord((AC_SLSH, AC_EQL),  KC.SLSH),
   
    Chord((AC_MINS, AC_QUOT), KC.TILD),
    Chord((AC_QUOT, AC_EQL),  KC.GRV),
   
    Chord((AC_COMM, AC_DOT),  KC.LALT(KC.TAB)),
   
    # Sequence((AC_QUOT, KC.M), send_string("'m"),  timeout=100),
    # Sequence((AC_QUOT, KC.S), send_string("'s"),  timeout=100),
    # Sequence((AC_QUOT, KC.D), send_string("'d"),  timeout=100),
    # Sequence((AC_QUOT, KC.T), send_string("'t"),  timeout=100),
    # Sequence((AC_QUOT, KC.L), send_string("'ll"), timeout=100),
    # Sequence((AC_QUOT, KC.R), send_string("'re"), timeout=100), 
    # Sequence((AC_QUOT, KC.V), send_string("'ve"), timeout=100),

    Sequence((AC_SCLN, KC.A), send_ascii("ä"), timeout=200),
    Sequence((AC_SCLN, KC.E), send_ascii("ë"), timeout=200),
    Sequence((AC_SCLN, KC.I), send_ascii("ï"), timeout=200),
    Sequence((AC_SCLN, KC.O), send_ascii("ö"), timeout=200),
    Sequence((AC_SCLN, KC.U), send_ascii("ü"), timeout=200),
]

# Actual keymap
keyboard.keymap = [
    [ #0 Base
        LHS_1,   KC.Q,    KC.W,    KC.F,    KC.P,    KC.B,       KC.J,    KC.L,    KC.U,    KC.Y,    AC_SCLN, AC_MINS,
        LHS_2,   KC.A,    KC.R,    KC.S,    KC.T,    KC.G,       KC.M,    KC.N,    KC.E,    KC.I,    KC.O,    AC_QUOT,
        LHS_3,   KC.Z,    KC.X,    KC.C,    KC.D,    KC.V,       KC.K,    KC.H,    AC_COMM, AC_DOT,  AC_SLSH, AC_EQL,
        XXXXX,   XXXXX,   XXXXX,   MRY_L1,  MRY_L2,  MRY_L3,     MRY_R1,  MRY_R2,  MRY_R3,  XXXXX,   XXXXX,   XXXXX   ],

    [ #1 Numpad
        KC.PSLS, KC.PAST, KC.P7,   KC.P8,   KC.P9,   KC.PMNS,    KC.BSLS, KC.P7,   KC.P8,   KC.P9,   KC.PSLS, KC.NLCK,
        KC.NLCK, KC.BSLS, KC.P4,   KC.P5,   KC.P6,   KC.PPLS,    KC.PDOT, KC.P4,   KC.P5,   KC.P6,   KC.PMNS, KC.PAST,
        KC.PDOT, KC.P0,   KC.P1,   KC.P2,   KC.P3,   KC.ENT,     KC.P0,   KC.P1,   KC.P2,   KC.P3,   KC.PPLS, KC.EQL,
        XXXXX,   XXXXX,   XXXXX,   _______, _______, _______,    _______, _______, _______, XXXXX,   XXXXX,   XXXXX   ],

    [ #2 Nav       
        MM_CAT,  KC.HOME, KC.PGDN, KC.PGUP, KC.END,  KC.INS,     SEL_WRD, KC.LSFT(KC.PGUP), SEL_HOME,         SEL_END,        KC.LSFT(KC.PGDN), KC.NO,
        LHS_2,   KC.LEFT, KC.DOWN, KC.UP,   KC.RGHT, KC.ENT,     SEL_LEFT,KC.LSFT(KC.LEFT), KC.LSFT(KC.DOWN), KC.LSFT(KC.UP), KC.LSFT(KC.RGHT), SEL_RGHT,
        SEL_HOME,SEL_LEFT,COL_DOWN,COL_UP,  SEL_RGHT,SEL_END,    KC.NO,   KC.NO,   COL_DOWN,COL_UP,  KC.NO,   KC.NO,
        XXXXX,   XXXXX,   XXXXX,   _______, _______, _______,    _______, _______, _______, XXXXX,   XXXXX,   XXXXX   ],
    
    [ #3 RHS Normal numbers and brackets
        KC.TRNS, KC.NO,   KC.AMPR, KC.ASTR, KC.NO,   KC.NO,      KC.NO,   KC.N7,   KC.N8,   KC.NO,   KC.COMM, KC.DOT,   
        KC.TRNS, KC.NO,   KC.DLR,  KC.PERC, KC.CIRC, KC.NO,      KC.NO,   KC.N4,   KC.N5,   KC.N6,   KC.LBRC, KC.RBRC,
        KC.TRNS, KC.NO,   KC.EXLM, KC.AT,   KC.HASH, KC.NO,      KC.NO,   KC.N1,   KC.N2,   KC.N3,   SS_LSBR, SS_RSBR,
        XXXXX,   XXXXX,   XXXXX,   _______, _______, KC.TO(0),   _______, CE_PIN,  _______, XXXXX,   XXXXX,   XXXXX   ],

    [ #4 RHS Fn keys
        LHS_1,   TM_LHS,  TM_DN,   TM_UP,   TM_RHS,  KC.NO,      TSKMN,   KC.F7,   KC.F8,   KC.F9,   KC.F12,  KC.PSCR,
        LHS_2,   KC.LGUI, KC.LALT, KC.LSFT, KC.LCTL, KC.NO,      KC.CAPS, KC.F4,   KC.F5,   KC.F6,   KC.F11,  KC.SLCK,
        LHS_3,   MM_LHS,  KC.NO,   KC.NO,   MM_RHS,  KC.NO,      KC.APP,  KC.F1,   KC.F2,   KC.F3,   KC.F10,  KC.PAUS,
        XXXXX,   XXXXX,   XXXXX,   KC.LSFT, _______, KC.TO(0),   _______, _______, _______, XXXXX,   XXXXX,   XXXXX   ],
]

if __name__ == '__main__':
    keyboard.go()