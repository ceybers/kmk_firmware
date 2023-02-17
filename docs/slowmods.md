# Slow Modifiers

This module provides a workaround to address issues with sending modified keycodes on Windows over Hyper-V, Remote Desktop, or Spice.

Additionally, tt will automatically apply to [US ANSI Shifted Symbols](keycodes.md#us-ansi-shifted-symbols) keycodes, i.e. shifted keycodes between `KC.TILD` and `KC.QUES`. 

## Example
```python
from kmk.modules.slowmods import SlowMods

keyboard.modules.append(SlowMods())

SEL_ALL = KC.SL(KC.A, KC.LCTL)

keyboard.keymap = [
	[
        SEL_ALL,
    ],
]
```

## Keycodes
|Keycode                         | Description              |
|--------------------------------|--------------------------|
|SEL_ALL = KC.LT(base, modifier) | mod + base               |
|SEL_ALL = KC.LT(KC.A, KC.LCTL)  | `LCTL` + `A`             |
|SLOW_AT = KC.LT(KC.N2,KC.LSFT)  | `LSFT` + `2`             |
|S_ALT_F = KC.LT(KC.F, KC.LALT)  | `LALT` + `F`             |
|S_GUI_E = KC.LT(KC.E, KC.LGUI)  | `LGUI` + `E`             |


## Issue
Sending a key such as `KC.LCTL(C)` via these clients occasionally results in the following behaviour:

```
KEY-DOWN - QMK: KC_LCTL Event key: Control     Code: ControlLeft   KeyCode: 17
KEY-UP   - QMK: KC_LCTL Event key: Control     Code: ControlLeft   KeyCode: 17 in 7.230ms
KEY-DOWN - QMK: KC_C    Event key: c           Code: KeyC          KeyCode: 67
KEY-UP   - QMK: KC_C    Event key: c           Code: KeyC          KeyCode: 67 in 183.920ms
```

Rather than the expected:
```
KEY-DOWN - QMK: KC_LCTL Event key: Control     Code: ControlLeft   KeyCode: 17
KEY-DOWN - QMK: KC_C    Event key: c           Code: KeyC          KeyCode: 67
KEY-UP   - QMK: KC_C    Event key: c           Code: KeyC          KeyCode: 67 in 137.250ms
KEY-UP   - QMK: KC_LCTL Event key: Control     Code: ControlLeft   KeyCode: 17 in 158.335ms
```

This module works around this issue by first sending the modifier key press as a separate HID event, then sending the base key as a separate key press. This is as opposed to sending on HID event with the modifier applied to the base key.