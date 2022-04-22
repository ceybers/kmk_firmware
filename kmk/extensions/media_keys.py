from kmk.extensions import Extension
from kmk.keys import make_consumer_key


class MediaKeys(Extension):
    def __init__(self):
        # Consumer ("media") keys. Most known keys aren't supported here. A much
        # longer list used to exist in this file, but the codes were almost certainly
        # incorrect, conflicting with each other, or otherwise 'weird'. We'll add them
        # back in piecemeal as needed. PRs welcome.
        #
        # A super useful reference for these is http://www.freebsddiary.org/APC/usb_hid_usages.php
        # Note that currently we only have the PC codes. Recent MacOS versions seem to
        # support PC media keys, so I don't know how much value we would get out of
        # adding the old Apple-specific consumer codes, but again, PRs welcome if the
        # lack of them impacts you.
        make_consumer_key(code=226, names=('AUDIO_MUTE', 'MUTE'))  # 0xE2
        make_consumer_key(code=233, names=('AUDIO_VOL_UP', 'VOLU'))  # 0xE9
        make_consumer_key(code=234, names=('AUDIO_VOL_DOWN', 'VOLD'))  # 0xEA
        make_consumer_key(code=181, names=('MEDIA_NEXT_TRACK', 'MNXT'))  # 0xB5
        make_consumer_key(code=182, names=('MEDIA_PREV_TRACK', 'MPRV'))  # 0xB6
        make_consumer_key(code=183, names=('MEDIA_STOP', 'MSTP'))  # 0xB7
        make_consumer_key(
            code=205, names=('MEDIA_PLAY_PAUSE', 'MPLY')
        )  # 0xCD (this may not be right)
        make_consumer_key(code=184, names=('MEDIA_EJECT', 'EJCT'))  # 0xB8
        make_consumer_key(code=179, names=('MEDIA_FAST_FORWARD', 'MFFD'))  # 0xB3
        make_consumer_key(code=180, names=('MEDIA_REWIND', 'MRWD'))  # 0xB4
        # 15.15 Application Launch Buttons
        make_consumer_key(code=0x0183, names=('MEDIA_SELECT', 'MSEL',))  
        make_consumer_key(code=0x018A, names=('MAIL',))  
        make_consumer_key(code=0x0192, names=('CALCULATOR', 'CALC',))  
        make_consumer_key(code=0x0194, names=('EXPLORER', 'EXPL',))
        # make_consumer_key(code=0x0196, names=('BROWSER', 'WWW',)) # This does not seem to work on Windows 10
        make_consumer_key(code=0x0221, names=('AC_SEARCH',))  
        make_consumer_key(code=0x0223, names=('AC_HOME',))  
        make_consumer_key(code=0x0224, names=('AC_BACK',))  
        make_consumer_key(code=0x0225, names=('AC_FORWARD',))  
        make_consumer_key(code=0x0226, names=('AC_STOP',))  

    def on_runtime_enable(self, sandbox):
        return

    def on_runtime_disable(self, sandbox):
        return

    def during_bootup(self, sandbox):
        return

    def before_matrix_scan(self, sandbox):
        return

    def after_matrix_scan(self, sandbox):
        return

    def before_hid_send(self, sandbox):
        return

    def after_hid_send(self, sandbox):
        return

    def on_powersave_enable(self, sandbox):
        return

    def on_powersave_disable(self, sandbox):
        return
