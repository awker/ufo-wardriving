#!/usr/bin/python
'''
//=============================================================================
//
//	File : huaweigui.py
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

from core import ufo_huaweidecode
from core.ufo_picsfinder import getQIcon

class huaweiGuiWidget(QWidget):
	@staticmethod
	def findKey(self):
		mac_huawei = str(self.macLineEdit.text())
		mac_huawei = mac_huawei.replace(" ","")
		stdouterr_huawei = ufo_huaweidecode.calc(mac_huawei)
		if stdouterr_huawei:
			self.outputTextEdit.setText(stdouterr_huawei)
		else:
			self.outputTextEdit.setText(self.tr("No key found."))

	def __init__(self, parent = None):
		super(huaweiGuiWidget, self).__init__(parent)

		hBoxLayout = QHBoxLayout()
		hBoxLayout.setSpacing(5)

		vBoxLayout = QVBoxLayout()
		vBoxLayout.setSpacing(5)

		macLabel = QLabel("MAC:",self)
		self.macLineEdit= QLineEdit(self)
		self.macLineEdit.setToolTip("SSID "+self.tr("Compatible")+": \nHuawei-*")
		self.macLineEdit.setInputMask("HH:HH:HH:HH:HH:HH;_")

		self.outputTextEdit = QTextEdit(self)
		self.outputTextEdit.setReadOnly(True)

		self.calcPushButton = QPushButton(self.tr("Find"),self)
		self.calcPushButton.setIcon(getQIcon("key.png"))
		self.calcPushButton.setEnabled(0)

		hBoxLayout.addWidget(macLabel)
		hBoxLayout.addWidget(self.macLineEdit)
		hBoxLayout.addWidget(self.calcPushButton)
		vBoxLayout.addLayout(hBoxLayout)
		vBoxLayout.addWidget(self.outputTextEdit)

		self.setLayout(vBoxLayout)

		def slotFindKey():
				self.findKey(self)

		def enableBtn():
			if self.macLineEdit.text().length()==17:
				self.calcPushButton.setEnabled(1)
			else:
				self.calcPushButton.setEnabled(0)

		self.macLineEdit.textChanged.connect(enableBtn)
		self.calcPushButton.clicked.connect(slotFindKey)
