import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import QDate , QTime , QDateTime
from date_time_Form import Ui_MainWindow

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window , self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btnCalculate.clicked.connect(self.calculate)

    def calculate(self):
        start = self.ui.dateStart.date()
        end = self.ui.dateFinish.date()
        print(start , end)

        print('Days in month: {0}' .format(start.daysInMonth()))
        print('Days in year: {0}'.format(start.daysInYear()))

        print('Total days: {0}'.format(start.daysTo(end)))

        now = QDate.currentDate()
        print('Total days from now: {0}'.format(start.daysTo(now)))

def app():
    app = QtWidgets.QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())
app()