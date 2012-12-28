#!/usr/bin/python
'''
//=============================================================================
//
//	File : teletugui.py
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

from core import ufo_teletudecode

class teletuGuiWidget(QWidget):
	@staticmethod
	def findKey(self):
		mac_teletu = str(self.lineEditTeletu.text())
		mac_teletu = mac_teletu.replace(" ","")
		stdouterr_teletu = ufo_teletudecode.calc(mac_teletu)
		if stdouterr_teletu == 0:
			self.outputTextEdit.setText(self.tr("No key found."))
		else:
			self.outputTextEdit.setText(stdouterr_teletu)

	def __init__(self, parent = None):
		super(teletuGuiWidget, self).__init__(parent)

		hBoxTeletu = QHBoxLayout()
		hBoxTeletu.setSpacing(5)

		vBoxTeletu = QVBoxLayout()
		vBoxTeletu.setSpacing(5)

		labelTeletu = QLabel("MAC:",self)
		self.lineEditTeletu= QLineEdit(self)
		self.lineEditTeletu.setToolTip("SSID "+self.tr("Compatible")+" : \nTeleTu_ \nTele2")
		self.lineEditTeletu.setInputMask("HH:HH:HH:HH:HH:HH;_")

		self.outputTextEdit = QTextEdit(self)
		self.outputTextEdit.setReadOnly(True)

		self.buttonCalc = QPushButton(self.tr("Find"),self)
		self.buttonCalc.setIcon(getQIcon("key.png"))
		self.buttonCalc.setEnabled(0)

		hBoxTeletu.addWidget(labelTeletu)
		hBoxTeletu.addWidget(self.lineEditTeletu)
		hBoxTeletu.addWidget(self.buttonCalc)
		vBoxTeletu.addLayout(hBoxTeletu)
		vBoxTeletu.addWidget(self.outputTextEdit)

		self.setLayout(vBoxTeletu)

		def slotFindKey():
				self.findKey(self)

		def enableBtn():
			if self.lineEditTeletu.text().length()==17:
				self.buttonCalc.setEnabled(1)
			else:
				self.buttonCalc.setEnabled(0)

		self.lineEditTeletu.textChanged.connect(enableBtn)
		self.buttonCalc.clicked.connect(slotFindKey)
