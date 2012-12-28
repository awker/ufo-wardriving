#!/usr/bin/python
'''
//=============================================================================
//
//	File : infogui.py
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

from core import ufo_infostradadecode
from core.ufo_picsfinder import getQIcon

class infostradaGuiWidget(QWidget):
	@staticmethod
	def findKey(self):
		mac_infostrada = str(self.macLineEdit.text())
		mac_infostrada = mac_infostrada.replace(" ","")
		stdouterr_infostrada = ufo_infostradadecode.calc(mac_infostrada)
		if stdouterr_infostrada:
			self.outputTextEdit.setText(stdouterr_infostrada)
		else:
			self.outputTextEdit.setText(self.tr("No key found."))

	def __init__(self, parent = None):
		super(infostradaGuiWidget, self).__init__(parent)

		hboxLayout = QHBoxLayout()
		hboxLayout.setSpacing(5)

		vboxLayout = QVBoxLayout()
		vboxLayout.setSpacing(5)

		macLabel = QLabel("MAC:",self)
		self.macLineEdit= QLineEdit(self)
		self.macLineEdit.setToolTip("SSID "+self.tr("Compatible")+" : \nInfostradaWIFI-*")
		self.macLineEdit.setInputMask("HH:HH:HH:HH:HH:HH;_")

		self.outputTextEdit = QTextEdit(self)
		self.outputTextEdit.setReadOnly(True)

		self.calcPushButton = QPushButton(self.tr("Find"),self)
		self.calcPushButton.setIcon(getQIcon("key.png"))
		self.calcPushButton.setEnabled(0)

		hboxLayout.addWidget(macLabel)
		hboxLayout.addWidget(self.macLineEdit)
		hboxLayout.addWidget(self.calcPushButton)
		vboxLayout.addLayout(hboxLayout)
		vboxLayout.addWidget(self.outputTextEdit)


		self.setLayout(vboxLayout)

		def slotFindKey():
				self.findKey(self)

		def enableBtn():
			if self.macLineEdit.text().length()==17:
				self.calcPushButton.setEnabled(1)
			else:
				self.calcPushButton.setEnabled(0)

		self.macLineEdit.textChanged.connect(enableBtn)
		self.calcPushButton.clicked.connect(slotFindKey)
