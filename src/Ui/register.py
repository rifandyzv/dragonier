# Form implementation generated from reading ui file 'register.ui'
#
# Created by: PyQt6 UI code generator 6.2.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from login import MainWindow
import sys

class Ui_register(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("register")
        MainWindow.resize(720, 504)
        MainWindow.setMinimumSize(QtCore.QSize(720, 504))
        MainWindow.setMaximumSize(QtCore.QSize(720, 504))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(300, 40, 171, 390))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setMaximumSize(QtCore.QSize(100, 20))
        self.label.setLineWidth(1)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout.addWidget(self.lineEdit_2)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setMaximumSize(QtCore.QSize(100, 20))
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setMaximumSize(QtCore.QSize(100, 20))
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.verticalLayout.addWidget(self.lineEdit_3)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_4.setMaximumSize(QtCore.QSize(100, 20))
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.verticalLayout.addWidget(self.lineEdit_4)
        self.label_9 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_9.setMaximumSize(QtCore.QSize(100, 20))
        self.label_9.setLineWidth(1)
        self.label_9.setObjectName("label_9")
        self.verticalLayout.addWidget(self.label_9)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.verticalLayout.addWidget(self.lineEdit_9)
        self.label_10 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_10.setMaximumSize(QtCore.QSize(100, 20))
        self.label_10.setLineWidth(1)
        self.label_10.setObjectName("label_10")
        self.verticalLayout.addWidget(self.label_10)
        self.lineEdit_10 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.verticalLayout.addWidget(self.lineEdit_10)
        self.label_11 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_11.setMaximumSize(QtCore.QSize(100, 20))
        self.label_11.setLineWidth(1)
        self.label_11.setObjectName("label_11")
        self.verticalLayout.addWidget(self.label_11)
        self.lineEdit_11 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.verticalLayout.addWidget(self.lineEdit_11)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 20, 21, 24))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(340, 440, 75, 24))
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Nama Lengkap"))
        self.label_2.setText(_translate("MainWindow", "Email"))
        self.label_3.setText(_translate("MainWindow", "Username"))
        self.label_4.setText(_translate("MainWindow", "Password"))
        self.label_9.setText(_translate("MainWindow", "Cabang"))
        self.label_10.setText(_translate("MainWindow", "Jabatan"))
        self.label_11.setText(_translate("MainWindow", "Role"))
        self.pushButton.setText(_translate("MainWindow", "⬅️"))
        self.pushButton_2.setText(_translate("MainWindow", "Daftar"))
    

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    
    widget = QtWidgets.QStackedWidget()
    MainWindow = MainWindow()
    register = Ui_register()

    widget.addWidget(MainWindow)
    widget.addWidget(register)
    widget.setFixedHeight(512)
    widget.setFixedWidth(512)
    widget.show()