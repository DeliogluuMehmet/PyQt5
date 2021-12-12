import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from messageBox_Form import Ui_MainWindow

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window , self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btnExit.clicked.connect(self.showDialog)

    def showDialog(self):

        result = QMessageBox.question(self , 'Close Application' , 'Are you Sure?' , QMessageBox.Ok | QMessageBox.Cancel | QMessageBox.Ignore , QMessageBox.Cancel)
        if result == QMessageBox.Ok:
            print('Yes Clicked')
            QtWidgets.qApp.quit()
        else:
            print('No Clicked')

        # msg = QMessageBox()
        # msg.setWindowTitle('Close Application')
        # msg.setText('Are you Sure?')
        # # msg.setIcon(QMessageBox.Question)
        # msg.setIcon(QMessageBox.Warning)
        # msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel | QMessageBox.Ignore)
        # # msg.setDefaultButton(QMessageBox.Ok)
        # msg.setDefaultButton(QMessageBox.Ok)
        # msg.setDetailedText('details....')
        # msg.buttonClicked.connect(self.popup_button)

        # x = msg.exec_()
        # print(x)

    #açılan ikinci pencerenin detayları
    # def popup_button(self , i):
    #     print(i.text())

    #     if i.text() == 'Ok':
    #         print('Okey...')
    #         QtWidgets.qApp.quit()
    #     elif i.text() == 'Cancel':
    #         print('Okey...')
    #     else:
    #         print('Ignore...')

def app():
    app = QtWidgets.QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())
app()