from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setFixedSize(400, 355)
        Form.setStyleSheet("QWidget {\n"
"background: #9f9f9f;\n"
"}\n"
"\n"
"QComboBox {\n"
"color: #ffffff; \n"
"background: #636363;\n"
"border: 2px solid #bcbcbc;\n"
"border-radius: 1px;\n"
"}\n"
"\n"
"QLineEdit {\n"
"color: #ffffff; \n"
"background: #636363;\n"
"border: 2px solid #bcbcbc;\n"
"border-radius: 1px;\n"
"}\n"
"\n"
"QLabel { \n"
"color: #ffffff; \n"
"}")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(20, 50, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(240, 50, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(240, 230, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.comboBox_2 = QtWidgets.QComboBox(Form)
        self.comboBox_2.setGeometry(QtCore.QRect(170, 230, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.comboBox_2.setFont(font)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.lineEdit_4 = QtWidgets.QLineEdit(Form)
        self.lineEdit_4.setGeometry(QtCore.QRect(20, 230, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(Form)
        self.lineEdit_5.setGeometry(QtCore.QRect(300, 100, 81, 20))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(Form)
        self.lineEdit_6.setGeometry(QtCore.QRect(300, 280, 81, 20))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_7 = QtWidgets.QLineEdit(Form)
        self.lineEdit_7.setGeometry(QtCore.QRect(300, 190, 81, 20))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_8 = QtWidgets.QLineEdit(Form)
        self.lineEdit_8.setGeometry(QtCore.QRect(240, 140, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lineEdit_8.setFont(font)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.lineEdit_9 = QtWidgets.QLineEdit(Form)
        self.lineEdit_9.setGeometry(QtCore.QRect(20, 140, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lineEdit_9.setFont(font)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(222, 140, 20, 41))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(15)
        self.label_4.setFont(font)
        self.label_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_4.setAutoFillBackground(False)
        self.label_4.setStyleSheet("QLabel { \n"
"color: #636363;\n"
"}")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(280, 100, 16, 16))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(15)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("QLabel { \n"
"color: #636363;\n"
"}")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(280, 190, 16, 16))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(15)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("QLabel { \n"
"color: #636363;\n"
"}")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(280, 280, 16, 16))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(15)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("QLabel { \n"
"color: #636363;\n"
"}")
        self.label_7.setObjectName("label_7")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(208, 50, 31, 39))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(15)
        self.label_3.setFont(font)
        self.label_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_3.setAutoFillBackground(False)
        self.label_3.setStyleSheet("QLabel { \n"
"color: #636363;\n"
"}")
        self.label_3.setTextFormat(QtCore.Qt.AutoText)
        self.label_3.setObjectName("label_3")
        self.pushButton_10 = QtWidgets.QPushButton(Form)
        self.pushButton_10.setGeometry(QtCore.QRect(370, 200, 16, 16))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_20 = QtWidgets.QPushButton(Form)
        self.pushButton_20.setGeometry(QtCore.QRect(370, 110, 16, 16))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.pushButton_20.setFont(font)
        self.pushButton_20.setObjectName("pushButton_20")
        self.pushButton_30 = QtWidgets.QPushButton(Form)
        self.pushButton_30.setGeometry(QtCore.QRect(370, 290, 16, 16))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.pushButton_30.setFont(font)
        self.pushButton_30.setObjectName("pushButton_30")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton_10.setText(_translate("Form", "⧉"))
        self.pushButton_20.setText(_translate("Form", "⧉"))
        self.pushButton_30.setText(_translate("Form", "⧉"))
        self.lineEdit.setPlaceholderText(_translate("Form", "%"))
        self.lineEdit_2.setPlaceholderText(_translate("Form", "N"))
        self.lineEdit_3.setPlaceholderText(_translate("Form", "%"))
        self.comboBox_2.setItemText(0, _translate("Form", "  +"))
        self.comboBox_2.setItemText(1, _translate("Form", "  -"))
        self.lineEdit_4.setPlaceholderText(_translate("Form", "N"))
        self.lineEdit_5.setPlaceholderText(_translate("Form", "N"))
        self.lineEdit_6.setPlaceholderText(_translate("Form", "N"))
        self.lineEdit_7.setPlaceholderText(_translate("Form", "%"))
        self.lineEdit_8.setPlaceholderText(_translate("Form", "N"))
        self.lineEdit_9.setPlaceholderText(_translate("Form", "N"))
        self.label_4.setText(_translate("Form", "в"))
        self.label_5.setText(_translate("Form", "="))
        self.label_6.setText(_translate("Form", "="))
        self.label_7.setText(_translate("Form", "="))
        self.label_3.setText(_translate("Form", " от"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
