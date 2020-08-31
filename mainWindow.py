

from detailUI import *
from PyQt5.QtGui import QPalette, QBrush, QPixmap
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QMessageBox, QPushButton
from PyQt5 import QtCore

class main_UI(QWidget):
    def __init__(self):
        super(main_UI, self).__init__()
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowTitle("os")
        self.setMinimumSize(1920,1080)
        self.setMaximumSize(1920,1080)
        palette = QPalette()
        palette.setBrush(QPalette.Background, QBrush(QPixmap("详览界面.jpg")))
        self.setPalette(palette)
        self.btn = QPushButton("",self)
        self.btn.setGeometry(260,80,260,130)
        self.btn.setStyleSheet(
                                 "background:transparent;")
        # self.btn.clicked.connect(self.show_msg)
        self.setAcceptDrops(True)





if __name__ == "__main__":
    app = QApplication(sys.argv)

    parent = main_UI()
    child = detail_UI()
    parent.btn.clicked.connect(child.show)

    parent.show()


    sys.exit(app.exec())