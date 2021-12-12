from PyQt5 import QtWidgets
import sys
from calculator import Ui_UI_MainWindow

class myApp(QtWidgets.QMainWindow):

    def __init__(self):
        super(myApp , self).__init__()
        self.ui = Ui_UI_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_toplama.clicked.connect(self.hesapla)
        self.ui.btn_cikarma.clicked.connect(self.hesapla)
        self.ui.btn_carpma.clicked.connect(self.hesapla)
        self.ui.btn_bol.clicked.connect(self.hesapla)

    def hesapla(self):
        sender = self.sender().text()
        result = 0
        
        if sender == 'Toplam':
            result = int(self.ui.txt_sayi1.text()) + int(self.ui.txt_sayi2.text())
        elif sender == 'Çıkarma':
            result = int(self.ui.txt_sayi1.text()) - int(self.ui.txt_sayi2.text())
        elif sender == 'Çarpma':
            result = int(self.ui.txt_sayi1.text()) * int(self.ui.txt_sayi2.text())
        elif sender == 'Bölme':
            result = int(self.ui.txt_sayi1.text()) / int(self.ui.txt_sayi2.text())
        
        self.ui.label_3.setText('Sonuç: ' + str(result))

def app():
    app = QtWidgets.QApplication(sys.argv)
    win = myApp()
    win.show()
    sys.exit(app.exec_())
app()