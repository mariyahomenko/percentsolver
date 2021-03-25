from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
import sys
from ui import Ui_Form
from decimal import Decimal

app = QtWidgets.QApplication(sys.argv)
Form = QtWidgets.QWidget()
ui = Ui_Form()
ui.setupUi(Form)
Form.show()


def i():
    a = ui.lineEdit.text()
    b = ui.lineEdit_2.text()
    try:
        if a != '' and b != '':
            c = Decimal(b) / Decimal(100) * Decimal(a)
            ui.lineEdit_5.setText(str(c))
        else:
            ui.lineEdit_5.setText('')
    except:
        ui.lineEdit_5.setText('wrong')

def ii():
    a = ui.lineEdit_9.text()
    b = ui.lineEdit_8.text()
    try:
        if a != '' and b != '':
            c = Decimal(100) / (Decimal(b) / Decimal(a))
            ui.lineEdit_7.setText(str(c))
        else:
            ui.lineEdit_7.setText('')
    except:
        ui.lineEdit_7.setText('wrong')

def iii():
    z = ui.comboBox_2.currentText()
    a = ui.lineEdit_4.text()
    b = ui.lineEdit_3.text()
    try:
        if a != '' and b != '':
            if z == '  +':
                c = ((Decimal(a) / Decimal(100)) * Decimal(b)) + Decimal(a)
                ui.lineEdit_6.setText(str(c))
            elif z == '  -':
                c = Decimal(a) - (Decimal(a) / Decimal(100) * Decimal(b))
                ui.lineEdit_6.setText(str(c))
        else:
            ui.lineEdit_6.setText('')
    except:
        ui.lineEdit_6.setText('wrong')

def copy(num):
    cb = QApplication.clipboard()
    cb.clear(mode=cb.Clipboard)
    cb.setText(num, mode=cb.Clipboard)


ui.lineEdit.textChanged.connect(lambda: i())
ui.lineEdit_2.textChanged.connect(lambda: i())
ui.lineEdit_9.textChanged.connect(lambda: ii())
ui.lineEdit_8.textChanged.connect(lambda: ii())
ui.lineEdit_4.textChanged.connect(lambda: iii())
ui.lineEdit_3.textChanged.connect(lambda: iii())
ui.comboBox_2.currentTextChanged.connect(lambda: iii())

ui.pushButton_20.clicked.connect(lambda: copy(ui.lineEdit_5.text()))
ui.pushButton_10.clicked.connect(lambda: copy(ui.lineEdit_7.text()))
ui.pushButton_30.clicked.connect(lambda: copy(ui.lineEdit_6.text()))


sys.exit(app.exec_())

