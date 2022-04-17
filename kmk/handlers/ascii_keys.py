'''Prints ASCII characters in Windows using LALT + 0123 Numpad sequences'''
from kmk.keys import KC, make_key
from kmk.handlers.sequences import KeySequenceMeta
from kmk.handlers.stock import passthrough

def ascii_sequence_press_handler(key, keyboard, KC, *args, **kwargs):
    oldkeys_pressed = keyboard.keys_pressed
    keyboard.keys_pressed = set()

    keyboard.process_key(KC.LALT, True)
    keyboard._send_hid()

    for ikey in key.meta.seq:
        if not getattr(ikey, 'no_press', None):
            keyboard.process_key(ikey, True)
            keyboard._send_hid()
        if not getattr(ikey, 'no_release', None):
            keyboard.process_key(ikey, False)
            keyboard._send_hid()

    keyboard.process_key(KC.LALT, False)
    keyboard._send_hid()
    
    keyboard.keys_pressed = oldkeys_pressed

    return keyboard


def simple_ascii_key_sequence(seq):
    return make_key(
        meta=KeySequenceMeta(seq),
        on_press=ascii_sequence_press_handler,
        on_release=passthrough,
    )

# https://stackoverflow.com/questions/32752750/how-to-find-the-numbers-in-the-thousands-hundreds-tens-and-ones-place-in-pyth
# Brian Tompsett Feb 2, 2020 at 15:26
def get_pos_nums(num):
    pos_nums = []
    while num != 0:
        pos_nums.append(num % 10)
        num = num // 10
    return pos_nums

def send_ascii(message):
    if len(message) == 1:
        ascii = ord(message[0])

        if ascii > 255:
            raise ValueError('send_ascii cannot send characters greater than U+00FF')

        ascii_arr = get_pos_nums(ascii)
        
        seq = []
        seq.append(KC.P0)
        seq.append(getattr(KC, "P" + str(ascii_arr[2])))
        seq.append(getattr(KC, "P" + str(ascii_arr[1])))
        seq.append(getattr(KC, "P" + str(ascii_arr[0])))
    else:
        raise ValueError('send_ascii accepts only a single character')
    return simple_ascii_key_sequence(seq)