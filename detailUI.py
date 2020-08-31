
import sys
import threading
import time
from tkinter.commondialog import Dialog

from PyQt5.QtCore import pyqtSignal, QEventLoop, QTimer, pyqtSlot, QObject
from PyQt5.QtGui import QPalette, QBrush, QPixmap, QTextCursor
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QMessageBox, QDialog, QTextEdit
from PyQt5 import QtCore, QtGui

import tools


class Stream(QObject):
    txt_signal = pyqtSignal(str)

    def write(self, text):
        self.txt_signal.emit(str(text))
class detail_UI(QDialog):



    def __init__(self):
        super(detail_UI, self).__init__()

        sys.stdout = Stream(txt_signal = self.onUpdateText)
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowTitle("监测数据")
        self.setMinimumSize(800,600)
        self.setMaximumSize(800,600)
        self.process = QTextEdit(self,readOnly = True)
        self.process.ensureCursorVisible()
        self.process.setGeometry(0,0,800,600)
        t = threading.Thread(target=tools.get_detail, args=())
        t.start()




        # sys.stdout = EmittingStr(textWritten=self.outputWritten)
        # sys.stderr = EmittingStr(textWritten=self.outputWritten)
        self.setAcceptDrops(True)
    # def printHello(self):
    #     AT_dic = {
    #         "AT1": '0104001A0001100D',  # 获取A相电流值报文
    #         "AT2": '01040014000171CE',  # 获取A相电压值
    #         "AT3": '0104010000013036',  # 获取A相电压总谐波含量
    #         "AT4": '010401030001C036',  # 获取A相电压奇次谐波含量
    #         "AT5": '010401090001E034',  # 获取A相电流总谐波含量
    #         "AT6": '0104011200019033',  # 获取A相电流奇次谐波含量
    #     }
    #     # Func_Serial_Info()   #初始化串口
    #     while True:
    #         for key in AT_dic:
    #             # Flag = True  # 标志位，超时为False
    #             # SEND_DATA = bytes.fromhex(AT_dic[key])
    #             # Func_Send_Data(SEND_DATA)
    #             # # start_time = time.time()
    #             # # while Flag:
    #             # recv = Func_Receive_Data()
    #             # print("recv:", recv)
    #             #     # cost_time = time.time() - start_time
    #             #     # print(time)
    #             #     # if cost_time>2.0:
    #             #     #     Flag = False
    #             #     #     print("获取数据超时！")
    #             # # if len:
    #             # #     continue
    #             # e_recv = Func_Handle_Recv()
    #             # print("e_recv:", e_recv)
    #             print("hello")
    #             if key == "AT1":
    #                 time.sleep(1)
    #                 print("A相电流值")
    #             elif key == "AT2":
    #                 time.sleep(1)
    #                 print("A相电压值")
    #             elif key == "AT3":
    #                 time.sleep(1)
    #                 print("A相电压总谐波含量")
    #             elif key == "AT4":
    #                 time.sleep(1)
    #                 print("A相电压奇次谐波含量")
    #             elif key == "AT5":
    #                 time.sleep(1)
    #                 print("A相电流总谐波含量")
    #             elif key == "AT6":
    #                 time.sleep(1)
    #                 print("A相电流奇次谐波含量")

    def onUpdateText(self,text):
        cursor = self.process.textCursor()
        cursor.movePosition(QTextCursor.End)
        cursor.insertText(text)
        self.process.setTextCursor(cursor)
        self.process.ensureCursorVisible()




    # def write(self,s):
    #     self.txt_signal.emit(s)
    # @pyqtSlot(str)
    # def write2Textbox(self,text):
    #     self.text.append(text)

    # def outputWritten(self, text):
    #     # self.textEdit.clear()
    #     cursor = self.textEdit.textCursor()
    #     cursor.movePosition(QtGui.QTextCursor.End)
    #     cursor.insertText(text)
    #     self.textEdit.setTextCursor(cursor)
    #     self.textEdit.ensureCursorVisible()
#
# class EmittingStr(QtCore.QObject):
#     textWritten = QtCore.pyqtSignal(str)  # 定义一个发送str的信号
#
#     def write(self, text):
#         self.textWritten.emit(str(text))
#         loop = QEventLoop()
#         QTimer.singleShot(1000, loop.quit)
#         loop.exec_()