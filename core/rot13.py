# Created by LimerBoy

from string import ascii_uppercase as upper
from string import ascii_lowercase as lower

def encode(s, n=13):
    """
    Encode string s with ROT-n, i.e., by shifting all letters n positions.
    When n is not supplied, ROT-13 encoding is assumed.
    """
    upper_start = ord(upper[0])
    lower_start = ord(lower[0])
    out = ''
    for letter in s:
        if letter in upper:
            out += chr(upper_start + (ord(letter) - upper_start + n) % 26)
        elif letter in lower:
            out += chr(lower_start + (ord(letter) - lower_start + n) % 26)
        else:
            out += letter
    return(out)

def decode(s, n=13):
    """
    Decode a string s encoded with ROT-n-encoding
    When n is not supplied, ROT-13 is assumed.
    """
    try:
        return(encode(s, -n))
    except RecursionError:
        print("Please enter only english characters")
        raise SystemExit
