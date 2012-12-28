import sys
import hashlib
from optparse import OptionParser 
import os.path


localdir = repr(os.path.dirname(os.path.realpath(sys.argv[0])))

localdir = localdir.replace("\\\\","/")
localdir = localdir.replace("\'","")



def calc(ssid, mac):
    arg = "k"
    magic = open(localdir+"/config/agpf_config.txt","r")
    pwd = ''
    passwords = []
    if mac == 0:
        arg = 0
    elif len(mac) == 17:
        mac = mac.replace(":","")
        arg = 1

    ssid = int(ssid)
    ssid_0 = "%x" % (ssid)
    ssid_1 = int("1%d" % ssid)
    ssid_1 = "%x" % ssid_1
    ssid_2 = int("2%d" % ssid)
    ssid_2 = "%x" % ssid_2
    ssid_0_str = str(ssid_0)
    ssid_1_str = str(ssid_1)
    ssid_2_str = str(ssid_2)
    ssid_str = str(ssid)



    part = ssid_str
    part = part[0:3]


    alis = "64C6DDE3E579B6D986968D3445D23B15CAAF128402AC560005CE2075913FDCE8"
    conv_table = "0123456789abcdefghijklmnopqrstuvwxyz0123456789abcdefghijklmnopqrstuvwxyz0123456789abcdefghijklmnopqrstuvwxyz0123456789abcdefghijklmnopqrstuvwxyz0123456789abcdefghijklmnopqrstuvwxyz0123456789abcdefghijklmnopqrstuvwxyz0123456789abcdefghijklmnopqrstuvwxyz0123"
    charset = list(conv_table)
    alis = alis.decode('hex')




    for lines in magic.readlines():
        lines = lines.split(",") 
        if part in lines[0]:
            if arg == 1:
                if len(mac) == 12:
                    mac = str(mac)
                    mac_n = mac
                    mac = mac.decode('hex')
                    pwd = ''
                    k = lines[2]
                    q = lines[3]
                    sn1 = lines[1]
                    sn2 = (int(ssid) -int(q)) / int(k)

                    if len(str(sn2)) == 4:
                        sn_3 = "%sX000%d" % (sn1,sn2)
                        hash3 = hashlib.sha256()
                        hash3.update(alis)
                        hash3.update(sn_3)
                        hash3.update(mac)
                        c3 = hash3.hexdigest()
                        chdec3 = c3[:48]
                        b3 = [chdec3[x:x+2] for x in xrange(0,len(chdec3),2)]
                        for bytes3 in b3:
                            inc = int(bytes3,16)
                            pwd = pwd+charset[inc]
                        passwords.append(pwd)
                        pwd = ''

                    if len(str(sn2)) == 5:
                        sn_2 = "%sX00%d" % (sn1,sn2)
                        hash2 = hashlib.sha256()
                        hash2.update(alis)
                        hash2.update(sn_2)
                        hash2.update(mac)
                        c2 = hash2.hexdigest()
                        chdec2 = c2[:48]
                        b2 = [chdec2[x:x+2] for x in xrange(0,len(chdec2),2)]
                        for bytes2 in b2:
                            inc = int(bytes2,16)
                            pwd = pwd+charset[inc]
                        passwords.append(pwd)
                        pwd = ''

                    if len(str(sn2)) == 6:
                        sn_1 = "%sX0%d" % (sn1,sn2)
                        hash1 = hashlib.sha256()
                        hash1.update(alis)
                        hash1.update(sn_1)
                        hash1.update(mac)
                        c1 = hash1.hexdigest()
                        chdec1 = c1[:48]
                        b1 = [chdec1[x:x+2] for x in xrange(0,len(chdec1),2)]
                        for bytes1 in b1:
                            inc = int(bytes1,16)
                            pwd = pwd+charset[inc]
                        passwords.append(pwd)
                        pwd = ''

                    if len(str(sn2)) == 7:
                        sn = "%sX%d" % (sn1,sn2)
                        hash = hashlib.sha256()
                        hash.update(alis)
                        hash.update(sn)
                        hash.update(mac)
                        c = hash.hexdigest()
                        chdec = c[:48]
                        b = [chdec[x:x+2] for x in xrange(0,len(chdec),2)]
                        for bytes in b:
                            inc = int(bytes,16)
                            pwd = pwd+charset[inc]
                        passwords.append(pwd)
                        pwd = ''


            else:
                mac = lines[4]
                mac = mac.replace("\n","")
                sn1 = lines[1]
                k = lines[2]
                q = lines[3]


                if mac[-1]: 
                    pwd = ''
                    completo = mac+ssid_0_str[1:]
                    completo = str(completo.upper())
                    completo = completo.decode('hex')
                    sn2 = (int(ssid) -int(q)) / int(k)
                    if len(str(sn2)) == 4:
                        sn_3 = "%sX000%d" % (sn1,sn2)
                        hash3 = hashlib.sha256()
                        hash3.update(alis)
                        hash3.update(sn_3)
                        hash3.update(completo)
                        c3 = hash3.hexdigest()
                        chdec3 = c3[:48]
                        b3 = [chdec3[x:x+2] for x in xrange(0,len(chdec3),2)]
                        for bytes3 in b3:
                            inc = int(bytes3,16)
                            pwd = pwd+charset[inc]
                        passwords.append(pwd)
                        pwd = ''

                    if len(str(sn2)) == 5:
                        sn_2 = "%sX00%d" % (sn1,sn2)
                        hash2 = hashlib.sha256()
                        hash2.update(alis)
                        hash2.update(sn_2)
                        hash2.update(completo)
                        c2 = hash2.hexdigest()
                        chdec2 = c2[:48]
                        b2 = [chdec2[x:x+2] for x in xrange(0,len(chdec2),2)]
                        for bytes2 in b2:
                            inc = int(bytes2,16)
                            pwd = pwd+charset[inc]
                        passwords.append(pwd)
                        pwd = ''
  
                    if len(str(sn2)) == 6:
                        sn_1 = "%sX0%d" % (sn1,sn2)
                        hash1 = hashlib.sha256()
                        hash1.update(alis)
                        hash1.update(sn_1)
                        hash1.update(completo)
                        c1 = hash1.hexdigest()
                        chdec1 = c1[:48]
                        b1 = [chdec1[x:x+2] for x in xrange(0,len(chdec1),2)]
                        for bytes1 in b1:
                            inc = int(bytes1,16)
                            pwd = pwd+charset[inc]
                        passwords.append(pwd)
                        pwd = ''

                    if len(str(sn2)) == 7:
                        sn = "%sX%d" % (sn1,sn2)
                        hash = hashlib.sha256()
                        hash.update(alis)
                        hash.update(sn)
                        hash.update(completo)
                        c = hash.hexdigest()
                        chdec = c[:48]
                        b = [chdec[x:x+2] for x in xrange(0,len(chdec),2)]
                        for bytes in b:
                            inc = int(bytes,16)
                            pwd = pwd+charset[inc]
                        passwords.append(pwd)
                        pwd = ''
     

    return passwords

   

