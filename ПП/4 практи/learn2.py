# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'learn1.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(502, 332)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setObjectName("centralwidget")
        
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 491, 291))
        self.tabWidget.setObjectName("tabWidget")
        
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        
        self.scrollArea = QtWidgets.QScrollArea(self.tab)
        self.scrollArea.setGeometry(QtCore.QRect(10, 10, 451, 241))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 447, 237))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")

        self.frame = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame.setGeometry(QtCore.QRect(20, 100, 311, 111))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(20, 10, 221, 16))
        self.label.setObjectName("label")
        
        self.radioButton = QtWidgets.QRadioButton(self.frame)
        self.radioButton.setGeometry(QtCore.QRect(20, 30, 82, 18))
        self.radioButton.setObjectName("radioButton")
        self.buttonGroup = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.radioButton)
        
        self.radioButton_2 = QtWidgets.QRadioButton(self.frame)
        self.radioButton_2.setGeometry(QtCore.QRect(20, 50, 82, 18))
        self.radioButton_2.setObjectName("radioButton_2")
        self.buttonGroup.addButton(self.radioButton_2)
        self.radioButton_3 = QtWidgets.QRadioButton(self.frame)
        self.radioButton_3.setGeometry(QtCore.QRect(20, 80, 82, 18))
        self.radioButton_3.setObjectName("radioButton_3")
        self.buttonGroup.addButton(self.radioButton_3)
        self.textEdit = QtWidgets.QTextEdit(self.scrollAreaWidgetContents)
        self.textEdit.setGeometry(QtCore.QRect(20, 10, 411, 41))
        self.textEdit.setObjectName("textEdit")
        
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        
        self.scrollArea_2 = QtWidgets.QScrollArea(self.tab_2)
        self.scrollArea_2.setGeometry(QtCore.QRect(20, 10, 451, 241))
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 447, 237))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")

        self.frame_2 = QtWidgets.QFrame(self.scrollAreaWidgetContents_2)
        self.frame_2.setGeometry(QtCore.QRect(20, 110, 271, 111))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(10, 0, 46, 13))
        self.label_2.setObjectName("label_2")

        self.radioButton_4 = QtWidgets.QRadioButton(self.frame_2)
        self.radioButton_4.setGeometry(QtCore.QRect(10, 20, 82, 18))
        self.radioButton_4.setObjectName("radioButton_4")
        self.buttonGroup_2 = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup_2.setObjectName("buttonGroup_2")
        self.buttonGroup_2.addButton(self.radioButton_4)
        
        self.radioButton_5 = QtWidgets.QRadioButton(self.frame_2)
        self.radioButton_5.setGeometry(QtCore.QRect(10, 50, 82, 18))
        self.radioButton_5.setObjectName("radioButton_5")
        self.buttonGroup_2.addButton(self.radioButton_5)
        
        self.radioButton_6 = QtWidgets.QRadioButton(self.frame_2)
        self.radioButton_6.setGeometry(QtCore.QRect(10, 80, 82, 18))
        self.radioButton_6.setObjectName("radioButton_6")
        self.buttonGroup_2.addButton(self.radioButton_6)
        
        self.textEdit_2 = QtWidgets.QTextEdit(self.scrollAreaWidgetContents_2)
        self.textEdit_2.setGeometry(QtCore.QRect(10, 10, 421, 81))
        self.textEdit_2.setObjectName("textEdit_2")
        
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.scrollArea_3 = QtWidgets.QScrollArea(self.tab_3)
        self.scrollArea_3.setGeometry(QtCore.QRect(10, 10, 451, 241))
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollArea_3.setObjectName("scrollArea_3")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 447, 237))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.frame_3 = QtWidgets.QFrame(self.scrollAreaWidgetContents_3)
        self.frame_3.setGeometry(QtCore.QRect(20, 90, 171, 131))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label_3 = QtWidgets.QLabel(self.frame_3)
        self.label_3.setGeometry(QtCore.QRect(20, 20, 46, 13))
        self.label_3.setObjectName("label_3")
        self.radioButton_7 = QtWidgets.QRadioButton(self.frame_3)
        self.radioButton_7.setGeometry(QtCore.QRect(10, 40, 82, 18))
        self.radioButton_7.setObjectName("radioButton_7")
        self.buttonGroup_3 = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup_3.setObjectName("buttonGroup_3")
        self.buttonGroup_3.addButton(self.radioButton_7)
        self.radioButton_8 = QtWidgets.QRadioButton(self.frame_3)
        self.radioButton_8.setGeometry(QtCore.QRect(10, 60, 82, 18))
        self.radioButton_8.setObjectName("radioButton_8")
        self.buttonGroup_3.addButton(self.radioButton_8)
        self.radioButton_9 = QtWidgets.QRadioButton(self.frame_3)
        self.radioButton_9.setGeometry(QtCore.QRect(10, 80, 82, 18))
        self.radioButton_9.setObjectName("radioButton_9")
        self.buttonGroup_3.addButton(self.radioButton_9)

        

        
        self.textEdit_3 = QtWidgets.QTextEdit(self.scrollAreaWidgetContents_3)
        self.textEdit_3.setGeometry(QtCore.QRect(20, 10, 411, 51))
        self.textEdit_3.setObjectName("textEdit_3")
        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)
        self.tabWidget.addTab(self.tab_3, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 502, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        
        self.textEdit.setText(_translate("MainWindow", "Где RadioButton?"))
        self.label.setText(_translate("MainWindow", "Один правильный"))
        self.radioButton.setText(_translate("MainWindow", "Kek"))
        self.radioButton_2.setText(_translate("MainWindow", "RadioButton2"))
        self.radioButton_3.setText(_translate("MainWindow", "RadioButton"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Tab 1"))

        self.textEdit_2.setText(_translate("MainWindow", "Где ComboBox?"))        
        self.label_2.setText(_translate("MainWindow", "Один правильный"))
        self.radioButton_4.setText(_translate("MainWindow", "RadioButton"))
        self.radioButton_5.setText(_translate("MainWindow", "RadioButton"))
        self.radioButton_6.setText(_translate("MainWindow", "RadioButton"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))

        self.textEdit_3.setText(_translate("MainWindow", "Где Tab Widgets?"))        
        self.label_3.setText(_translate("MainWindow", "Один правильный"))
        self.radioButton_7.setText(_translate("MainWindow", "RadioButton"))
        self.radioButton_8.setText(_translate("MainWindow", "RadioButton"))
        self.radioButton_9.setText(_translate("MainWindow", "RadioButton"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Страница"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

