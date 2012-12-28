#!/usr/bin/python
'''
//=============================================================================
//
//	File : yacomgui.py
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

from core.ufo_picsfinder import getQIcon

from core import ufo_yacomdecode

class yacomGuiWidget(QWidget):
	@staticmethod
	def findKey(self):
		self.outputTextEdit.setText("")
		mac_yacom = str(self.macInputLineEdit.text())
		ssid_yacom = str(self.ssidInputLineEdit.text())
		mac_yacom = mac_yacom.replace(" ","")
		ssid_yacom = ssid_yacom.replace(" ","")
		stdouterr_yacom = ufo_yacomdecode.calc(ssid_yacom, mac_yacom)
		if stdouterr_yacom:
			for passwords in stdouterr_yacom:
				self.outputTextEdit.append(passwords)
		else:
			self.outputTextEdit.setText(self.tr("No key find"))

	def __init__(self, parent = None):
		super(yacomGuiWidget, self).__init__(parent)

		hBoxLayoutSsid = QHBoxLayout()
		hBoxLayoutSsid.setSpacing(5)
		hBoxLayoutMac = QHBoxLayout()
		hBoxLayoutMac.setSpacing(5)

		vBoxLayout = QVBoxLayout()
		vBoxLayout.setSpacing(5)

		ssidLabel = QLabel("SID:",self)
		self.ssidInputLineEdit= QLineEdit(self)
		self.ssidInputLineEdit.setToolTip("SSID "+self.tr("Compatible")+" :\nYacom-*")
		self.ssidInputLineEdit.setMaxLength(6)
		self.ssidInputLineEdit.setInputMask("999999;-")

		macLabel = QLabel("MAC:",self)
		self.macInputLineEdit= QLineEdit(self)
#		Sembra servano gli ultimi 6 caratteri dell'essid YaCom-xxxxxx
		self.macInputLineEdit.setInputMask("HH:HH:HH:HH:HH:HH;_")

		self.outputTextEdit = QTextEdit(self)
		self.outputTextEdit.setReadOnly(True)

		self.calcPushButton = QPushButton(self.tr("Find"),self)
		self.calcPushButton.setIcon(getQIcon("key.png"))
		self.calcPushButton.setEnabled(0)

		hBoxLayoutSsid.addWidget(ssidLabel)
		hBoxLayoutSsid.addWidget(self.ssidInputLineEdit)
		hBoxLayoutMac.addWidget(macLabel)
		hBoxLayoutMac.addWidget(self.macInputLineEdit)

		hBoxLayoutSsid.addWidget(self.calcPushButton)

		vBoxLayout.addLayout(hBoxLayoutSsid)
		vBoxLayout.addLayout(hBoxLayoutMac)
		vBoxLayout.addWidget(self.outputTextEdit)

		self.setLayout(vBoxLayout)

		def slotFindKey():
				self.findKey(self)

		def enableBtn():
			if self.macInputLineEdit.text().length()==17 and self.ssidInputLineEdit.text().length()==6:
				self.calcPushButton.setEnabled(1)
			else:
				self.calcPushButton.setEnabled(0)

		self.ssidInputLineEdit.textChanged.connect(enableBtn)
		self.macInputLineEdit.textChanged.connect(enableBtn)
		self.calcPushButton.clicked.connect(slotFindKey)
