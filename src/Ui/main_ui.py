import sys
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QDialog, QApplication, QMainWindow, QMessageBox, QWidget
from PyQt6.uic import loadUi
from dashboard import Ui_MainWindow

class Login(QWidget) :
    def __init__(self):
        super(Login, self).__init__()
        loadUi("login.ui", self)
        self.pushButton.clicked.connect(self.login)
        self.pushButton_2.clicked.connect(self.goToRegister)
    def goToRegister(self) :
        register = Register()
        widget.addWidget(register)
        widget.setCurrentIndex(widget.currentIndex()+1)
    def login(self) :
        print(self.lineEdit.text())
        print(self.lineEdit_2.text())
        if (True) :
            MainWindow = Dashboard()
            widget.addWidget(MainWindow)
            widget.setCurrentIndex(widget.currentIndex()+1)
        


class Register(QWidget) :
    def __init__(self) :
        super(Register, self).__init__()
        loadUi("register_w.ui", self)
        self.pushButton.clicked.connect(self.goToLogin)
    def goToLogin(self) :
        widget.setCurrentIndex(0)

class Dashboard(QMainWindow) :
    def __init__(self) :
        super(Dashboard, self).__init__()
        loadUi("dashboard.ui", self)


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