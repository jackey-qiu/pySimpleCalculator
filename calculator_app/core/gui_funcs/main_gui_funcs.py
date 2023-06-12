import logging
import os
from pathlib import Path
from PyQt5 import QtGui
from PyQt5.QtCore import QSize

def append_after_cursor(lineEditObj, txt):
    #txt = pushButtonObj.text()
    if txt == '*':
        txt = '×'
    elif txt == '/':
        txt = '÷'
    pos = lineEditObj.cursorPosition()
    original_text_before_cursor = lineEditObj.text()[0:pos]
    original_text_after_cursor = lineEditObj.text()[pos:]
    new_text_after_appending_txt = original_text_before_cursor + txt + original_text_after_cursor
    lineEditObj.setText(new_text_after_appending_txt)
    if txt=='()':
        lineEditObj.setCursorPosition(len(original_text_before_cursor + txt)-1)
    else:
        lineEditObj.setCursorPosition(len(original_text_before_cursor + txt))

def calculate_result(lineEditObj):
    try:
        original_text = lineEditObj.text()
        decoded_text = original_text.replace('×','*')
        decoded_text = decoded_text.replace('÷','/')
        result = eval(decoded_text)
        lineEditObj.setText(str(round(result,8)))
        logging.getLogger('app.operation').info(\
                                        f'Succeed to calculate the expression of {original_text} = {result}')
    except:
        lineEditObj.setText('ERROR')
        logging.getLogger('app.operation').exception(f'Fail to calculate the expression of {lineEditObj.text()}')

def clear_lineEdit_field(lineEditObj):
    lineEditObj.setText('')

def signal_slot_connection(self):
    self.pushButton_n0.clicked.connect(lambda: append_after_cursor(self.lineEdit_result, '0'))
    self.pushButton_n1.clicked.connect(lambda: append_after_cursor(self.lineEdit_result, '1'))
    self.pushButton_n2.clicked.connect(lambda: append_after_cursor(self.lineEdit_result, '2'))
    self.pushButton_n3.clicked.connect(lambda: append_after_cursor(self.lineEdit_result, '3'))
    self.pushButton_n4.clicked.connect(lambda: append_after_cursor(self.lineEdit_result, '4'))
    self.pushButton_n5.clicked.connect(lambda: append_after_cursor(self.lineEdit_result, '5'))
    self.pushButton_n6.clicked.connect(lambda: append_after_cursor(self.lineEdit_result, '6'))
    self.pushButton_n7.clicked.connect(lambda: append_after_cursor(self.lineEdit_result, '7'))
    self.pushButton_n8.clicked.connect(lambda: append_after_cursor(self.lineEdit_result, '8'))
    self.pushButton_n9.clicked.connect(lambda: append_after_cursor(self.lineEdit_result, '9'))
    self.pushButton_pt.clicked.connect(lambda: append_after_cursor(self.lineEdit_result, '.'))
    self.pushButton_pct.clicked.connect(lambda: append_after_cursor(self.lineEdit_result, '%'))
    self.pushButton_div.clicked.connect(lambda: append_after_cursor(self.lineEdit_result, '/'))
    self.pushButton_mltp.clicked.connect(lambda: append_after_cursor(self.lineEdit_result, '*'))
    self.pushButton_minus.clicked.connect(lambda: append_after_cursor(self.lineEdit_result, '-'))
    self.pushButton_plus.clicked.connect(lambda: append_after_cursor(self.lineEdit_result, '+'))
    self.pushButton_res.clicked.connect(lambda: calculate_result(self.lineEdit_result))
    self.pushButton_c.clicked.connect(lambda: clear_lineEdit_field(self.lineEdit_result))
    self.pushButton_group.clicked.connect(lambda: append_after_cursor(self.lineEdit_result, '()'))

def set_button_icons(self):
    root = Path(__file__).parent.parent.parent/ "res" / "icons"
    self.setWindowIcon(QtGui.QIcon(str(root/ "calculator.png")))
    for i in range(0,10):
        if os.path.exists(str(root/'{}.png'.format(i))):
            icon = QtGui.QIcon(str(root/'{}.png'.format(i)))
            getattr(self, f'pushButton_n{i}').setText('')
            getattr(self, f'pushButton_n{i}').setIcon(icon)
            getattr(self, f'pushButton_n{i}').setIconSize(QSize(50,50))