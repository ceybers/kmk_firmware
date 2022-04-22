# Media Keys
Media keys extension adds keys for common media control keys. It can simply be 
added to the extensions list.

```python
from kmk.extensions.media_keys import MediaKeys
keyboard.extensions.append(MediaKeys())
```
 
 ## Keycodes

|Key                    |Aliases             |Description                                    |
|-----------------------|--------------------|-----------------------------------------------|
|`KC.AUDIO_MUTE`        |`KC.MUTE`           |Mute                                           |
|`KC.AUDIO_VOL_UP`      |`KC.VOLU`           |Volume Up                                      |
|`KC.AUDIO_VOL_DOWN`    |`KC.VOLD`           |Volume Down                                    |
|`KC.MEDIA_NEXT_TRACK`  |`KC.MNXT`           |Next Track (Windows)                           |
|`KC.MEDIA_PREV_TRACK`  |`KC.MPRV`           |Previous Track (Windows)                       |
|`KC.MEDIA_STOP`        |`KC.MSTP`           |Stop Track (Windows)                           |
|`KC.MEDIA_PLAY_PAUSE`  |`KC.MPLY`           |Play/Pause Track                               |
|`KC.MEDIA_EJECT`       |`KC.EJCT`           |Eject (macOS)                                  |
|`KC.MEDIA_FAST_FORWARD`|`KC.MFFD`           |Next Track (macOS)                             |
|`KC.MEDIA_REWIND`      |`KC.MRWD`           |Previous Track (macOS)                         |

 ## Keycodes (Application Launch)

|Key                    |Aliases             |Description                                    |
|-----------------------|--------------------|-----------------------------------------------|
|`KC.MEDIA_SELECT`      |`KC.MSEL`           | Launch Media Player                           |
|`KC.MAIL`              |                    | Launch Mail                                   |
|`KC.CALCULATOR`        |`KC.CALC`           | Launch Calculator                             |
|`KC.EXPLORER`          |`KC.EXPL`           | Launch My Computer                            |
|`KC.AC_SEARCH`         |                    | Browser Search                                |
|`KC.AC_HOME`           |                    | Browser Home                                  |
|`KC.AC_BACK`           |                    | Browser Back                                  |
|`KC.AC_FORWARD`        |                    | Browser Forward                               |
|`KC.AC_STOP`           |                    | Browser Stop                                  |
