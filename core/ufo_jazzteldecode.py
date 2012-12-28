#JAZZTEL_ , WLAN_ 
from optparse import OptionParser 
import hashlib
import sys

def calc(ssid, mac):
    try:
        if len(ssid) != 4:
            err_ssid = "SSID Errato, l'SSID deve essere di 4 caratteri" 
        else:
            ssid = ssid.upper()

    except TypeError:
        err = "Devi inserire i dati richiesti"
    mac2 = mac[:8]

    key = "bcgbghgg%s%s%s" % (mac2,ssid,mac)
    hash = hashlib.md5(key).hexdigest()
    pwd = hash[:20]
    return pwd

