import sys 
import os
import math
from Randevu_python import Ui_Randevu
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class dataPage(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.randevuForm = Ui_Randevu()
        self.randevuForm.setupUi(self)
        
        
        ################### FİELDS ######################
        self.bakimMenu = self.randevuForm.bakimMenu # BAKİM FRAME
        self.bakimBtn = self.randevuForm.bakmBtn # BAKİM BUTONU
        self.kamyonetBtn = self.randevuForm.kamyonetBtn # KAMYONET BUTONU
        self.otomobilBtn = self.randevuForm.otomobilBtn # OTOMOBİL BUTONU
        self.secimframe = self.randevuForm.secimFrame # SECİM FRAME
        self.bottomMenu = self.randevuForm.secimBottom # BOTTOM MENU
        self.labelTutar = self.randevuForm.labelTutar # TUTAR MENU
        self.tamirBtn = self.randevuForm.tamirBtn # TAMİR BUTONU
        self.muayeneBtn = self.randevuForm.muayeneBtn # MUAYENE BUTONU
        self.camFilmiBtn = self.randevuForm.camFilmBtn # CAM FİLMİ BUTONU
        self.cikisBtn = self.randevuForm.cikisBtn # CIKIS BUTONU
        self.gazCheck = self.randevuForm.gazCheck # GAZ CHECKBOX
        self.lastikCheck = self.randevuForm.lastikCheck # LASTİK CHECKBOX
        self.rotBalansCheck = self.randevuForm.rotCheck # ROTBALANS CHECKBOX
        self.yagDegisimCheck = self.randevuForm.yagCheck # YAG DEGİSİM CHECKBOX
        self.takvim = self.randevuForm.calenderFrame # TAKVİM
        self.onayla = self.randevuForm.onayBtn # ONAYLA
        self.total = 200 
        self.kapora = 200
        self.gazAyari = 350
        self.lastikKontrol = 200
        self.rotBalans = 500
        self.yagDegisim = 400
        self.muayeneKontrol = 500
        self.camFilmi = 600
        self.tamir = 0
        ##################### STARTER ###################
        self.bakimMenu.hide()
        self.bakimMenu.height = 0
        self.randevuForm.secimFrame.hide()
        self.labelTutar.setText("Tutar :")
        #################################################
        
        ################ BUTTON EVENTS ##################
        self.bakimBtn.clicked.connect(self.toggleBakimMenu)
        self.kamyonetBtn.clicked.connect(self.menuGoster1)
        self.otomobilBtn.clicked.connect(self.menuGoster2)
        self.gazCheck.stateChanged.connect(self.gazAyariFiyat)
        self.lastikCheck.stateChanged.connect(self.lastikKontrolFiyat)
        self.rotBalansCheck.stateChanged.connect(self.rotBalansFiyat)
        self.yagDegisimCheck.stateChanged.connect(self.yagDegisimFiyat)
        self.muayeneBtn.clicked.connect(self.muayeneFiyat)
        self.camFilmiBtn.clicked.connect(self.camfilmFiyat)
        self.onayla.clicked.connect(self.randevuOlustur)
        #################################################

        ################# RESPONSİVE AND RESİZE ############
        screen = QDesktopWidget().screenGeometry()
        width, height = screen.width(), screen.height()
        self.resize(width * 0.85, height * 0.85)
        self.center()
        
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        ####################################################

    def toggleBakimMenu(self):
        if self.bakimMenu.isVisible():
            self.bakimMenu.hide()
        else:
            self.bakimMenu.show()

    def menuGoster1(self):
        self.kamyonetBtn.setStyleSheet("background-color: red")
        if self.otomobilBtn.styleSheet() == "background-color: red":
            self.otomobilBtn.setStyleSheet("")
        self.secimframe.show()
        
    def menuGoster2(self):
        self.otomobilBtn.setStyleSheet("background-color: red")
        if self.kamyonetBtn.styleSheet() == "background-color: red":
            self.kamyonetBtn.setStyleSheet("")
        self.secimframe.show()
    
    def gazAyariFiyat(self, state):
        if state == 2:
            self.total += self.gazAyari
            self.labelTutar.setText("Tutar : " + str(self.total) + " TL")
            print(self.total)
        elif state == 0:
            self.total -= self.gazAyari
            self.labelTutar.setText("Tutar : " + str(self.total) + " TL")
        print(self.total)
        
    def lastikKontrolFiyat(self, state):
        if state == 2:
            self.total += self.lastikKontrol
            self.labelTutar.setText("Tutar : " + str(self.total) + " TL")
        elif state == 0:
            self.total -= self.lastikKontrol
            self.labelTutar.setText("Tutar : " + str(self.total) + " TL")
            
    def rotBalansFiyat(self, state):
        if state == 2:
            self.total += self.rotBalans
            self.labelTutar.setText("Tutar : " + str(self.total) + " TL")
        elif state == 0:
            self.total -= self.rotBalans
            self.labelTutar.setText("Tutar : " + str(self.total) + " TL")
            
    def yagDegisimFiyat(self, state):
        if state == 2:
            self.total += self.yagDegisim
            self.labelTutar.setText("Tutar : " + str(self.total) + " TL")
        elif state == 0:
            self.total -= self.yagDegisim
            self.labelTutar.setText("Tutar : " + str(self.total) + " TL")
        
    
    def muayeneFiyat(self):
        # self.kamyonetBtn.setStyleSheet("background-color: red")
        # if self.otomobilBtn.styleSheet() == "background-color: red":
        #     self.otomobilBtn.setStyleSheet("")
        # self.secimframe.show()
        if self.muayeneBtn.styleSheet() == "":
            self.muayeneBtn.setStyleSheet("background-color: blue")
            self.total += self.muayeneKontrol
            self.labelTutar.setText("Tutar : " + str(self.total) + " TL")
        else:
            self.muayeneBtn.setStyleSheet("")
            self.total -= self.muayeneKontrol
            self.labelTutar.setText("Tutar : " + str(self.total) + " TL")
        
    def camfilmFiyat(self):
        if self.camFilmiBtn.styleSheet() == "":
            self.camFilmiBtn.setStyleSheet("background-color: blue")
            self.total += self.camFilmi
            self.labelTutar.setText("Tutar : " + str(self.total) + " TL")
        else:
            self.camFilmiBtn.setStyleSheet("")
            self.total -= self.camFilmi
            self.labelTutar.setText("Tutar : " + str(self.total) + " TL")
        
    def showDate(self,date):
        self.randevuForm.labelGun.setText(str(date("dd")))

    def randevuOlustur(self):
        self.labelTutar.setText("Tutar : " + str(self.total) + " TL")
