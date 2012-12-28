#!/usr/bin/python
'''
//=============================================================================
//
//	File : alicegui.py
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

from core import ufo_alicedecode
from core.ufo_picsfinder import getQIcon

class aliceGuiWidget(QWidget):
# Grifisx: Il metodo lo definisco statico per potervi accedere dallo scanner wifi tramite un hack del codice
	@staticmethod
	def findKey(self):
		self.outputTextEdit.setText("")
		ssid_alice = str(self.ssidLineEdit.text())
		mac_alice = str(self.macLineEdit.text())
		if len(mac_alice) != 17:
			stdouterr_alice = ufo_alicedecode.calc(ssid_alice,0)
			self.outputTextEdit.append(self.tr("Try without MAC\n"))
			if stdouterr_alice:
				for passwords in stdouterr_alice:
					self.outputTextEdit.append(passwords)
			else:
				self.outputTextEdit.append(self.tr("No key found."))
		else:
			stdouterr_alice = ufo_alicedecode.calc(ssid_alice,mac_alice)
			if stdouterr_alice:
				for passwords in stdouterr_alice:
					self.outputTextEdit.append(passwords)
			else:
				self.outputTextEdit.setText(self.tr("No key found."))

	def __init__(self, parent = None):
		super(aliceGuiWidget, self).__init__(parent)

		hBoxLayoutSid = QHBoxLayout()
		hBoxLayoutSid.setSpacing(5)
		hBoxLayoutMac = QHBoxLayout()
		hBoxLayoutMac.setSpacing(5)

		vBoxLayout = QVBoxLayout()
		vBoxLayout.setSpacing(5)

		ssidLabel = QLabel("SID:",self)
		self.ssidLineEdit= QLineEdit(self)
		self.ssidLineEdit.setToolTip("SSID "+self.tr("Compatible")+" :\nAlice-*")
		self.ssidLineEdit.setMaxLength(8)
		self.ssidLineEdit.setInputMask("99999999;-")

		macLabel = QLabel("MAC:",self)
		self.macLineEdit= QLineEdit(self)
		self.macLineEdit.setToolTip(self.tr("Optional"))
		self.macLineEdit.setInputMask("HH:HH:HH:HH:HH:HH;_")

		self.outputTextEdit = QTextEdit(self)
		self.outputTextEdit.setReadOnly(True)

		self.calcPushButton = QPushButton(self.tr("Find"),self)
		self.calcPushButton.setIcon(getQIcon("key.png"))
		self.calcPushButton.setEnabled(0)

		hBoxLayoutSid.addWidget(ssidLabel)
		hBoxLayoutSid.addWidget(self.ssidLineEdit)
		hBoxLayoutMac.addWidget(macLabel)
		hBoxLayoutMac.addWidget(self.macLineEdit)

		hBoxLayoutSid.addWidget(self.calcPushButton)

		vBoxLayout.addLayout(hBoxLayoutSid)
		vBoxLayout.addLayout(hBoxLayoutMac)
		vBoxLayout.addWidget(self.outputTextEdit)

		self.setLayout(vBoxLayout)

# @Grifisx: 	questa e' una classe di passaggio, poiche' il connect non puo' essere fatto con un metodo
#			statico che riceve un self come argomento
		def slotFindKey():
				self.findKey(self)
		def enableBtn():
			if self.ssidLineEdit.text().length()==8:
				if self.macLineEdit.text().length()==17 or self.macLineEdit.text().length()==5:
					self.calcPushButton.setEnabled(1)
				else:
					self.calcPushButton.setEnabled(0)
			else:
				self.calcPushButton.setEnabled(0)

		self.ssidLineEdit.textChanged.connect(enableBtn)
		self.macLineEdit.textChanged.connect(enableBtn)
		self.calcPushButton.clicked.connect(slotFindKey)
