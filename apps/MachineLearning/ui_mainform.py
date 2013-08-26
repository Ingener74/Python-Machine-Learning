# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ml.ui'
#
# Created: Mon Aug 26 17:03:57 2013
#      by: pyside-uic 0.2.13 running on PySide 1.1.0
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(826, 710)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/chalkboard.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tabMain = QtGui.QTabWidget(self.centralwidget)
        self.tabMain.setIconSize(QtCore.QSize(48, 48))
        self.tabMain.setObjectName("tabMain")
        self.tabMultiLayerPerceptron = QtGui.QWidget()
        self.tabMultiLayerPerceptron.setObjectName("tabMultiLayerPerceptron")
        self.gridLayout_3 = QtGui.QGridLayout(self.tabMultiLayerPerceptron)
        self.gridLayout_3.setObjectName("gridLayout_3")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/neuron3.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabMain.addTab(self.tabMultiLayerPerceptron, icon1, "")
        self.tabGeneticAlgorithm = QtGui.QWidget()
        self.tabGeneticAlgorithm.setAccessibleName("")
        self.tabGeneticAlgorithm.setObjectName("tabGeneticAlgorithm")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.tabGeneticAlgorithm)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.graphicsView = QtGui.QGraphicsView(self.tabGeneticAlgorithm)
        self.graphicsView.setObjectName("graphicsView")
        self.horizontalLayout_2.addWidget(self.graphicsView)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton = QtGui.QPushButton(self.tabGeneticAlgorithm)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/genetics-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabMain.addTab(self.tabGeneticAlgorithm, icon2, "")
        self.horizontalLayout.addWidget(self.tabMain)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 826, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        self.tabMain.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.tabMain.setTabText(self.tabMain.indexOf(self.tabMultiLayerPerceptron), QtGui.QApplication.translate("MainWindow", "Multilayer Perceptron", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("MainWindow", "PushButton", None, QtGui.QApplication.UnicodeUTF8))
        self.tabMain.setTabText(self.tabMain.indexOf(self.tabGeneticAlgorithm), QtGui.QApplication.translate("MainWindow", "Genetic algorithm", None, QtGui.QApplication.UnicodeUTF8))

import ml_rc
