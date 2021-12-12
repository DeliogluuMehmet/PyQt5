import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
from tableForm import Ui_MainWindow

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window , self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.loadProducts() 
        self.ui.btnSave.clicked.connect(self.saveProduct)
        self.ui.tableWidget.doubleClicked.connect(self.doubleClick)

    def loadProducts(self):
        #dinamik bilgileri yükleme
        product = [{'name': 'Samsung S5' , 'price': 2000},
                {'name': 'Samsung S6' , 'price': 3000},
                {'name': 'Samsung S7' , 'price': 4000},
                {'name': 'Samsung S8' , 'price': 5000}]

        self.ui.tableWidget.setRowCount(len(product))
        self.ui.tableWidget.setColumnCount(2)
        self.ui.tableWidget.setHorizontalHeaderLabels(('Name' , 'Price'))
        self.ui.tableWidget.setColumnWidth(0,200)
        self.ui.tableWidget.setColumnWidth(1,100)

        rowIndex = 0
        for i in product:
            self.ui.tableWidget.setItem(rowIndex,0 , QTableWidgetItem(i['name']))
            self.ui.tableWidget.setItem(rowIndex,1 , QTableWidgetItem(str(i['price'])))

            rowIndex += 1

    def saveProduct(self):
        name = self.ui.txtName.text()
        price = self.ui.txtPrice.text()

        if name and price is not None:
            rowCount = self.ui.tableWidget.rowCount()
            print(rowCount)
            self.ui.tableWidget.insertRow(rowCount)
            self.ui.tableWidget.setItem(rowCount,0 , QTableWidgetItem(name))
            self.ui.tableWidget.setItem(rowCount,1 , QTableWidgetItem(price))

    #bilgileri okuma
    def doubleClick(self):
        for item in self.ui.tableWidget.selectedItems():
            print(item.row() , item.column() , item.text())

def app():
    app = QtWidgets.QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())
app()