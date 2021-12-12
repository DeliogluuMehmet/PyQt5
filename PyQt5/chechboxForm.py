import sys
from PyQt5 import QtWidgets
from checkbox import Ui_MainWindow

class myApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(myApp , self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.cbKitap.stateChanged.connect(self.show_state)
        self.ui.cbSinema.stateChanged.connect(self.show_state)
        self.ui.cbSpor.stateChanged.connect(self.show_state)

        self.ui.btnSecilenAlDersler.clicked.connect(self.getAllDersler)
        self.ui.btnSecilenAlHobiler.clicked.connect(self.getAllHobiler)
   
    #checkbox'ta seçili olanları push edince seçili olanları gösterir
    def getAllHobiler(self):
        result = ''
        items = self.ui.grupHobiler.findChildren(QtWidgets.QCheckBox)
        for cb in items:
            if cb.isChecked():
                result += cb.text() + '\n'
        self.ui.lblResultHobiler.setText(result)
    def getAllDersler(self):
        result = ''
        items = self.ui.grupDersler.findChildren(QtWidgets.QCheckBox)
        for cb in items:
            if cb.isChecked():
                result += cb.text() + '\n'
        self.ui.lblResultDersler.setText(result)

    #checkboxlardan gelen değerlerin sonucunu yazar(seçili mi? gibi)
    def show_state(self , value):
        cb = self.sender()
        print(value)
        print(cb.text())
        print(cb.isChecked())

def app():
    app = QtWidgets.QApplication(sys.argv)
    win = myApp()
    win.show()
    sys.exit(app.exec_())
app()