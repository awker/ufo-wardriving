import sys
import fileinput
import sys, os.path

def calc(mac_addr):
    localdir = repr(os.path.dirname(os.path.realpath(sys.argv[0])))

    localdir = localdir.replace("\\\\","/")
    localdir = localdir.replace("\'","")


    dbfile = open(localdir+"/config/Tele2.txt","r")
    wmac = mac_addr[:8]
    mac6 = mac_addr[9:17]
    
    try:
        for riga in dbfile.readlines():
            da = riga[9:17]
            a = riga[18:26]
            if((riga[:8] == wmac) and (da < mac6 < a)):    
                sn1 = riga[27:32]
                base = riga[33:39]
                inc = riga[40]
                esit = bool(1)
                break
            else:
                esit = bool(0)
    except IOError:
        filerr = 0
    if(not(esit)):    
        macerr = 0
        return macerr
    else:
        mac6 = mac6.replace(':','') 
        mac6 = int(mac6,16)
        base = int(base,16)
        inc = int(inc)
        ris = mac6-base
        ris = ris/inc
        ris = str(ris)
        wpa = sn1+'Y'+ris
        return wpa

    
