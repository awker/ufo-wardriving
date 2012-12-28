import sys

def calc(mac):
    if len(mac) == 17:
        mac = mac.replace(":","")
        password = "2"+mac
        return password
        
