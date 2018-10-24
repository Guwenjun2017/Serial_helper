# -*- coding:utf-8 -*-

import serial


ser = serial.Serial("/dev/ttyUSB0", 9600, timeout=10) #linux系统使用com1口连接串行口
print(ser.name)
print(ser.port)
print(serial.tools.list_ports.comports())
ser.close()
