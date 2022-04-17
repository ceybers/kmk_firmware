# Send ASCII Characters

Send [ASCII characters](https://www.asciitable.com/) to Windows desktops using the LALT + number pad technique.

e.g. `LALT` + `P0` + `P2` + `P4` + `P6` = `ö`

## Example

```python
from kmk.handlers.ascii_keys import send_ascii

keyboard = KMKKeyboard()

DIA_O = send_ascii("ö")

keyboard.keymap = [
	[
        DIA_O,   
    ],
]
```

## Considerations

* `send_ascii()` must be passed a string of exactly one character. It will raise an error if length <> 1. 
* This character must have an ASCII value of 255 or less, otherwise an error will be raised.
* `NumLock` must be enabled for Windows to process the combination.