# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Randevu.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCalendarWidget, QCheckBox, QComboBox,
    QFrame, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QVBoxLayout, QWidget)

class Ui_Randevu(object):
    def setupUi(self, Randevu):
        if not Randevu.objectName():
            Randevu.setObjectName(u"Randevu")
        Randevu.resize(1280, 749)
        Randevu.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QWidget(Randevu)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.titleFrame = QFrame(self.centralwidget)
        self.titleFrame.setObjectName(u"titleFrame")
        self.titleFrame.setMinimumSize(QSize(0, 50))
        self.titleFrame.setMaximumSize(QSize(16777215, 50))
        self.titleFrame.setFrameShape(QFrame.StyledPanel)
        self.titleFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.titleFrame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.labelFrame = QFrame(self.titleFrame)
        self.labelFrame.setObjectName(u"labelFrame")
        self.labelFrame.setMinimumSize(QSize(0, 30))
        self.labelFrame.setFrameShape(QFrame.StyledPanel)
        self.labelFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.labelFrame)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.labelTitle = QLabel(self.labelFrame)
        self.labelTitle.setObjectName(u"labelTitle")
        self.labelTitle.setMinimumSize(QSize(170, 30))
        self.labelTitle.setMaximumSize(QSize(170, 30))
        font = QFont()
        font.setPointSize(15)
        self.labelTitle.setFont(font)

        self.horizontalLayout_3.addWidget(self.labelTitle, 0, Qt.AlignHCenter|Qt.AlignBottom)


        self.horizontalLayout_2.addWidget(self.labelFrame, 0, Qt.AlignTop)


        self.gridLayout.addWidget(self.titleFrame, 0, 0, 1, 1)

        self.mainFrame = QFrame(self.centralwidget)
        self.mainFrame.setObjectName(u"mainFrame")
        self.mainFrame.setFrameShape(QFrame.StyledPanel)
        self.mainFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.mainFrame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuFrame = QFrame(self.mainFrame)
        self.leftMenuFrame.setObjectName(u"leftMenuFrame")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leftMenuFrame.sizePolicy().hasHeightForWidth())
        self.leftMenuFrame.setSizePolicy(sizePolicy)
        self.leftMenuFrame.setMinimumSize(QSize(152, 668))
        self.leftMenuFrame.setMaximumSize(QSize(250, 16777215))
        self.leftMenuFrame.setFrameShape(QFrame.NoFrame)
        self.leftMenuFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.leftMenuFrame)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.aracTipiFrame = QFrame(self.leftMenuFrame)
        self.aracTipiFrame.setObjectName(u"aracTipiFrame")
        self.aracTipiFrame.setMinimumSize(QSize(150, 150))
        self.aracTipiFrame.setMaximumSize(QSize(150, 150))
        self.aracTipiFrame.setFrameShape(QFrame.StyledPanel)
        self.aracTipiFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.aracTipiFrame)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.aracTipiFrame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(140, 0))
        self.frame_4.setMaximumSize(QSize(140, 41))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_4)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(15, 0, 0, 0)
        self.label_2 = QLabel(self.frame_4)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(81, 21))
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.label_2.setFont(font1)

        self.verticalLayout_8.addWidget(self.label_2)


        self.verticalLayout_2.addWidget(self.frame_4)

        self.kamyonetBtn = QPushButton(self.aracTipiFrame)
        self.kamyonetBtn.setObjectName(u"kamyonetBtn")
        self.kamyonetBtn.setMinimumSize(QSize(0, 50))
        font2 = QFont()
        font2.setPointSize(10)
        self.kamyonetBtn.setFont(font2)

        self.verticalLayout_2.addWidget(self.kamyonetBtn, 0, Qt.AlignTop)

        self.otomobilBtn = QPushButton(self.aracTipiFrame)
        self.otomobilBtn.setObjectName(u"otomobilBtn")
        self.otomobilBtn.setMinimumSize(QSize(0, 50))
        self.otomobilBtn.setFont(font2)

        self.verticalLayout_2.addWidget(self.otomobilBtn, 0, Qt.AlignTop)


        self.verticalLayout_4.addWidget(self.aracTipiFrame)

        self.verticalSpacer = QSpacerItem(20, 70, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.secimFrame = QFrame(self.leftMenuFrame)
        self.secimFrame.setObjectName(u"secimFrame")
        self.secimFrame.setFrameShape(QFrame.StyledPanel)
        self.secimFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.secimFrame)
        self.verticalLayout_3.setSpacing(20)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.tamirBtn = QPushButton(self.secimFrame)
        self.tamirBtn.setObjectName(u"tamirBtn")
        self.tamirBtn.setMinimumSize(QSize(0, 50))
        self.tamirBtn.setFont(font2)

        self.verticalLayout_3.addWidget(self.tamirBtn)

        self.bakmBtn = QPushButton(self.secimFrame)
        self.bakmBtn.setObjectName(u"bakmBtn")
        self.bakmBtn.setMinimumSize(QSize(0, 50))
        self.bakmBtn.setFont(font2)

        self.verticalLayout_3.addWidget(self.bakmBtn)

        self.bakimMenu = QFrame(self.secimFrame)
        self.bakimMenu.setObjectName(u"bakimMenu")
        self.bakimMenu.setMinimumSize(QSize(0, 120))
        self.bakimMenu.setFrameShape(QFrame.NoFrame)
        self.bakimMenu.setFrameShadow(QFrame.Raised)
        self.bakimMenu.setLineWidth(2)
        self.verticalLayout_5 = QVBoxLayout(self.bakimMenu)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gazCheck = QCheckBox(self.bakimMenu)
        self.gazCheck.setObjectName(u"gazCheck")
        self.gazCheck.setFont(font2)

        self.verticalLayout_5.addWidget(self.gazCheck)

        self.lastikCheck = QCheckBox(self.bakimMenu)
        self.lastikCheck.setObjectName(u"lastikCheck")
        self.lastikCheck.setFont(font2)

        self.verticalLayout_5.addWidget(self.lastikCheck)

        self.rotCheck = QCheckBox(self.bakimMenu)
        self.rotCheck.setObjectName(u"rotCheck")
        self.rotCheck.setFont(font2)

        self.verticalLayout_5.addWidget(self.rotCheck)

        self.yagCheck = QCheckBox(self.bakimMenu)
        self.yagCheck.setObjectName(u"yagCheck")
        self.yagCheck.setFont(font2)

        self.verticalLayout_5.addWidget(self.yagCheck)


        self.verticalLayout_3.addWidget(self.bakimMenu)

        self.secimBottom = QFrame(self.secimFrame)
        self.secimBottom.setObjectName(u"secimBottom")
        self.secimBottom.setFrameShape(QFrame.StyledPanel)
        self.secimBottom.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.secimBottom)
        self.verticalLayout_7.setSpacing(25)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.muayeneBtn = QPushButton(self.secimBottom)
        self.muayeneBtn.setObjectName(u"muayeneBtn")
        self.muayeneBtn.setMinimumSize(QSize(0, 50))
        self.muayeneBtn.setFont(font2)

        self.verticalLayout_7.addWidget(self.muayeneBtn)

        self.camFilmBtn = QPushButton(self.secimBottom)
        self.camFilmBtn.setObjectName(u"camFilmBtn")
        self.camFilmBtn.setMinimumSize(QSize(0, 50))
        self.camFilmBtn.setFont(font2)

        self.verticalLayout_7.addWidget(self.camFilmBtn)


        self.verticalLayout_3.addWidget(self.secimBottom, 0, Qt.AlignTop)


        self.verticalLayout_4.addWidget(self.secimFrame)

        self.cikisBtn = QPushButton(self.leftMenuFrame)
        self.cikisBtn.setObjectName(u"cikisBtn")
        self.cikisBtn.setMinimumSize(QSize(0, 50))
        self.cikisBtn.setFont(font2)

        self.verticalLayout_4.addWidget(self.cikisBtn, 0, Qt.AlignBottom)


        self.horizontalLayout.addWidget(self.leftMenuFrame)

        self.stackedWidget = QStackedWidget(self.mainFrame)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_13 = QVBoxLayout(self.page)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.topFrame = QFrame(self.page)
        self.topFrame.setObjectName(u"topFrame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.topFrame.sizePolicy().hasHeightForWidth())
        self.topFrame.setSizePolicy(sizePolicy1)
        self.topFrame.setFrameShape(QFrame.StyledPanel)
        self.topFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.topFrame)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 50, 0)
        self.kisiselInfoFrame = QFrame(self.topFrame)
        self.kisiselInfoFrame.setObjectName(u"kisiselInfoFrame")
        self.kisiselInfoFrame.setFrameShape(QFrame.StyledPanel)
        self.kisiselInfoFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.kisiselInfoFrame)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.labelInftoFrame_3 = QFrame(self.kisiselInfoFrame)
        self.labelInftoFrame_3.setObjectName(u"labelInftoFrame_3")
        self.labelInftoFrame_3.setMaximumSize(QSize(100, 16777215))
        self.labelInftoFrame_3.setFrameShape(QFrame.StyledPanel)
        self.labelInftoFrame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.labelInftoFrame_3)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.labelInftoFrame_3)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(100, 25))
        font3 = QFont()
        font3.setFamilies([u"Favela-Regular"])
        font3.setPointSize(10)
        self.label.setFont(font3)

        self.verticalLayout_6.addWidget(self.label)

        self.labelAd = QLabel(self.labelInftoFrame_3)
        self.labelAd.setObjectName(u"labelAd")
        self.labelAd.setMaximumSize(QSize(100, 25))
        self.labelAd.setFont(font3)

        self.verticalLayout_6.addWidget(self.labelAd)

        self.labelSoyad = QLabel(self.labelInftoFrame_3)
        self.labelSoyad.setObjectName(u"labelSoyad")
        self.labelSoyad.setMaximumSize(QSize(100, 25))
        self.labelSoyad.setFont(font3)

        self.verticalLayout_6.addWidget(self.labelSoyad)

        self.labelTelefon = QLabel(self.labelInftoFrame_3)
        self.labelTelefon.setObjectName(u"labelTelefon")
        self.labelTelefon.setMaximumSize(QSize(100, 25))
        self.labelTelefon.setFont(font3)

        self.verticalLayout_6.addWidget(self.labelTelefon)

        self.labelGmail = QLabel(self.labelInftoFrame_3)
        self.labelGmail.setObjectName(u"labelGmail")
        self.labelGmail.setMaximumSize(QSize(100, 25))
        self.labelGmail.setFont(font3)

        self.verticalLayout_6.addWidget(self.labelGmail)


        self.horizontalLayout_7.addWidget(self.labelInftoFrame_3)

        self.textInfoFrame = QFrame(self.kisiselInfoFrame)
        self.textInfoFrame.setObjectName(u"textInfoFrame")
        sizePolicy.setHeightForWidth(self.textInfoFrame.sizePolicy().hasHeightForWidth())
        self.textInfoFrame.setSizePolicy(sizePolicy)
        self.textInfoFrame.setMaximumSize(QSize(300, 16777215))
        self.textInfoFrame.setFrameShape(QFrame.StyledPanel)
        self.textInfoFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.textInfoFrame)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.tcText = QLineEdit(self.textInfoFrame)
        self.tcText.setObjectName(u"tcText")
        self.tcText.setMaximumSize(QSize(16777215, 25))

        self.verticalLayout_12.addWidget(self.tcText)

        self.adText = QLineEdit(self.textInfoFrame)
        self.adText.setObjectName(u"adText")
        self.adText.setMinimumSize(QSize(0, 20))
        self.adText.setMaximumSize(QSize(16777215, 25))

        self.verticalLayout_12.addWidget(self.adText)

        self.soyadText = QLineEdit(self.textInfoFrame)
        self.soyadText.setObjectName(u"soyadText")
        self.soyadText.setMinimumSize(QSize(0, 20))
        self.soyadText.setMaximumSize(QSize(16777215, 25))

        self.verticalLayout_12.addWidget(self.soyadText)

        self.telefonText = QLineEdit(self.textInfoFrame)
        self.telefonText.setObjectName(u"telefonText")
        self.telefonText.setMinimumSize(QSize(0, 20))
        self.telefonText.setMaximumSize(QSize(16777215, 25))

        self.verticalLayout_12.addWidget(self.telefonText)

        self.gmailText = QLineEdit(self.textInfoFrame)
        self.gmailText.setObjectName(u"gmailText")
        self.gmailText.setMinimumSize(QSize(0, 20))
        self.gmailText.setMaximumSize(QSize(16777215, 25))

        self.verticalLayout_12.addWidget(self.gmailText)


        self.horizontalLayout_7.addWidget(self.textInfoFrame)


        self.horizontalLayout_8.addWidget(self.kisiselInfoFrame)

        self.aracFrame = QFrame(self.topFrame)
        self.aracFrame.setObjectName(u"aracFrame")
        self.aracFrame.setFrameShape(QFrame.StyledPanel)
        self.aracFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.aracFrame)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.labelAracFrame_3 = QFrame(self.aracFrame)
        self.labelAracFrame_3.setObjectName(u"labelAracFrame_3")
        self.labelAracFrame_3.setMaximumSize(QSize(150, 16777215))
        self.labelAracFrame_3.setFrameShape(QFrame.StyledPanel)
        self.labelAracFrame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.labelAracFrame_3)
        self.verticalLayout_10.setSpacing(10)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.labelMarka = QLabel(self.labelAracFrame_3)
        self.labelMarka.setObjectName(u"labelMarka")
        self.labelMarka.setMaximumSize(QSize(150, 25))
        self.labelMarka.setFont(font3)

        self.verticalLayout_10.addWidget(self.labelMarka)

        self.labelModel = QLabel(self.labelAracFrame_3)
        self.labelModel.setObjectName(u"labelModel")
        self.labelModel.setMaximumSize(QSize(150, 25))
        self.labelModel.setFont(font3)

        self.verticalLayout_10.addWidget(self.labelModel)

        self.labelKm = QLabel(self.labelAracFrame_3)
        self.labelKm.setObjectName(u"labelKm")
        self.labelKm.setMaximumSize(QSize(150, 25))
        self.labelKm.setFont(font3)

        self.verticalLayout_10.addWidget(self.labelKm)

        self.labelPlaka = QLabel(self.labelAracFrame_3)
        self.labelPlaka.setObjectName(u"labelPlaka")
        self.labelPlaka.setMaximumSize(QSize(150, 25))
        self.labelPlaka.setFont(font3)

        self.verticalLayout_10.addWidget(self.labelPlaka)


        self.horizontalLayout_4.addWidget(self.labelAracFrame_3)

        self.aracInfoFrame = QFrame(self.aracFrame)
        self.aracInfoFrame.setObjectName(u"aracInfoFrame")
        self.aracInfoFrame.setMaximumSize(QSize(300, 16777215))
        self.aracInfoFrame.setFrameShape(QFrame.StyledPanel)
        self.aracInfoFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.aracInfoFrame)
        self.verticalLayout_11.setSpacing(15)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.markaCombo = QComboBox(self.aracInfoFrame)
        self.markaCombo.addItem("")
        self.markaCombo.addItem("")
        self.markaCombo.addItem("")
        self.markaCombo.addItem("")
        self.markaCombo.addItem("")
        self.markaCombo.addItem("")
        self.markaCombo.addItem("")
        self.markaCombo.addItem("")
        self.markaCombo.addItem("")
        self.markaCombo.addItem("")
        self.markaCombo.addItem("")
        self.markaCombo.addItem("")
        self.markaCombo.addItem("")
        self.markaCombo.addItem("")
        self.markaCombo.addItem("")
        self.markaCombo.addItem("")
        self.markaCombo.addItem("")
        self.markaCombo.addItem("")
        self.markaCombo.addItem("")
        self.markaCombo.addItem("")
        self.markaCombo.addItem("")
        self.markaCombo.addItem("")
        self.markaCombo.addItem("")
        self.markaCombo.addItem("")
        self.markaCombo.addItem("")
        self.markaCombo.addItem("")
        self.markaCombo.addItem("")
        self.markaCombo.addItem("")
        self.markaCombo.addItem("")
        self.markaCombo.setObjectName(u"markaCombo")
        self.markaCombo.setMaximumSize(QSize(16777215, 25))
        self.markaCombo.setDuplicatesEnabled(False)
        self.markaCombo.setFrame(True)

        self.verticalLayout_11.addWidget(self.markaCombo)

        self.modelCombo = QComboBox(self.aracInfoFrame)
        self.modelCombo.addItem("")
        self.modelCombo.addItem("")
        self.modelCombo.addItem("")
        self.modelCombo.addItem("")
        self.modelCombo.addItem("")
        self.modelCombo.addItem("")
        self.modelCombo.addItem("")
        self.modelCombo.addItem("")
        self.modelCombo.addItem("")
        self.modelCombo.addItem("")
        self.modelCombo.addItem("")
        self.modelCombo.addItem("")
        self.modelCombo.addItem("")
        self.modelCombo.addItem("")
        self.modelCombo.addItem("")
        self.modelCombo.addItem("")
        self.modelCombo.addItem("")
        self.modelCombo.addItem("")
        self.modelCombo.addItem("")
        self.modelCombo.addItem("")
        self.modelCombo.addItem("")
        self.modelCombo.addItem("")
        self.modelCombo.addItem("")
        self.modelCombo.addItem("")
        self.modelCombo.addItem("")
        self.modelCombo.addItem("")
        self.modelCombo.addItem("")
        self.modelCombo.addItem("")
        self.modelCombo.addItem("")
        self.modelCombo.addItem("")
        self.modelCombo.addItem("")
        self.modelCombo.addItem("")
        self.modelCombo.addItem("")
        self.modelCombo.addItem("")
        self.modelCombo.setObjectName(u"modelCombo")
        self.modelCombo.setMaximumSize(QSize(16777215, 25))

        self.verticalLayout_11.addWidget(self.modelCombo)

        self.kmText = QLineEdit(self.aracInfoFrame)
        self.kmText.setObjectName(u"kmText")
        self.kmText.setMinimumSize(QSize(0, 20))
        self.kmText.setMaximumSize(QSize(16777215, 25))

        self.verticalLayout_11.addWidget(self.kmText)

        self.plakaText = QLineEdit(self.aracInfoFrame)
        self.plakaText.setObjectName(u"plakaText")
        self.plakaText.setMinimumSize(QSize(0, 20))
        self.plakaText.setMaximumSize(QSize(16777215, 25))

        self.verticalLayout_11.addWidget(self.plakaText)


        self.horizontalLayout_4.addWidget(self.aracInfoFrame)


        self.horizontalLayout_8.addWidget(self.aracFrame)


        self.verticalLayout_13.addWidget(self.topFrame)

        self.bottomFrame = QFrame(self.page)
        self.bottomFrame.setObjectName(u"bottomFrame")
        self.bottomFrame.setFrameShape(QFrame.StyledPanel)
        self.bottomFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.bottomFrame)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.tutarTopFrame = QFrame(self.bottomFrame)
        self.tutarTopFrame.setObjectName(u"tutarTopFrame")
        sizePolicy1.setHeightForWidth(self.tutarTopFrame.sizePolicy().hasHeightForWidth())
        self.tutarTopFrame.setSizePolicy(sizePolicy1)
        self.tutarTopFrame.setFrameShape(QFrame.StyledPanel)
        self.tutarTopFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.tutarTopFrame)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.tarihFrame = QFrame(self.tutarTopFrame)
        self.tarihFrame.setObjectName(u"tarihFrame")
        self.tarihFrame.setMaximumSize(QSize(16777215, 60))
        self.tarihFrame.setFrameShape(QFrame.StyledPanel)
        self.tarihFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.tarihFrame)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalSpacer_2 = QSpacerItem(300, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_2)

        self.labelTitle_2 = QLabel(self.tarihFrame)
        self.labelTitle_2.setObjectName(u"labelTitle_2")
        self.labelTitle_2.setMinimumSize(QSize(170, 30))
        self.labelTitle_2.setMaximumSize(QSize(220, 30))
        self.labelTitle_2.setFont(font)

        self.horizontalLayout_6.addWidget(self.labelTitle_2)

        self.horizontalSpacer = QSpacerItem(423, 17, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer)


        self.verticalLayout_16.addWidget(self.tarihFrame)

        self.ajandaFrame = QFrame(self.tutarTopFrame)
        self.ajandaFrame.setObjectName(u"ajandaFrame")
        self.ajandaFrame.setMaximumSize(QSize(16777215, 220))
        self.ajandaFrame.setFrameShape(QFrame.StyledPanel)
        self.ajandaFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.ajandaFrame)
        self.horizontalLayout_10.setSpacing(50)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(40, 0, 0, 0)
        self.calenderFrame = QFrame(self.ajandaFrame)
        self.calenderFrame.setObjectName(u"calenderFrame")
        self.calenderFrame.setMinimumSize(QSize(0, 230))
        self.calenderFrame.setMaximumSize(QSize(416, 230))
        self.calenderFrame.setFrameShape(QFrame.StyledPanel)
        self.calenderFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.calenderFrame)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.calendarWidget = QCalendarWidget(self.calenderFrame)
        self.calendarWidget.setObjectName(u"calendarWidget")

        self.horizontalLayout_9.addWidget(self.calendarWidget)


        self.horizontalLayout_10.addWidget(self.calenderFrame)

        self.dateFrame = QFrame(self.ajandaFrame)
        self.dateFrame.setObjectName(u"dateFrame")
        self.dateFrame.setFrameShape(QFrame.StyledPanel)
        self.dateFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.dateFrame)
        self.horizontalLayout_14.setSpacing(15)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.dateLabelFrame = QFrame(self.dateFrame)
        self.dateLabelFrame.setObjectName(u"dateLabelFrame")
        self.dateLabelFrame.setMaximumSize(QSize(50, 16777215))
        self.dateLabelFrame.setFrameShape(QFrame.StyledPanel)
        self.dateLabelFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.dateLabelFrame)
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.dateLabelFrame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(50, 16777215))
        self.label_3.setFont(font3)

        self.verticalLayout_21.addWidget(self.label_3)

        self.label_4 = QLabel(self.dateLabelFrame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(50, 16777215))
        self.label_4.setFont(font3)

        self.verticalLayout_21.addWidget(self.label_4)

        self.label_5 = QLabel(self.dateLabelFrame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(50, 16777215))
        self.label_5.setFont(font3)

        self.verticalLayout_21.addWidget(self.label_5)


        self.horizontalLayout_14.addWidget(self.dateLabelFrame)

        self.frame = QFrame(self.dateFrame)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.labelGun = QLabel(self.frame)
        self.labelGun.setObjectName(u"labelGun")
        self.labelGun.setFont(font3)

        self.verticalLayout_15.addWidget(self.labelGun)


        self.horizontalLayout_14.addWidget(self.frame)


        self.horizontalLayout_10.addWidget(self.dateFrame)


        self.verticalLayout_16.addWidget(self.ajandaFrame)


        self.verticalLayout_14.addWidget(self.tutarTopFrame)

        self.tutarFrame = QFrame(self.bottomFrame)
        self.tutarFrame.setObjectName(u"tutarFrame")
        self.tutarFrame.setMinimumSize(QSize(0, 35))
        self.tutarFrame.setFrameShape(QFrame.StyledPanel)
        self.tutarFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.tutarFrame)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.labelTutar = QLabel(self.tutarFrame)
        self.labelTutar.setObjectName(u"labelTutar")
        self.labelTutar.setMinimumSize(QSize(300, 0))
        self.labelTutar.setFont(font3)

        self.horizontalLayout_15.addWidget(self.labelTutar, 0, Qt.AlignHCenter)

        self.onayBtn = QPushButton(self.tutarFrame)
        self.onayBtn.setObjectName(u"onayBtn")
        self.onayBtn.setMinimumSize(QSize(100, 50))
        self.onayBtn.setMaximumSize(QSize(100, 50))
        self.onayBtn.setFont(font3)

        self.horizontalLayout_15.addWidget(self.onayBtn)


        self.verticalLayout_14.addWidget(self.tutarFrame, 0, Qt.AlignBottom)


        self.verticalLayout_13.addWidget(self.bottomFrame)

        self.stackedWidget.addWidget(self.page)

        self.horizontalLayout.addWidget(self.stackedWidget)


        self.gridLayout.addWidget(self.mainFrame, 1, 0, 1, 1)

        Randevu.setCentralWidget(self.centralwidget)

        self.retranslateUi(Randevu)
        self.calendarWidget.selectionChanged.connect(self.labelGun.update)

        self.markaCombo.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Randevu)
    # setupUi

    def retranslateUi(self, Randevu):
        Randevu.setWindowTitle(QCoreApplication.translate("Randevu", u"Randevu", None))
        self.labelTitle.setText(QCoreApplication.translate("Randevu", u"RANDEVU T\u0130P\u0130", None))
        self.label_2.setText(QCoreApplication.translate("Randevu", u"ARA\u00c7 T\u0130P\u0130", None))
        self.kamyonetBtn.setText(QCoreApplication.translate("Randevu", u"Kamyonet", None))
        self.otomobilBtn.setText(QCoreApplication.translate("Randevu", u"Otomobil", None))
        self.tamirBtn.setText(QCoreApplication.translate("Randevu", u"TAM\u0130R", None))
        self.bakmBtn.setText(QCoreApplication.translate("Randevu", u"BAKIM", None))
        self.gazCheck.setText(QCoreApplication.translate("Randevu", u"Gaz ayar\u0131", None))
        self.lastikCheck.setText(QCoreApplication.translate("Randevu", u"Lastik kontrol\u00fc", None))
        self.rotCheck.setText(QCoreApplication.translate("Randevu", u"Rot balans ", None))
        self.yagCheck.setText(QCoreApplication.translate("Randevu", u"Ya\u011f de\u011fi\u015fimi", None))
        self.muayeneBtn.setText(QCoreApplication.translate("Randevu", u"Muayene kontrol\u00fc", None))
        self.camFilmBtn.setText(QCoreApplication.translate("Randevu", u"Cam filmi", None))
        self.cikisBtn.setText(QCoreApplication.translate("Randevu", u"\u00c7\u0131k\u0131\u015f Yap", None))
        self.label.setText(QCoreApplication.translate("Randevu", u"TC NO :", None))
        self.labelAd.setText(QCoreApplication.translate("Randevu", u"AD :", None))
        self.labelSoyad.setText(QCoreApplication.translate("Randevu", u"SOYAD :", None))
        self.labelTelefon.setText(QCoreApplication.translate("Randevu", u"TELEFON :", None))
        self.labelGmail.setText(QCoreApplication.translate("Randevu", u"GMA\u0130L : ", None))
        self.labelMarka.setText(QCoreApplication.translate("Randevu", u"ARAC MARKASI:", None))
        self.labelModel.setText(QCoreApplication.translate("Randevu", u"ARAC MODEL\u0130 :", None))
        self.labelKm.setText(QCoreApplication.translate("Randevu", u"ARAC KM :", None))
        self.labelPlaka.setText(QCoreApplication.translate("Randevu", u"ARAC PLAKA :", None))
        self.markaCombo.setItemText(0, QCoreApplication.translate("Randevu", u"Se\u00e7iniz", None))
        self.markaCombo.setItemText(1, QCoreApplication.translate("Randevu", u"Alfa Romeo", None))
        self.markaCombo.setItemText(2, QCoreApplication.translate("Randevu", u"Aston Martin", None))
        self.markaCombo.setItemText(3, QCoreApplication.translate("Randevu", u"Audi", None))
        self.markaCombo.setItemText(4, QCoreApplication.translate("Randevu", u"BMW", None))
        self.markaCombo.setItemText(5, QCoreApplication.translate("Randevu", u"Chery", None))
        self.markaCombo.setItemText(6, QCoreApplication.translate("Randevu", u"Chery", None))
        self.markaCombo.setItemText(7, QCoreApplication.translate("Randevu", u"Dacia", None))
        self.markaCombo.setItemText(8, QCoreApplication.translate("Randevu", u"Dodge", None))
        self.markaCombo.setItemText(9, QCoreApplication.translate("Randevu", u"Fiat", None))
        self.markaCombo.setItemText(10, QCoreApplication.translate("Randevu", u"Ford", None))
        self.markaCombo.setItemText(11, QCoreApplication.translate("Randevu", u"Honda", None))
        self.markaCombo.setItemText(12, QCoreApplication.translate("Randevu", u"Hyundai", None))
        self.markaCombo.setItemText(13, QCoreApplication.translate("Randevu", u"Isuzu", None))
        self.markaCombo.setItemText(14, QCoreApplication.translate("Randevu", u"Kia", None))
        self.markaCombo.setItemText(15, QCoreApplication.translate("Randevu", u"Lada", None))
        self.markaCombo.setItemText(16, QCoreApplication.translate("Randevu", u"Mazda", None))
        self.markaCombo.setItemText(17, QCoreApplication.translate("Randevu", u"Mercedes", None))
        self.markaCombo.setItemText(18, QCoreApplication.translate("Randevu", u"Mitsubishi", None))
        self.markaCombo.setItemText(19, QCoreApplication.translate("Randevu", u"Nissan", None))
        self.markaCombo.setItemText(20, QCoreApplication.translate("Randevu", u"Peugeot", None))
        self.markaCombo.setItemText(21, QCoreApplication.translate("Randevu", u"Renault", None))
        self.markaCombo.setItemText(22, QCoreApplication.translate("Randevu", u"Seat", None))
        self.markaCombo.setItemText(23, QCoreApplication.translate("Randevu", u"Subaru", None))
        self.markaCombo.setItemText(24, QCoreApplication.translate("Randevu", u"Suzuki", None))
        self.markaCombo.setItemText(25, QCoreApplication.translate("Randevu", u"TOFA\u015e", None))
        self.markaCombo.setItemText(26, QCoreApplication.translate("Randevu", u"Toyota", None))
        self.markaCombo.setItemText(27, QCoreApplication.translate("Randevu", u"Volkswagen", None))
        self.markaCombo.setItemText(28, QCoreApplication.translate("Randevu", u"Volvo", None))

        self.modelCombo.setItemText(0, QCoreApplication.translate("Randevu", u"Se\u00e7iniz", None))
        self.modelCombo.setItemText(1, QCoreApplication.translate("Randevu", u"1990", None))
        self.modelCombo.setItemText(2, QCoreApplication.translate("Randevu", u"1991", None))
        self.modelCombo.setItemText(3, QCoreApplication.translate("Randevu", u"1992", None))
        self.modelCombo.setItemText(4, QCoreApplication.translate("Randevu", u"1993", None))
        self.modelCombo.setItemText(5, QCoreApplication.translate("Randevu", u"1994", None))
        self.modelCombo.setItemText(6, QCoreApplication.translate("Randevu", u"1995", None))
        self.modelCombo.setItemText(7, QCoreApplication.translate("Randevu", u"1996", None))
        self.modelCombo.setItemText(8, QCoreApplication.translate("Randevu", u"1997", None))
        self.modelCombo.setItemText(9, QCoreApplication.translate("Randevu", u"1998", None))
        self.modelCombo.setItemText(10, QCoreApplication.translate("Randevu", u"1999", None))
        self.modelCombo.setItemText(11, QCoreApplication.translate("Randevu", u"2000", None))
        self.modelCombo.setItemText(12, QCoreApplication.translate("Randevu", u"2001", None))
        self.modelCombo.setItemText(13, QCoreApplication.translate("Randevu", u"2002", None))
        self.modelCombo.setItemText(14, QCoreApplication.translate("Randevu", u"2003", None))
        self.modelCombo.setItemText(15, QCoreApplication.translate("Randevu", u"2004", None))
        self.modelCombo.setItemText(16, QCoreApplication.translate("Randevu", u"2005", None))
        self.modelCombo.setItemText(17, QCoreApplication.translate("Randevu", u"2006", None))
        self.modelCombo.setItemText(18, QCoreApplication.translate("Randevu", u"2007", None))
        self.modelCombo.setItemText(19, QCoreApplication.translate("Randevu", u"2008", None))
        self.modelCombo.setItemText(20, QCoreApplication.translate("Randevu", u"2009", None))
        self.modelCombo.setItemText(21, QCoreApplication.translate("Randevu", u"2010", None))
        self.modelCombo.setItemText(22, QCoreApplication.translate("Randevu", u"2011", None))
        self.modelCombo.setItemText(23, QCoreApplication.translate("Randevu", u"2012", None))
        self.modelCombo.setItemText(24, QCoreApplication.translate("Randevu", u"2013", None))
        self.modelCombo.setItemText(25, QCoreApplication.translate("Randevu", u"2014", None))
        self.modelCombo.setItemText(26, QCoreApplication.translate("Randevu", u"2015", None))
        self.modelCombo.setItemText(27, QCoreApplication.translate("Randevu", u"2016", None))
        self.modelCombo.setItemText(28, QCoreApplication.translate("Randevu", u"2017", None))
        self.modelCombo.setItemText(29, QCoreApplication.translate("Randevu", u"2018", None))
        self.modelCombo.setItemText(30, QCoreApplication.translate("Randevu", u"2019", None))
        self.modelCombo.setItemText(31, QCoreApplication.translate("Randevu", u"2020", None))
        self.modelCombo.setItemText(32, QCoreApplication.translate("Randevu", u"2021", None))
        self.modelCombo.setItemText(33, QCoreApplication.translate("Randevu", u"2022", None))

        self.labelTitle_2.setText(QCoreApplication.translate("Randevu", u"RANDEVU TAR\u0130H\u0130", None))
        self.label_3.setText(QCoreApplication.translate("Randevu", u"G\u00fcn :", None))
        self.label_4.setText(QCoreApplication.translate("Randevu", u"Ay :", None))
        self.label_5.setText(QCoreApplication.translate("Randevu", u"Y\u0131l :", None))
        self.labelGun.setText("")
        self.labelTutar.setText(QCoreApplication.translate("Randevu", u"Tutar :", None))
        self.onayBtn.setText(QCoreApplication.translate("Randevu", u"ONAYLA", None))
    # retranslateUi

