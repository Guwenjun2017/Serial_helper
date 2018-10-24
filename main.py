# -*- coding:utf-8 -*-

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
from serial_helper import Ui_MainWindow
import serial


class LayoutDemo(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(LayoutDemo, self).__init__(parent)
        self.setupUi(self)

    # 打开串口按钮按下时
    def open_serial_button_clicked(self):
        print("hello,world1")
        ser = serial.Serial()
        ser.port = self.serial_choose.currentText()
        ser.baudrate = self.baudrate.currentText()
        ser.bytesize = int(self.datasize.currentText())
        ser.paritybyte = self.checkbyte.currentText()
        ser.stopbits = int(self.stopbyte.currentText())

        print("hello,world2")
        self.serial_defined.setText(self.serial_choose.currentText())
        self.sendbytecount.setText(str(0))
        self.receivebytecount.setText(str(0))
        print("hello,world3")

    # 清空发送框按钮按下时，清空输入框
    def clear_send_button_clicked(self):
        self.sendcontent.clear()

    # 发送按钮按下时候，发送内容到接收框
    def send_button_clicked(self):
        #self.receivecontent.setText(self.sendcontent.toPlainText())
        self.receivecontent.append(self.sendcontent.toPlainText())
        num1 = int(self.sendbytecount.toPlainText()) + 1
        num2 = int(self.receivebytecount.toPlainText()) + 1
        self.sendbytecount.setText(str(num1))
        self.receivebytecount.setText(str(num2))

    # 自动发送按钮按下时，自动发送
    def auto_send_button_clicked(self):
        #for i in range(3):
        self.send_button_clicked


    # 清空计数按钮按下时，清空计数
    def clear_count_button_clicked(self):
        self.sendbytecount.setText(str(0))
        self.receivebytecount.setText(str(0))

    # 清空接收框按钮按下时，清空接收框
    def clear_receive_button_clicked(self):
        self.receivecontent.clear()


if __name__=="__main__":
    import sys 
    app = QApplication(sys.argv) 
    ui = LayoutDemo()

    # 连接事件与函数
    ui.clear_send_button.clicked.connect(ui.clear_send_button_clicked)
    ui.send_button.clicked.connect(ui.send_button_clicked)
    ui.auto_send_button.clicked.connect(ui.auto_send_button_clicked)
    ui.open_serial_button.clicked.connect(ui.open_serial_button_clicked)
    ui.clear_count_button.clicked.connect(ui.clear_count_button_clicked)
    ui.clear_receive_button.clicked.connect(ui.clear_receive_button_clicked)


    ui.show()
    sys.exit(app.exec_())
