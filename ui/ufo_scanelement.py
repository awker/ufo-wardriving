#!/usr/bin/python
'''
//=============================================================================
//
//	File : scanelement.py
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

from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys, os.path,platform

from core.ufo_picsfinder import getQIcon

class scannViewElement(QListWidgetItem):
	def __init__(self,parent = None):
		QListWidgetItem.__init__(self)
#		super(scannViewElement, self).__init__(parent) // Non funziona come super
		self.setIcon(getQIcon("wifi25.png"))
		self.essidString =" - "
		self.macString=" - "
		self.signalString=" - "
		self.chanString=""
		self.freqString=" - "
		self.encrString=" - "
		self.encrString2=" - "
		self.dBmValue=25

	def setdBmValue(self, dBm):
		if (platform.system() != 'Windows'):
			self.dBmValue=self.dBmToPercentage(dBm)
			i_dBm = self.dBmValue
		else:
			self.dBmValue = dBm
			i_dBm = dBm
		if  i_dBm >=0 and i_dBm <26: 	self.setIcon(getQIcon("wifi25.png"))
		if  i_dBm >25 and i_dBm <51:	self.setIcon(getQIcon("wifi50.png"))
		if  i_dBm >50 and i_dBm <76:	self.setIcon(getQIcon("wifi75.png"))
		if  i_dBm >75 and i_dBm <=100:	self.setIcon(getQIcon("wifi100.png"))
		
	def dBmToPercentage(self,dbm):
			# In linea di massima: non c'e' una vera corrispondenza tra dBm e percentuale
			dbm =int(dbm)
			if dbm > -55:				return 100
			if dbm < -55 and dbm > -72:	return 75
			if dbm < -72 and dbm > -84:	return 50
			if dbm < -84:				return 25


	def setSsid(self,ssid):
		self.setText(ssid)

	def setMac(self,mac):
		self.macString = mac

	def setSignal(self,signal):
		self.signalString = signal

	def setFrequency(self,freq):
		self.freqString = freq

	def setChannel(self,chan):
		self.chanString = chan

	def setEncription(self,encr):
		self.encrString = encr

	def setEncription2(self,encr):
		self.encrString2 = encr

	def setInfo(self):
		if self.macString != "":
			self.setToolTip("Address: "+self.macString+"\n"+"Quality: "+self.signalString+"\n"+"Frequency: "+self.freqString+"\n"+"Channel: "+self.chanString+"\n"+"IE Encription: "+self.encrString+"\n"+"IEEE Encription: "+self.encrString2)
	def setWinInfo(self):
		if self.macString != "":
			self.setToolTip("Address: "+self.macString+"\n"+"Quality: "+str(self.signalString)+"\n"+"Frequency: "+self.freqString+"\n"+"Channel: "+self.chanString+"\n"+"Encription: "+self.encrString+"/"+self.encrString2)

	def getSsid(self):
		return self.essidString

	def getMac(self):
		return self.macString

	def getSignal(self):
		return self.signalString

	def getFrequency(self):
		return self.freqString

	def getChannel(self):
		return self.chanString

	def getEncription(self):
		return self.encrString

	def getEncription2(self):
		return self.encrString2
