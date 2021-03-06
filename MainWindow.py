# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1048, 802)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.BodePlot = QtWidgets.QWidget()
        self.BodePlot.setObjectName("BodePlot")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.BodePlot)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupBox = QtWidgets.QGroupBox(self.BodePlot)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.startFreq_spinBox = QtWidgets.QSpinBox(self.groupBox)
        self.startFreq_spinBox.setMinimum(1)
        self.startFreq_spinBox.setMaximum(1000000)
        self.startFreq_spinBox.setProperty("value", 100)
        self.startFreq_spinBox.setObjectName("startFreq_spinBox")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.startFreq_spinBox)
        self.stopFreq_spinBox = QtWidgets.QSpinBox(self.groupBox)
        self.stopFreq_spinBox.setMinimum(1)
        self.stopFreq_spinBox.setMaximum(1000000)
        self.stopFreq_spinBox.setProperty("value", 20000)
        self.stopFreq_spinBox.setObjectName("stopFreq_spinBox")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.stopFreq_spinBox)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.stepFreq_spinBox = QtWidgets.QSpinBox(self.groupBox)
        self.stepFreq_spinBox.setMinimum(1)
        self.stepFreq_spinBox.setMaximum(500000)
        self.stepFreq_spinBox.setProperty("value", 100)
        self.stepFreq_spinBox.setObjectName("stepFreq_spinBox")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.stepFreq_spinBox)
        self.verticalLayout_2.addLayout(self.formLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.Signal_doubleSpinBox = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.Signal_doubleSpinBox.setMaximum(4.0)
        self.Signal_doubleSpinBox.setProperty("value", 3.0)
        self.Signal_doubleSpinBox.setObjectName("Signal_doubleSpinBox")
        self.horizontalLayout.addWidget(self.Signal_doubleSpinBox)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout_3.addWidget(self.groupBox)
        self.start_pushButton = QtWidgets.QPushButton(self.BodePlot)
        self.start_pushButton.setObjectName("start_pushButton")
        self.verticalLayout_3.addWidget(self.start_pushButton)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.tabWidget.addTab(self.BodePlot, "")
        self.RLCMeter = QtWidgets.QWidget()
        self.RLCMeter.setObjectName("RLCMeter")
        self.tabWidget.addTab(self.RLCMeter, "")
        self.verticalLayout.addWidget(self.tabWidget)
        self.log_plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.log_plainTextEdit.setReadOnly(True)
        self.log_plainTextEdit.setObjectName("log_plainTextEdit")
        self.verticalLayout.addWidget(self.log_plainTextEdit)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1048, 21))
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
        self.groupBox.setTitle(_translate("MainWindow", "Generator Settings"))
        self.label_2.setText(_translate("MainWindow", "From"))
        self.label_3.setText(_translate("MainWindow", "To"))
        self.label.setText(_translate("MainWindow", "Frequency"))
        self.label_5.setText(_translate("MainWindow", "Step"))
        self.label_4.setText(_translate("MainWindow", "Signal (Vpk-pk)"))
        self.start_pushButton.setText(_translate("MainWindow", "Start!"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.BodePlot), _translate("MainWindow", "Bode Plot"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.RLCMeter), _translate("MainWindow", "RLC Meter"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

