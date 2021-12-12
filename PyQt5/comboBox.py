import sys
from PyQt5 import QtWidgets
from comboBox_Form import Ui_MainWindow

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window , self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    # default olarak box'ta gelir
        # combo = self.ui.cbSehirler
        # combo.addItem('Ankara')
        # combo.addItem('Antalya')
        # combo.addItem('İstanbul')
        # combo.addItem('İzmir')
        #combo.addItems(['Hatay', 'Adana' , 'Muş'])

        self.ui.GetItem.clicked.connect(self.GetItem)
        self.ui.LoadItems.clicked.connect(self.LoadItems)
        self.ui.ClearItem.clicked.connect(self.ClearItems)

        #seçili olanın int değerini getirir
        self.ui.cbSehirler.currentIndexChanged.connect(self.selectedChangedIndex)
        #seçili olanın str bilgisini getir
        self.ui.cbSehirler.currentIndexChanged[str].connect(self.selectedChangedText)

    # veritabanından çeker ve box'a atar
    def LoadItems(self):
        sehirler = ['Hatay', 'Adana' , 'Muş' , 'Ankara' , 'Antalya' , 'İstanbul' , 'İzmir']

        self.ui.cbSehirler.addItems(sehirler)

    def GetItem(self):
        print(self.ui.cbSehirler.currentText())
        print(self.ui.cbSehirler.currentIndex())

        count = self.ui.cbSehirler.count()
        for index in range(count):
            print(self.ui.cbSehirler.itemText(index))

    # itemleri temizler
    def ClearItems(self):
        self.ui.cbSehirler.clear()

    #o an seçilen elemanın indexini alır
    def selectedChangedIndex(self , index):
        print(index)
    
    def selectedChangedText(self , text):
        print(text)

def app():
    app = QtWidgets.QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())
app()