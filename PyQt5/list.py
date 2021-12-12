import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QInputDialog, QListWidget , QMessageBox
from listForm import Ui_MainWindow

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window , self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        #load student
        self.loadStudents()
        
        #add new student
        self.ui.btnAdd.clicked.connect(self.addStudent)

        #edit student
        self.ui.btnEdit.clicked.connect(self.EditStudent)

        #delete student
        self.ui.btnRemove.clicked.connect(self.removeStudent)

        # up student
        self.ui.btnUp.clicked.connect(self.upStudent)

        # down student
        self.ui.btnDown.clicked.connect(self.downStudent)

        # sort student
        self.ui.btnSort.clicked.connect(self.sortStudents)

        # close
        self.ui.btnExit.clicked.connect(self.close)

    def loadStudents(self):
        listWidget = QListWidget()
        item = ['Mehmet' , 'Ali', 'Veli']
        listWidget.addItems(item)
        #    
        # #seçili getirme
        # self.ui.listItems.setCurrentRow(1)

    def addStudent(self):
        currentIndex = self.ui.listItems.currentRow()
        text , ok = QInputDialog.getText(self , 'New Student', 'Student Name')
        if ok and text is not None:
            self.ui.listItems.insertItem(currentIndex , text)

    def EditStudent(self):
        index = self.ui.listItems.currentRow()
        item = self.ui.listItems.item(index)

        if item is not None:
            text , ok = QInputDialog.getText(self , 'Edit Student' , 'Student Name' , item)
            if text and ok is not None:
                item.setText(text)

    def removeStudent(self):
        index = self.ui.listItems.currentRow()
        item = self.ui.listItems.item(index)

        if item is not None:
            return
        
        q = QMessageBox.question(self , "Remove Student" , "Do you want to remove student " + item.text() , QMessageBox.Yes | QMessageBox.No)
        if q == QMessageBox.Yes:
            item = self.ui.listItems.takeItem(index)
            del item

    def upStudent(self):
        index = self.ui.listItems.currentRow()
        if index >= 1:
            item = self.ui.listItems.takeItem(index)
            self.ui.listItems.insertItem(index-1 , item)
            self.ui.listItems.setCurrentItem(item)

    def downStudent(self):
        index = self.ui.listItems.currentRow()
        if index < self.ui.listItems.count() -1 :
            item = self.ui.listItems.takeItem(index)
            self.ui.listItems.insertItem(index+1 , item)
            self.ui.listItems.setCurrentItem(item)

    def sortStudents(self):
        self.ui.listItems.sortItems()

    def close(self):
        quit()

def app():
    app = QtWidgets.QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())
app()