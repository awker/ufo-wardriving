#! /usr/bin/env python
# WLANxxxyyy, YaCOMxxxyyy, WiFixxxyyy
from optparse import OptionParser 
import sys



def hd(s):
    return int(s, 16)

def dh(n):
    return "%X" % n


def yacom(E,M,S):
	K1=hd(S[6])+hd(S[7])+hd(M[10])+hd(M[11]) #S7+S8+M11+M12
	K2= hd(M[8])+hd(M[9])+hd(S[8])+hd(S[9])  #M9+M10+S9+S10 

	K1= dh(K1)[-1]
	K2= dh(K2)[-1]

	X1=dh(hd(K1)^hd(S[9]));
	X2=dh(hd(K1)^hd(S[8]));
	X3=dh(hd(K1)^hd(S[7]));

	Y1=dh(hd(K2)^hd(M[9]));
	Y2=dh(hd(K2)^hd(M[10]));
	Y3=dh(hd(K2)^hd(M[11]));

	Z1=dh(hd(M[10])^hd(S[9]));
	Z2=dh(hd(M[11])^hd(S[8]));
	Z3=dh(hd(K1)^hd(K2));

	W1=dh(hd(X1)^hd(Z2));
	W2=dh(hd(Y2)^hd(Y3));
	W3=dh(hd(Y1)^hd(X3));
	W4=dh(hd(Z3)^hd(X2));
	return W4+X1+Y1+Z1+W1+X2+Y2+Z2+W2+X3+Y3+Z3+W3

def calc(E,M):
    chiavi = []
    try:
        ssid = E.upper()
        if len(M) != 17:
            errmac = "MAC Errato"
        else:
            M = M.replace(":","")
            for i in range(0, 10):
                S7=i;
                S="xxxxxx"+str(S7)+E[3:]
                key = yacom(E,M,S)
                chiavi.append(key)
            return chiavi
    except TypeError:
        pass

        
