import sys
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QDialog, QApplication, QMainWindow, QMessageBox, QWidget
from PyQt6.uic import loadUi
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
    # def login(self) :
    #     print(self.lineEdit.text())
    #     print(self.lineEdit_2.text())
    #     if (True) :
    #         MainWindow = Dashboard()
    #         # widget.insertWidget(MainWindow)
    #         widget.addWidget(MainWindow)
    #         widget.setCurrentWidget(MainWindow)
    #         # widget.setCurrentIndex(widget.currentIndex()+1)
    def login(self) :
        url = 'http://localhost:8000/login'
        body = {
            "username": self.lineEdit.text(),
            "password": self.lineEdit_2.text()
            }
        req = requests.post(url, json=body)

        if (req.status_code == 200) :
            print(self.lineEdit.setText(''))
            print(self.lineEdit_2.setText(''))
            MainWindow = Dashboard()
            widget.addWidget(MainWindow)
            widget.setCurrentWidget(MainWindow)
        else :
            QtWidgets.QMessageBox.about(self, 'Connection', "Invalid Credentials !!")


class Register(QWidget) :
    def __init__(self) :
        super(Register, self).__init__()
        loadUi("register_w.ui", self)
        self.pushButton.clicked.connect(self.goToLogin)
        self.pushButton_2.clicked.connect(self.registerRequest)
    def registerRequest(self) :
        url = 'http://localhost:8000/register'
        body = {
            "username": self.lineEdit_3.text(),
            "password": self.lineEdit_4.text(),
            "email" : self.lineEdit.text(),
            "namaLengkap" : self.lineEdit_2.text(),
            "cabang" : self.lineEdit_9.text(),
            "jabatan" : self.lineEdit_10.text(),
            "role" : self.lineEdit_11.text()
            }
        req = requests.post(url, json=body)

        if (req.status_code == 200) :
            self.lineEdit.setText('')
            self.lineEdit_2.setText('')
            self.lineEdit_3.setText('')
            self.lineEdit_4.setText('')
            self.lineEdit_9.setText('')
            self.lineEdit_10.setText('')
            self.lineEdit_11.setText('')
            QtWidgets.QMessageBox.about(self, 'Connection', "User Registered !!")
            
        else :
            QtWidgets.QMessageBox.about(self, 'Connection', "Failed")
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
        self.actionInput_Data_Pengeluaran.triggered.connect(self.goToPengeluaran)
        self.actionData_Laba_Rugi.triggered.connect(self.goToLabaRugi)
        self.actionData_Keuangan.triggered.connect(self.goToKeuangan)
        self.actionLogout.triggered.connect(self.logout)
        self.actionInput_Data_Pemasukan.triggered.connect(self.goToPemasukan)
    def logout(self) :
        widget.setCurrentIndex(0)
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
    def goToPengeluaran(self) :
        pengeluaran = InputDataPengeluaran()

        widget.addWidget(pengeluaran)
        widget.setCurrentWidget(pengeluaran)
    def goToLabaRugi(self) :
        labarugi = LabaRugi()

        widget.addWidget(labarugi)
        widget.setCurrentWidget(labarugi)
        
    def goToKeuangan(self) :
        keuangan = DataKeuangan()

        widget.addWidget(keuangan)
        widget.setCurrentWidget(keuangan)
    def goToPemasukan(self) :
        pemasukan = InputDataPemasukan()
        widget.addWidget(pemasukan)
        widget.setCurrentWidget(pemasukan)
        


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
class DataKeuangan(QWidget) :
    def __init__(self) :
        super(DataKeuangan, self).__init__()
        loadUi("datakeuangan.ui", self)
        self.backButton.clicked.connect(self.backToMain)
    def backToMain(self) :
        main = Dashboard()
        widget.addWidget(main)
        widget.setCurrentWidget(main)
class LabaRugi(QWidget) :
    def __init__(self) :
        super(LabaRugi, self).__init__()
        loadUi("labarugi.ui", self)
        self.backButton.clicked.connect(self.backToMain)
    def backToMain(self) :
        main = Dashboard()
        widget.addWidget(main)
        widget.setCurrentWidget(main)

class InputDataPengeluaran(QWidget):
    def __init__(self) :
        super(InputDataPengeluaran, self).__init__()
        loadUi("pengeluaran.ui", self)
        self.pushButton_3.clicked.connect(self.InsertData)
        self.backButton.clicked.connect(self.backToMain)
    def backToMain(self) :
        main = Dashboard()
        widget.addWidget(main)
        widget.setCurrentWidget(main)
    def InsertData(self):

        url = 'http://localhost:8000/dataKeuangan/supplyBahanDasar'

        body = {
            "idSupplier": self.lineEdit.text(),
            "idBahan": self.lineEdit_2.text(),
            "harga": self.lineEdit_3.text(),
            "kuantitas": self.lineEdit_4.text(),
            "satuan": self.lineEdit_5.text()
        }

        bodyFix = {
            "idSupplier": int(body["idSupplier"]),
            "idBahan": int(body["idBahan"]),
            "harga": int(body["harga"]),
            "kuantitas": int(body["kuantitas"]),
            "satuan": body["satuan"],
        }

        try :
            print(bodyFix)
            print(type(bodyFix["idSupplier"]))
            requests.post(url, json=bodyFix)
            QtWidgets.QMessageBox.about(self, 'Connection', 'data pengeluaran berhasil ditambahkan')
            
            
        except :
            QtWidgets.QMessageBox.about(self, 'Connection', 'data pengeluaran gagal ditambahkan')


class InputDataPemasukan(QWidget) :
    def __init__(self) :
        super(InputDataPemasukan, self).__init__()
        loadUi("inputDataPemasukan.ui", self)
        self.pushButton_2.clicked.connect(self.InsertData)
        self.backButton.clicked.connect(self.backToMain)
    def backToMain(self) :
        main = Dashboard()
        widget.addWidget(main)
        widget.setCurrentWidget(main)
    def InsertData(self):
        url = 'http://localhost:8000/dataKeuangan/pemasukan'

        body = {
            "metodePembayaran": self.lineEdit.text(),
            "idPesanan": int(self.lineEdit_4.text()),
            
        }

        try :
            requests.post(url, json=body)
            QtWidgets.QMessageBox.about(self, 'Connection', 'Success')
            # print('sudah disubmit')

            # self.close()
        except :
            QtWidgets.QMessageBox.about(self, 'Connection', 'Failed')
            # self.close()   
            # print('gagal')


app = QtWidgets.QApplication(sys.argv)
widget = QtWidgets.QStackedWidget()
login = Login()

widget.addWidget(login)
# widget.addWidget(register)

widget.setCurrentIndex(0)
widget.show()

app.exec()