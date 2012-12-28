from string import hexdigits

def calc(mac):
    err_mac = "MAC Errato"
    err_hex = "MAC non esadecimale"
    for c in ":-._":
        mac = mac.replace(c, "")
    if len(mac) != 12:
        return err_mac
        exit()
    try:
        mac.decode("hex")
    except TypeError:
        return err_hex
    newkey = []
    key = []
    hash = "XrqaHNpdSYw86215"
    indici = [11, 0, 10, 1, 9, 2, 8, 3, 7, 4, 6, 5, 1, 6, 8, 9, 11, 2, 4, 10]
    for i in indici:
        key.append(mac[i])
    for c in key:
        if c in hexdigits:
            index = int(c, 16)
        else:
            return 1
        newkey.append(hash[index])
    chiave = []
    for chiavi in newkey:
        chiave.append(chiavi)
    chiave = "".join(chiave)
    return chiave

