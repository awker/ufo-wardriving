#!/usr/bin/python
'''
//=============================================================================
//
//	File : scannerguy.py
//	Creation date : Wed Dec 05 14:30:48 CEST 2012
//	Working on this file:	^4st3r1X^ (Cristian Steri)
//							Grifisx (Antonino G. Imbesi)
// 	This file is part of the Ufo Wardriving distribution
//
//	Websites: http://thc-scripting.it
//
// 	This program is FREE software. You can redistribute it and/or
// 	modify it under the terms of the GNU General Public License
// 	as published by the Free Software Foundation; either version 2
// 	of the License, or (at your opinion) any later version.
//
//	This program is distributed in the HOPE that it will be USEFUL,
// 	but WITHOUT ANY WARRANTY; without even the implied warranty of
// 	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
// 	See the GNU General Public License for more details.
//
// 	You should have received a copy of the GNU General Public License
// 	along with this program. If not, write to the Free Software Foundation,
// 	Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
//
//=============================================================================
'''

import os
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys, os.path
import subprocess
import re
import platform

from core.ufo_picsfinder import getQIcon

from ui import ufo_scanelement

class scannerGuiWidget(QWidget):
	def __init__(self, parent=None):
		super(scannerGuiWidget, self).__init__(parent)
		self.timer = QTimer(self)
		self.timer.setInterval(6000)
		hBoxLayout = QHBoxLayout()
		hBoxLayout.setSpacing(5)

		vBoxLayout = QVBoxLayout()
		vBoxLayout.setSpacing(5)

		scannerLabel = QLabel("Wifi Scanner",self)

		scannerPushButton = QPushButton(self.tr("Search"),self)
		scannerPushButton.setIcon(getQIcon("wifi.png"))
		scannerPushButton.setToolTip(self.tr("Warning! You must be root!"))

		outputListWI = QListWidget(self)

		hBoxLayout.addWidget(scannerLabel)
		hBoxLayout.addWidget(scannerPushButton)
		vBoxLayout.addLayout(hBoxLayout)
		vBoxLayout.addWidget(outputListWI)

		self.setLayout(vBoxLayout)

		def findItem():
			item = outputListWI.currentItem()
			if item.text().contains("Fastweb-1"):
				parent.fastGuiWidget.macLineEdit.setText(item.text().trimmed().right(12))
				parent.fastGuiWidget.findKey(parent.fastGuiWidget)
				parent.tabWidget.setCurrentIndex(0)

			if item.text().contains("Thomson") or item.text().contains("INFINITUM") or item.text().contains("Speedtouch") or item.text().contains("Discus-"):
				parent.speedGuiWidget.ssidLineEdit.setText(item.text().trimmed().right(6))
				parent.speedGuiWidget.findKey(parent.speedGuiWidget)
				parent.tabWidget.setCurrentIndex(1)
			if item.text().contains("BTHomeHub"):
				parent.speedGuiWidget.ssidLineEdit.setText(item.text().trimmed().right(4))
				parent.speedGuiWidget.findKey(parent.speedGuiWidget)
				parent.tabWidget.setCurrentIndex(1)

			if item.text().contains("TeleTu_") or item.text().contains("Tele2"):
				parent.teletuGuiWidget.lineEditTeletu.setText(item.getMac())
				parent.teletuGuiWidget.findKey(parent.teletuGuiWidget)
				parent.tabWidget.setCurrentIndex(2)

			if item.text().contains("Infostrada-"):
				parent.infostradaGuiWidget.macLineEdit.setText(item.getMac())
				parent.infostradaGuiWidget.findKey(parent.infostradaGuiWidget)
				parent.tabWidget.setCurrentIndex(3)

			if item.text().contains("Alice-"):
				parent.aliceGuiWidget.ssidLineEdit.setText(item.text().trimmed().right(8))
				parent.aliceGuiWidget.macLineEdit.setText(item.getMac())
				parent.aliceGuiWidget.findKey(parent.aliceGuiWidget)
				parent.tabWidget.setCurrentIndex(4)

			if item.text().contains("Dlink-"):
				parent.dlinkGuiWidget.inputMacLineEdit.setText(item.getMac())
				parent.dlinkGuiWidget.findKey(parent.dlinkGuiWidget)
				parent.tabWidget.setCurrentIndex(5)

			if item.text().contains("Huawei-"):
				parent.huaweiGuiWidget.macLineEdit.setText(item.getMac())
				parent.huaweiGuiWidget.findKey(parent.huaweiGuiWidget)
				parent.tabWidget.setCurrentIndex(6)

			if item.text().contains("Jazztel"):
				parent.jazztelGuiWidget.ssidLineEdit.setText(item.text().trimmed().right(4))
				parent.jazztelGuiWidget.macLineEdit.setText(item.getMac())
				parent.jazztelGuiWidget.findKey(parent.jazztelGuiWidget)
				parent.tabWidget.setCurrentIndex(7)

			if item.text().contains("Yacom"):
				parent.yacomGuiWidget.ssidInputLineEdit.setText(item.text().trimmed().right(6))
				parent.yacomGuiWidget.macInputLineEdit.setText(item.getMac())
				parent.yacomGuiWidget.findKey(parent.yacomGuiWidget)
				parent.tabWidget.setCurrentIndex(8)



		def wlan_scansione():
			if (platform.system() == 'Windows'):
				outputListWI.clear()
				cmd = "netsh wlan show networks mode=bssid"
				out = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
				out = out.stdout.read()
				output = QString(out)
				ssdlist = QStringList
				ssdlist= output.split(QRegExp("[^B]SSID"))
				cellsnumber = ssdlist.count()
				n_rete = 1
				netlist = {}
				def clear_output(netlist):
					netlist[mac] = [nomerete, mac, tiporete, autenticazione,
			 				crittografia, segnale, freq, chan]

	

						
						

				while n_rete != cellsnumber:
					infocellist = QStringList
					infocelllist =ssdlist[n_rete].split("\n")
					nomerete = str(infocelllist[0].section(":",1,-1))
					tiporete = str(infocelllist[1].section(":",1,-1))
					autenticazione = str(infocelllist[2].section(":",1,-1))
					crittografia = str(infocelllist[3].section(":",1,-1))
					mac = str(infocelllist[4].section(":",1,-1))
					segnale = str(infocelllist[5].section(":",1,-1))
					freq = str(infocelllist[6].section(":",1,-1))
					chan = str(infocelllist[7].section(":",1,-1))
        				clear_output(netlist)
					n_rete = n_rete+1
					output = ""
					tot = 1
				for macs in netlist:
					tot = tot+1
					item = ufo_scanelement.scannViewElement(outputListWI)
					net_essid = netlist[macs][0]
					net_essid = net_essid.replace(" ","")
					net_mac = netlist[macs][1]
					net_type = netlist[macs][2]
					net_auth = netlist[macs][3]
					net_cifr = netlist[macs][4]
					net_signal = netlist[macs][5]
					net_signal = net_signal.replace(":","") and net_signal.replace("%","")
					net_signal = int(net_signal)
					net_freq = netlist[macs][6]
					net_chan = netlist[macs][7]
					if net_essid:
						item.setSsid(net_essid)
					else:
						item.setSsid("-Hidden-")
					outputListWI.insertItem(n_rete,item)	
					item.setMac(net_mac)
					item.setdBmValue(net_signal)
					item.setSignal(net_signal)
					item.setFrequency(net_freq)
					item.setEncription(net_cifr)
					item.setEncription2(net_auth)
					item.setChannel(net_chan)
					item.setWinInfo()
					item = ""
					item = ufo_scanelement.scannViewElement(outputListWI)


			else:
				outputListWI.clear()
				idx=0
				scan_net = subprocess.Popen("iwconfig", stdout=subprocess.PIPE, stderr=subprocess.PIPE)
				schede_rete = scan_net.stdout.readlines()
				schede_rete = [x.split(None, 1)[0] for x in schede_rete if 'IEEE 802.11' in x]
				for schede in schede_rete:
					schede = schede[0:]
					reti = subprocess.Popen(["iwlist", schede, "scanning"], stdout=subprocess.PIPE)
					buf = reti.stdout.readlines()
					idx=idx+1
					item = ufo_scanelement.scannViewElement(outputListWI)

				for data in buf:
					if "ESSID:" in data :
						essid = re.search(r'\s+ESSID:"([^"]+)"', data).group(1)
						essid = "".join(essid)
						item.setSsid(essid)
						outputListWI.insertItem(idx,item)

					if "Address:" in data :
						mac = re.search(r'\s+Cell \d+ - Address: (\S+)', data).group(1)
						mac = "".join(mac)
						item.setMac(mac)

					if "Quality=" in data :
						signal = re.search(r'\s+Quality=(\d+/\d+)',data).group(1)
						item.setSignal(signal)

					if "Frequency:" in data :
						frequenza = re.search(r'\s+Frequency:(\S+)',data).group(1)
						item.setFrequency(frequenza)

					if "Signal" in data :
						signal = QString(data)
						second = signal.section("level=",1,-1).remove(" dBm")
						item.setdBmValue(second)
					if "IE:" in data:
							if "IEEE " in data:
								encr = QString(data)
								encr = encr.section("i/",1,-1).replace("\n","")
								if encr.contains("unknow"):	encr = "Unknow"
								item.setEncription(encr)
							else:
								encr2 = QString(data)
								encr2 = encr2.section("E: ",1,-1).replace("\n","")
								item.setEncription2(encr2)
					if "(Channel" in data :
						canale = re.search(r'\(Channel\s+(\d+)\)', data).group(1)
						canale = "%s" % (canale.replace(" ",""))
						item.setChannel(canale)

					if "Extra" in data:
						item.setInfo()
						item = ""
						item = ufo_scanelement.scannViewElement(outputListWI)
		self.wlan_scansioneMtd = wlan_scansione()
		self.timer.timeout.connect(wlan_scansione)
		scannerPushButton.clicked.connect(wlan_scansione)
		outputListWI.itemDoubleClicked.connect(findItem)

