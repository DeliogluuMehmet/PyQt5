import sys
from PyQt5 import QtWidgets
from radio_button_Form import Ui_MainWindow

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window , self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #seçili olarak açar
        self.ui.rdTurkiye.setChecked(True)
        self.ui.rdUni.setChecked(True)

        self.ui.rdTurkiye.toggled.connect(self.onClickedUlke)
        self.ui.rdAzerbaycan.toggled.connect(self.onClickedUlke)
        self.ui.rdAlmanya.toggled.connect(self.onClickedUlke)
        self.ui.rdAmerika.toggled.connect(self.onClickedUlke)

        self.ui.rdilkokul.toggled.connect(self.onClickedEgitim)
        self.ui.rdLise.toggled.connect(self.onClickedEgitim)
        self.ui.rdUni.toggled.connect(self.onClickedEgitim)
        self.ui.rdYL.toggled.connect(self.onClickedEgitim)

        self.ui.UlkeSec.clicked.connect(self.getSelectedUlke)
        self.ui.EgitimSec.clicked.connect(self.getSelectedEgitim)

    #tıklanan elemanı alma
    def onClickedUlke(self):
        rb = self.sender()
        if rb.isChecked():
            print('Seçilen Ülke: ' + rb.text())
    
    def onClickedEgitim(self):
        rb = self.sender()
        if rb.isChecked():
            print('Seçilen Eğitim: ' + rb.text())

    def getSelectedUlke(self):
        items = self.ui.grupUlke.findChildren(QtWidgets.QRadioButton)
        for rb in items:
            if rb.isChecked():
                self.ui.lblResultUlke.setText("Seçilen Ülke: " + rb.text())
    
    def getSelectedEgitim(self):
        items = self.ui.grupEgitim.findChildren(QtWidgets.QRadioButton)
        for rb in items:
            if rb.isChecked():
                self.ui.lblResultEgitim.setText("Seçilen Eğitim: " + rb.text())

def app():
    app = QtWidgets.QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())
app()