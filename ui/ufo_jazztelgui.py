#!/usr/bin/python
'''
//=============================================================================
//
//	File : jazztelgui.py
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

from core import ufo_jazzteldecode

from core.ufo_picsfinder import getQIcon

class jazztelGuiWidget(QWidget):
	@staticmethod
	def findKey(self):
		mac_jazztel = str(self.macLineEdit.text())
		ssid_jazztel = str(self.ssidLineEdit.text())
		mac_jazztel = mac_jazztel.replace(" ","")
		ssid_jazztel = ssid_jazztel.replace(" ","")
		stdouterr_jazztel = ufo_jazzteldecode.calc(ssid_jazztel, mac_jazztel)
		if stdouterr_jazztel:
			self.outputTextEdit.setText(stdouterr_jazztel)
		else:
			self.outputTextEdit.setText(self.tr("No key found."))

	def __init__(self, parent = None):
		super(jazztelGuiWidget, self).__init__(parent)

		hBoxLayoutSsid = QHBoxLayout()
		hBoxLayoutSsid.setSpacing(5)
		hBoxLayoutMac = QHBoxLayout()
		hBoxLayoutMac.setSpacing(5)

		vBoxLayout = QVBoxLayout()
		vBoxLayout.setSpacing(5)

		ssidLabel = QLabel("SID:",self)
		self.ssidLineEdit= QLineEdit(self)
#		Sembra servano gli ultimi 4 caratteri dell'essid JAZZTEL_XXXX
		self.ssidLineEdit.setToolTip("SSID "+self.tr("Compatible")+" :\nJazztel*")
		self.ssidLineEdit.setMaxLength(4)
		self.ssidLineEdit.setInputMask("HHHH;-")

		macLabel = QLabel("MAC:",self)
		self.macLineEdit= QLineEdit(self)
		self.macLineEdit.setInputMask("HH:HH:HH:HH:HH:HH;_")

		self.outputTextEdit = QTextEdit(self)
		self.outputTextEdit.setReadOnly(True)

		self.calcPushButton = QPushButton(self.tr("Find"),self)
		self.calcPushButton.setIcon(getQIcon("key.png"))
		self.calcPushButton.setEnabled(0)

		hBoxLayoutSsid.addWidget(ssidLabel)
		hBoxLayoutSsid.addWidget(self.ssidLineEdit)
		hBoxLayoutMac.addWidget(macLabel)
		hBoxLayoutMac.addWidget(self.macLineEdit)

		hBoxLayoutSsid.addWidget(self.calcPushButton)

		vBoxLayout.addLayout(hBoxLayoutSsid)
		vBoxLayout.addLayout(hBoxLayoutMac)
		vBoxLayout.addWidget(self.outputTextEdit)


		self.setLayout(vBoxLayout)

		def slotFindKey():
				self.findKey(self)

		def enableBtn():
			if self.macLineEdit.text().length()==17 and self.ssidLineEdit.text().length()==4:
				self.calcPushButton.setEnabled(1)
			else:
				self.calcPushButton.setEnabled(0)

		self.ssidLineEdit.textChanged.connect(enableBtn)
		self.macLineEdit.textChanged.connect(enableBtn)
		self.calcPushButton.clicked.connect(slotFindKey)
