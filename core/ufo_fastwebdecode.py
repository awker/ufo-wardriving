#!/usr/bin/env python



from binascii import unhexlify 
from hashlib  import md5
import sys


def calc(ssid):
    len_err = "L'SSID deve essere di 12 caratteri"
    hex_err = "L'SSID non e' esadecimale"
    if len(ssid) != 12:
        return len_err
    try:
        ssid.decode("hex")
    except TypeError:
        return hex_err
    alfa   = unhexlify(ssid)
    beta   = unhexlify('223311340281FA22114168111201052271421066')
    digest = int(md5(alfa+beta).hexdigest(), 16)
    wpa    = ''
    for i in range(123,0,-5):
        chunk = digest >> i & 0b11111
        if chunk > 9: 
            chunk += 87
        wpa += '%02x' % chunk
    key = wpa[0:10]
    return key


