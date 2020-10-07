# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'VectorFlowMapping.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1034, 859)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("F:/论文/20200928demo/vfm_app(pyqt写)/界面pyqt/Documents/心脏.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color: rgb(225, 225, 225);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setText("")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 6, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 5, 1, 1, 1)
        self.manualAdjustment = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.manualAdjustment.sizePolicy().hasHeightForWidth())
        self.manualAdjustment.setSizePolicy(sizePolicy)
        self.manualAdjustment.setMaximumSize(QtCore.QSize(16777215, 38))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.manualAdjustment.setFont(font)
        self.manualAdjustment.setStyleSheet("background-color: rgb(170, 0, 255);\n"
"border-radius: 20px;")
        self.manualAdjustment.setObjectName("manualAdjustment")
        self.gridLayout.addWidget(self.manualAdjustment, 3, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 13, 1, 1, 1)
        self.vVorticity = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.vVorticity.sizePolicy().hasHeightForWidth())
        self.vVorticity.setSizePolicy(sizePolicy)
        self.vVorticity.setMaximumSize(QtCore.QSize(16777215, 38))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.vVorticity.setFont(font)
        self.vVorticity.setStyleSheet("background-color: rgb(106, 0, 159);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 20px;")
        self.vVorticity.setObjectName("vVorticity")
        self.gridLayout.addWidget(self.vVorticity, 16, 1, 1, 1)
        self.kineticEnergy = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.kineticEnergy.sizePolicy().hasHeightForWidth())
        self.kineticEnergy.setSizePolicy(sizePolicy)
        self.kineticEnergy.setMaximumSize(QtCore.QSize(16777215, 37))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.kineticEnergy.setFont(font)
        self.kineticEnergy.setStyleSheet("background-color: rgb(106, 0, 159);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 20px;")
        self.kineticEnergy.setObjectName("kineticEnergy")
        self.gridLayout.addWidget(self.kineticEnergy, 17, 1, 1, 1)
        self.quantitativeParamenters = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.quantitativeParamenters.sizePolicy().hasHeightForWidth())
        self.quantitativeParamenters.setSizePolicy(sizePolicy)
        self.quantitativeParamenters.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.quantitativeParamenters.setFont(font)
        self.quantitativeParamenters.setStyleSheet("font: 20pt \"Agency FB\";")
        self.quantitativeParamenters.setObjectName("quantitativeParamenters")
        self.gridLayout.addWidget(self.quantitativeParamenters, 15, 1, 1, 1)
        self.identityTheWall = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.identityTheWall.sizePolicy().hasHeightForWidth())
        self.identityTheWall.setSizePolicy(sizePolicy)
        self.identityTheWall.setMaximumSize(QtCore.QSize(16777215, 37))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.identityTheWall.setFont(font)
        self.identityTheWall.setStyleSheet("background-color: rgb(170, 0, 255);\n"
"border-radius: 20px;")
        self.identityTheWall.setObjectName("identityTheWall")
        self.gridLayout.addWidget(self.identityTheWall, 2, 1, 1, 1)
        self.vectorIllustration = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.vectorIllustration.sizePolicy().hasHeightForWidth())
        self.vectorIllustration.setSizePolicy(sizePolicy)
        self.vectorIllustration.setMaximumSize(QtCore.QSize(16777215, 38))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.vectorIllustration.setFont(font)
        self.vectorIllustration.setStyleSheet("background-color: rgb(170, 0, 127);\n"
"border-radius: 20px;")
        self.vectorIllustration.setObjectName("vectorIllustration")
        self.gridLayout.addWidget(self.vectorIllustration, 9, 1, 1, 1)
        self.wallTrackong = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.wallTrackong.sizePolicy().hasHeightForWidth())
        self.wallTrackong.setSizePolicy(sizePolicy)
        self.wallTrackong.setMaximumSize(QtCore.QSize(16777215, 37))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.wallTrackong.setFont(font)
        self.wallTrackong.setStyleSheet("background-color: rgb(170, 0, 255);\n"
"border-radius: 20px;")
        self.wallTrackong.setObjectName("wallTrackong")
        self.gridLayout.addWidget(self.wallTrackong, 4, 1, 1, 1)
        self.streamlineDiagram = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.streamlineDiagram.sizePolicy().hasHeightForWidth())
        self.streamlineDiagram.setSizePolicy(sizePolicy)
        self.streamlineDiagram.setMaximumSize(QtCore.QSize(16777215, 37))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.streamlineDiagram.setFont(font)
        self.streamlineDiagram.setStyleSheet("background-color: rgb(170, 0, 127);\n"
"border-radius: 20px;")
        self.streamlineDiagram.setObjectName("streamlineDiagram")
        self.gridLayout.addWidget(self.streamlineDiagram, 10, 1, 1, 1)
        self.visualization = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.visualization.sizePolicy().hasHeightForWidth())
        self.visualization.setSizePolicy(sizePolicy)
        self.visualization.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.visualization.setFont(font)
        self.visualization.setStyleSheet("font: 20pt \"Agency FB\";")
        self.visualization.setObjectName("visualization")
        self.gridLayout.addWidget(self.visualization, 8, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 12, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 11, 1, 1, 1)
        self.scroll_ares_images = QtWidgets.QScrollArea(self.centralwidget)
        self.scroll_ares_images.setWidgetResizable(True)
        self.scroll_ares_images.setObjectName("scroll_ares_images")
        self.ImageShow = QtWidgets.QWidget()
        self.ImageShow.setGeometry(QtCore.QRect(0, 0, 871, 784))
        self.ImageShow.setObjectName("ImageShow")
        self.scroll_ares_images.setWidget(self.ImageShow)
        self.gridLayout.addWidget(self.scroll_ares_images, 0, 0, 19, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 7, 1, 1, 1)
        self.wallVelocity = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.wallVelocity.sizePolicy().hasHeightForWidth())
        self.wallVelocity.setSizePolicy(sizePolicy)
        self.wallVelocity.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.wallVelocity.setFont(font)
        self.wallVelocity.setStyleSheet("font: 20pt \"Agency FB\";")
        self.wallVelocity.setObjectName("wallVelocity")
        self.gridLayout.addWidget(self.wallVelocity, 1, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1034, 26))
        self.menubar.setObjectName("menubar")
        self.openFile = QtWidgets.QMenu(self.menubar)
        self.openFile.setObjectName("openFile")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.promptInformation = QtWidgets.QStatusBar(MainWindow)
        self.promptInformation.setObjectName("promptInformation")
        MainWindow.setStatusBar(self.promptInformation)
        self.openFirstFile = QtWidgets.QAction(MainWindow)
        self.openFirstFile.setObjectName("openFirstFile")
        self.openTwoFile = QtWidgets.QAction(MainWindow)
        self.openTwoFile.setObjectName("openTwoFile")
        self.openFile.addAction(self.openFirstFile)
        self.openFile.addAction(self.openTwoFile)
        self.menubar.addAction(self.openFile.menuAction())
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.manualAdjustment.setText(_translate("MainWindow", "手动调整"))
        self.vVorticity.setText(_translate("MainWindow", "涡度"))
        self.kineticEnergy.setText(_translate("MainWindow", "动能"))
        self.quantitativeParamenters.setText(_translate("MainWindow", "参数定量"))
        self.identityTheWall.setText(_translate("MainWindow", "识别室壁"))
        self.vectorIllustration.setText(_translate("MainWindow", "矢量图"))
        self.wallTrackong.setText(_translate("MainWindow", "室壁追踪"))
        self.streamlineDiagram.setText(_translate("MainWindow", "流线图"))
        self.visualization.setText(_translate("MainWindow", "可视化"))
        self.wallVelocity.setText(_translate("MainWindow", "室壁速度"))
        self.openFile.setTitle(_translate("MainWindow", "导入文件"))
        self.menu.setTitle(_translate("MainWindow", "导出文件"))
        self.openFirstFile.setText(_translate("MainWindow", "第一帧"))
        self.openTwoFile.setText(_translate("MainWindow", "第二帧"))
