import sys
import requests
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from currency_converter import CurrencyConverter
from ui import Ui_MainWindow


class CurrencyConv(QtWidgets.QMainWindow):
    def __init__(self):
        super(CurrencyConv, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_UI()

    def init_UI(self):
        self.setWindowTitle('Обмен валют')
        self.setWindowIcon(QIcon('icon_conv2.png'))
        self.ui.input_cur.setPlaceholderText('Отдаю')
        self.ui.input_sum.setPlaceholderText('Сумма')
        self.ui.output_cur.setPlaceholderText('Получаю')
        self.ui.output_sum.setPlaceholderText('Результат')
        self.ui.pushButton.clicked.connect(self.converter)

    def converter(self):
        input_cur = self.ui.input_cur.text().upper()
        output_cur = self.ui.output_cur.text().upper()
        input_sum = int(self.ui.input_sum.text())
        c = CurrencyConverter()
        output_sum = round(c.convert(input_sum, '%s' % (input_cur), '%s' % (output_cur)), 2)
        self.ui.output_sum.setText(str(output_sum))


app = QtWidgets.QApplication([])
application = CurrencyConv()
application.show()
sys.exit(app.exec())