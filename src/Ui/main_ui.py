import sys
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QDialog, QApplication, QMainWindow, QMessageBox, QWidget
from PyQt6.uic import loadUi
from dashboard import Ui_MainWindow
import requests
class Login(QWidget) :
    def __init__(self):
        super(Login, self).__init__()
        loadUi("login.ui", self)
        self.pushButton.clicked.connect(self.login)
        self.pushButton_2.clicked.connect(self.goToRegister)
    def goToRegister(self) :
        register = Register()
        # widget.insertWidget(register)
        widget.addWidget(register)
        widget.setCurrentWidget(register)
        # widget.setCurrentIndex(widget.currentIndex()+1)
    def login(self) :
        print(self.lineEdit.text())
        print(self.lineEdit_2.text())
        if (True) :
            MainWindow = Dashboard()
            # widget.insertWidget(MainWindow)
            widget.addWidget(MainWindow)
            widget.setCurrentWidget(MainWindow)
            # widget.setCurrentIndex(widget.currentIndex()+1)
        


class Register(QWidget) :
    def __init__(self) :
        super(Register, self).__init__()
        loadUi("register_w.ui", self)
        self.pushButton.clicked.connect(self.goToLogin)
    def goToLogin(self) :
        
        # widget.removeWidget()
        widget.setCurrentIndex(0)
class Dashboard(QMainWindow) :
    def __init__(self) :
        super(Dashboard, self).__init__()
        loadUi("dashboard.ui", self)
        self.actionVisualisasi.triggered.connect(self.visualisasiScr)
        self.actionInput_Data_Beban.triggered.connect(self.goToBeban)
        self.actionInput.triggered.connect(self.goToEntryBahan)

    def goToEntryBahan(self) :
        bahanDasar = EntryBahanDasar()
        widget.addWidget(bahanDasar)
        widget.setCurrentWidget(bahanDasar)
    def goToBeban(self) :
        beban = DataBeban()
        widget.addWidget(beban)
        widget.setCurrentWidget(beban)

    def visualisasiScr(self):
        visualisasi = Visualisasi()

        widget.addWidget(visualisasi)
        widget.setCurrentWidget(visualisasi)


class Visualisasi(QWidget) :
    def __init__(self) :
        super(Visualisasi, self).__init__()
        loadUi("visualisasi2.ui", self)
        self.tableWidget.setColumnWidth(1,164)
        self.tableWidget.setColumnWidth(2,250)
        self.tableWidget.setColumnWidth(3,168)
        self.getData()
        self.backButton.clicked.connect(self.backToMain)
    def backToMain(self) :
        main = Dashboard()
        widget.addWidget(main)
        widget.setCurrentWidget(main)
    def getData(self):

        url = 'http://127.0.0.1:8000/bahanDasar'
        
        res = (requests.get(url)).json()
        tablerow = 0
        self.tableWidget.setRowCount(len(res))
        for row in res:
            self.tableWidget.setRowHeight(tablerow,402/len(res))
            self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row['id'])))
            self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(str(row['nama'])))
            self.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(str(row['kuantitas'])))
            tablerow+=1


class DataBeban(QDialog) :
    def __init__(self) :
        super(DataBeban, self).__init__()
        loadUi("DataBeban.ui", self)
        self.pushButton.clicked.connect(self.backToMain)
        self.pushButton_2.clicked.connect(self.post_beban)
    def backToMain(self) :
        main = Dashboard()
        widget.addWidget(main)
        widget.setCurrentWidget(main)
    def post_beban(self) :
        url = 'http://127.0.0.1:8000/dataBeban'
        body = {
            "idBeban": self.lineEdit.text(),
            "tanggal": self.lineEdit_2.text(),
            "namaBeban": self.lineEdit_3.text(),
            "harga": self.lineEdit_4.text(),
            "kuantitas": self.lineEdit_5.text(),
            "satuan": self.lineEdit_6.text()
            }

        try :
            requests.post(url, json=body)
            QtWidgets.QMessageBox.about(self, 'Connection', 'Insert data success')

        except :
            QtWidgets.QMessageBox.about

class EntryBahanDasar(QDialog) :

    def __init__(self) :
        super(EntryBahanDasar, self).__init__()
        loadUi("EntryBahanDasar.ui", self)
        self.pushButton.clicked.connect(self.backToMain)
        self.pushButton_2.clicked.connect(self.postBahanDasar)
        
    def backToMain(self) :
        main = Dashboard()
        widget.addWidget(main)
        widget.setCurrentWidget(main)

    def postBahanDasar(self) :
        
        url = 'http://127.0.0.1:8000/bahan-dasar'
        body = {
            "id": self.lineEdit.text(),
            "nama": self.lineEdit_2.text(),
            "kuantitas": self.lineEdit_3.text()
            }

        try :
            requests.post(url, json=body)
            QtWidgets.QMessageBox.about(self, 'Connection', 'Insert data success')

        except :
            QtWidgets.QMessageBox.about(self, 'Connection', "Insert data Failed")
            self.close()

#  Login = QtWidgets.QWidget()
#     ui = Ui_Login()
#     ui.setupUi(Login)
#     Login.show()
app = QtWidgets.QApplication(sys.argv)
widget = QtWidgets.QStackedWidget()
login = Login()
# register = Register()



widget.addWidget(login)
# widget.addWidget(register)

widget.setCurrentIndex(0)
widget.show()

app.exec()