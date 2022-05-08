# Toggle Mods

This module toggles modifiers between a pressed state and a released state when tapping the key.

Operates in a similar manner to Windows Sticky Keys, in that modifiers are locked or unlocked with a tap of the key.

Differs from [One Shot mods](oneshot.md) and [Sticky Mod](sticky_mod.md) in that it stays active regardless of which keys you press, how many keys you press, or timeouts.

Modifiers will be reset when changing layers.

## Enabling the module
```python
from kmk.modules.toggle_mods import ToggleMods

keyboard.modules.append(ToggleMods())

keyboard.keymap = [
	[
        KC.TSFT, 
        KC.TCTL, 
        KC.LEFT, 
        KC.RGHT,
    ],
]
```

