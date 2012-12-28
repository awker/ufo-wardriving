#!/usr/bin/python
'''
//=============================================================================
//
//	File : Ufo.py
//	Creation date : Wed Dec 05 14:30:48 CEST 2012
//	Working on this file:	^4st3r1X^ (Cristian Steri)
//				Grifisx (Antonino G. Imbesi)
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

import os, time
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys, os.path
import webbrowser
import platform
import subprocess
from core.ufo_picsfinder import getQIcon

from ui.ufo_fastwebgui import fastGuiWidget
from ui.ufo_speedgui import speedGuiWidget
from ui.ufo_infogui import infostradaGuiWidget
from ui.ufo_teletugui import teletuGuiWidget
from ui.ufo_alicegui import aliceGuiWidget
from ui.ufo_dlinkgui import dlinkGuiWidget
from ui.ufo_huaweigui import huaweiGuiWidget
from ui.ufo_jazztelgui import jazztelGuiWidget
from ui.ufo_yacomgui import yacomGuiWidget
from ui.ufo_scannergui import scannerGuiWidget




def main(args):
	app=QApplication(args)
	translator= getTranslator()
	app.installTranslator(translator)
	form = MainWindow()
	activateSplashScreen().finish(form)
	form.show()
	app.exec_()

def getTranslator():
	translator = QTranslator()
	locale = QLocale.system().name()
	if translator.load(QString.fromUtf8(repr(os.path.dirname(\
			os.path.realpath(sys.argv[0]))).replace("\\\\","/")\
			.replace("\'","")+"/locale/UFO_"+locale+".qm")) :
		return translator

def activateSplashScreen():
	splash_pix = QPixmap(QString.fromUtf8(repr(os.path.dirname(\
			os.path.realpath(sys.argv[0]))).replace("\\\\","/")\
			.replace("\'","")+"/pics/splash.png"))
	splash = QSplashScreen( splash_pix)
	splash.setMask(splash_pix.mask())
	splash.show()
	time.sleep(2)
	return splash

class MainWindow(QMainWindow):
	def __init__(self, parent=None):
		QMainWindow.__init__(self)

		self.setWindowTitle("Ufo Wardriving")
		self.setWindowIcon(getQIcon("ufo.png"))
		self.statusBar().showMessage("I want to belive")
		self.mainWidget = QWidget(self)

		exitAction = QAction(getQIcon("exit.png"), '&Exit', self)
		exitAction.setShortcut('Ctrl+Q')
		exitAction.setStatusTip(self.tr("Exit application"))
		exitAction.triggered.connect(qApp.quit)
		def donazione():
			webbrowser.open("https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=JBQXLC8J5SWTA")

		def homepage():
			webbrowser.open("http://www.thc-scripting.it/ufowardriving/")

		def showScanner():
			if scanWidget.isVisible() == 1:
				scanWidget.setVisible(0)
				scanWidget.timer.stop()
			else:
				if (platform.system() == 'Windows'):
					cmd_test = "netsh wlan show networks mode=bssid"
					try:
						out = subprocess.check_output(cmd_test, shell=True)
						scanWidget.setVisible(1)
						scanWidget.timer.start()
					except subprocess.CalledProcessError:
						msgBox = QMessageBox()
						msgBox.setWindowTitle(self.tr("Windows Vista and later!"))
						msgBox.setText(self.tr("Sorry, This feature is only for Windows Vista and later."))
						msgBox.setIcon(QMessageBox.Warning)
						msgBox.setDefaultButton(QMessageBox.Ok)
						ret = msgBox.exec_()
						return
				else:
					scanWidget.setVisible(1)
					scanWidget.timer.start()

		homeAction = QAction(getQIcon("home.png"), self.tr("&Project home page"), self)
		homeAction.setShortcut('Ctrl+H')
		homeAction.setStatusTip(self.tr("Project home page"))
		homeAction.triggered.connect(homepage)

		donAction = QAction(getQIcon("donation.png"), self.tr("Make a donation"), self)
		donAction.setShortcut('Ctrl+D')
		donAction.setStatusTip(self.tr("Donation"))
		donAction.triggered.connect(donazione)

		scanAction = QAction(getQIcon("wifi.png"), '&Scanner', self)
		scanAction.setShortcut('Ctrl+D')
		scanAction.setStatusTip(self.tr("Show the wifi scanner\nWarning!\nOnly for linux!"))
		scanAction.triggered.connect(showScanner)

		menubar = self.menuBar()
		fileMenu = menubar.addMenu(self.tr("&File"))
		fileMenu.addAction(exitAction)

		toolsMenu = menubar.addMenu(self.tr("&Tools"))
		toolsMenu.addAction(scanAction)

		infoMenu = menubar.addMenu(self.tr("&Info"))
		infoMenu.addAction(homeAction)
		infoMenu.addAction(donAction)

		hBox = QHBoxLayout(self.mainWidget)
		hBox.setSpacing(5)

		self.tabWidget = QTabWidget(self.mainWidget)
		hBox.addWidget(self.tabWidget)

		scanWidget= scannerGuiWidget(self)
		hBox.addWidget(scanWidget)
		scanWidget.setVisible(0)

		self.fastwebTab	= QWidget(self.tabWidget)
		self.speedTab	= QWidget(self.tabWidget)
		self.teletuTab	= QWidget(self.tabWidget)
		self.infostradaTab	= QWidget(self.tabWidget)
		self.aliceTab	= QWidget(self.tabWidget)
		self.dlinkTab	= QWidget(self.tabWidget)
		self.huaweiTab	= QWidget(self.tabWidget)
		self.jazztelTab	= QWidget(self.tabWidget)
		self.yacomTab	= QWidget(self.tabWidget)

		self.tabWidget.addTab(self.fastwebTab,getQIcon("fastweb.png"),"Fastweb")
		self.tabWidget.addTab(self.speedTab,getQIcon("speedtouch.png"),"Speedtouch")
		self.tabWidget.addTab(self.teletuTab,getQIcon("teletu.png"),"TeleTu")
		self.tabWidget.addTab(self.infostradaTab,getQIcon("infostrada.png"),"Infostrada")
		self.tabWidget.addTab(self.aliceTab,getQIcon("alice.png"),"Alice")
		self.tabWidget.addTab(self.dlinkTab,getQIcon("dlink.png"),"DLink")
		self.tabWidget.addTab(self.huaweiTab,getQIcon("huawei.png"),"Huawei")
		self.tabWidget.addTab(self.jazztelTab,getQIcon("jazztel.png"),"Jazztel")
		self.tabWidget.addTab(self.yacomTab,getQIcon("yacom.png"),"YaCom")

		vBoxlayoutFast		= QVBoxLayout()
		vBoxlayoutSpeed		= QVBoxLayout()
		vBoxlayoutInfostrada	= QVBoxLayout()
		vBoxlayoutTeletu	= QVBoxLayout()
		vBoxlayoutAlice		= QVBoxLayout()
		vBoxlayoutDlink		= QVBoxLayout()
		vBoxlayoutHuawei	= QVBoxLayout()
		vBoxlayoutJazztel	= QVBoxLayout()
		vBoxlayoutYacom		= QVBoxLayout()

		self.fastGuiWidget		= fastGuiWidget()
		self.speedGuiWidget		= speedGuiWidget()
		self.infostradaGuiWidget	= infostradaGuiWidget()
		self.teletuGuiWidget		= teletuGuiWidget()
		self.aliceGuiWidget		= aliceGuiWidget()
		self.dlinkGuiWidget		= dlinkGuiWidget()
		self.huaweiGuiWidget		= huaweiGuiWidget()
		self.jazztelGuiWidget		= jazztelGuiWidget()
		self.yacomGuiWidget		= yacomGuiWidget()

		vBoxlayoutFast.addWidget(self.fastGuiWidget)
		vBoxlayoutSpeed.addWidget(self.speedGuiWidget)
		vBoxlayoutInfostrada.addWidget(self.infostradaGuiWidget)
		vBoxlayoutTeletu.addWidget(self.teletuGuiWidget)
		vBoxlayoutAlice.addWidget(self.aliceGuiWidget)
		vBoxlayoutDlink.addWidget(self.dlinkGuiWidget)
		vBoxlayoutHuawei.addWidget(self.huaweiGuiWidget)
		vBoxlayoutJazztel.addWidget(self.jazztelGuiWidget)
		vBoxlayoutYacom.addWidget(self.yacomGuiWidget)

		self.fastwebTab.setLayout(vBoxlayoutFast)
		self.speedTab.setLayout(vBoxlayoutSpeed)
		self.infostradaTab.setLayout(vBoxlayoutInfostrada)
		self.teletuTab.setLayout(vBoxlayoutTeletu)
		self.aliceTab.setLayout(vBoxlayoutAlice)
		self.dlinkTab.setLayout(vBoxlayoutDlink)
		self.huaweiTab.setLayout(vBoxlayoutHuawei)
		self.jazztelTab.setLayout(vBoxlayoutJazztel)
		self.yacomTab.setLayout(vBoxlayoutYacom)

		self.mainWidget.setLayout(hBox)
		self.setCentralWidget(self.mainWidget)



if __name__=="__main__":
    main(sys.argv)
