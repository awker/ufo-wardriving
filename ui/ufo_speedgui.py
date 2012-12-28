#!/usr/bin/python
'''
//=============================================================================
//
//	File : speedgui.py
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

from core import ufo_speeddecode

class speedGuiWidget(QWidget):
	@staticmethod
	def findKey(self):
		self.outputTextEdit.setText("")
		ssid_speed = str(self.ssidLineEdit.text())
		ssid_speed = ssid_speed.replace("-","")
		stdouterr_speed = ufo_speeddecode.calc(ssid_speed)
		if stdouterr_speed:
			for passwords in stdouterr_speed:
				self.outputTextEdit.append(passwords)
		else:
			self.outputTextEdit.setText(self.tr("No key found."))

	def __init__(self, parent = None):
		super(speedGuiWidget, self).__init__(parent)

		hBoxLayout = QHBoxLayout()
		hBoxLayout.setSpacing(5)

		vBoxLayout = QVBoxLayout()
		vBoxLayout.setSpacing(5)

		ssidLabel = QLabel("SSID:",self)
		self.ssidLineEdit= QLineEdit(self)
		self.ssidLineEdit.setToolTip("SSID "+self.tr("Compatible")+" : \nSpeedtouch \nThomson, \nINFINITUM \nDiscus- \nDiscus-- \nBBox \nBTHomeHub \nOtenet \nSapo")
		self.ssidLineEdit.setInputMask("HHHHHH;-")
		self.ssidLineEdit.setMaxLength(6)

		self.outputTextEdit = QTextEdit(self)
		self.outputTextEdit.setReadOnly(True)

		self.calcPushButton = QPushButton(self.tr("Find"),self)
		self.calcPushButton.setIcon(getQIcon("key.png"))
		self.calcPushButton.setEnabled(0)

		hBoxLayout.addWidget(ssidLabel)
		hBoxLayout.addWidget(self.ssidLineEdit)
		hBoxLayout.addWidget(self.calcPushButton)
		vBoxLayout.addLayout(hBoxLayout)
		vBoxLayout.addWidget(self.outputTextEdit)

		self.setLayout(vBoxLayout)

		def slotFindKey():
				self.findKey(self)

		def enableBtn():
			if self.ssidLineEdit.text().length()==4 or self.ssidLineEdit.text().length()==6:
				self.calcPushButton.setEnabled(1)
			else:
				self.calcPushButton.setEnabled(0)

		self.ssidLineEdit.textChanged.connect(enableBtn)
		self.calcPushButton.clicked.connect(slotFindKey)
