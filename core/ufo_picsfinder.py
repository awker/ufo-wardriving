from PyQt4.QtCore import * 
from PyQt4.QtGui import *
import sys, os.path

def getQIcon(name):
    return QIcon(QString.fromUtf8(repr(os.path.dirname(\
    os.path.realpath(sys.argv[0]))).replace("\\\\","/")\
    .replace("\'","")+"/pics/"+name))