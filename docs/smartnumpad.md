# Smart Numpad

Smart Numpad deactivates your `NUM` layer when pressing a non-numpad key, or after a timeout.

Based heavily upon the CapsWord module.

## Behaviour

- When the layer is toggled on, it will stay active until:

  - A non-numpad key is pressed

  - The timeout expires

  - A layer key is used that deactivates the layer

- When holding `KC.TG`, this module will only take effect on the release of `KC.TG`. Non-numpad presses during the hold have no effect. The timeout begins on key release.

- This module has no effect when using momentarily layer changes such as `KC.MO`, `KC.LM`, or `KC.LT`.

- If the specified numpad layer is the only one active (e.g., `KC.DF` or `KC.TO`), it will not deactivate the layer.

- This module overrides Layer Lock (`LLOCK`) in the Layers moduel.

## Usage

```python
from kmk.modules.smartnumpad import SmartNumPad

keyboard.modules.append(SmartNumPad(layer=1))
```
## Keycodes

|Key                    |Aliases             |Description                                    |
|-----------------------|--------------------|-----------------------------------------------|
|*none*                 |                    | N/A                                           |

## Interaction with Layer Keycodes

|Key                 |  Tap                              |  Hold                             |
|--------------------|-----------------------------------|-----------------------------------|
|`KC.DF(layer)`      | No effect<sup>1</sup>                         | No effect<sup>1</sup>                        |
|`KC.MO(layer)`      | N/A                               | No effect                         |
|`KC.LM(layer, mod)` | N/A                               | No effect                         |
|`KC.LT(layer, kc)`  | N/A                               | No effect                         |
|`KC.TL(layer, kc)`  | Normal behaviour                  | N/A                               |
|`KC.TG(layer)`      | Normal behaviour                  | Normal behaviour once released    |
|`KC.TO(layer)`      | No effect<sup>1</sup>                         | No effect<sup>1</sup>                         |
|`KC.TT(layer)`      | Normal behaviour                  | No effect                         |
|`KC.TH(layer)`      | Normal behaviour                  | No effect                         |
|`KC.LLOCK`          | Normal behaviour                  | N/A                               |

<ins>Notes:</ins>
1. Module has no effect when only one layer is active