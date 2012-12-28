#!/usr/bin/python
'''
//=============================================================================
//
//	File : dlinkgui.py
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

from core import ufo_dlinkdecode
from core.ufo_picsfinder import getQIcon

class dlinkGuiWidget(QWidget):
	@staticmethod
	def findKey(self):
		mac_dlink = str(self.inputMacLineEdit.text())
		mac_dlink = mac_dlink.replace(" ","")
		stdouterr_dlink = ufo_dlinkdecode.calc(mac_dlink)
		if stdouterr_dlink:
			self.outputTextEdit.setText(stdouterr_dlink)
		else:
			self.outputTextEdit.setText(self.tr("No key found."))

	def __init__(self, parent = None):
		super(dlinkGuiWidget, self).__init__(parent)

		hBoxLayout = QHBoxLayout()
		hBoxLayout.setSpacing(5)

		vBoxLayout = QVBoxLayout()
		vBoxLayout.setSpacing(5)

		macLabel = QLabel("MAC:",self)
		self.inputMacLineEdit= QLineEdit(self)
		self.inputMacLineEdit.setToolTip("SSID "+self.tr("Compatible")+" : \nDlink-*")
		self.inputMacLineEdit.setInputMask("HH:HH:HH:HH:HH:HH;_")

		self.outputTextEdit = QTextEdit(self)
		self.outputTextEdit.setReadOnly(True)

		self.calcPushButton = QPushButton(self.tr("Find"),self)
		self.calcPushButton.setIcon(getQIcon("key.png"))
		self.calcPushButton.setEnabled(0)

		hBoxLayout.addWidget(macLabel)
		hBoxLayout.addWidget(self.inputMacLineEdit)
		hBoxLayout.addWidget(self.calcPushButton)
		vBoxLayout.addLayout(hBoxLayout)
		vBoxLayout.addWidget(self.outputTextEdit)

		self.setLayout(vBoxLayout)

		def slotFindKey():
				self.findKey(self)

		def enableBtn():
			if self.inputMacLineEdit.text().length()==17:
				self.calcPushButton.setEnabled(1)
			else:
				self.calcPushButton.setEnabled(0)

		self.inputMacLineEdit.textChanged.connect(enableBtn)
		self.calcPushButton.clicked.connect(slotFindKey)
