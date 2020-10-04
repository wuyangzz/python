
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
import designer.demo as demo1
class Firstui(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=uic.loadUi('\\designer\\demo.ui')

if __name__=='__main__':
    #创建一个QApplication窗口
    app=QApplication(sys.argv)
    firstui=Firstui()
    firstui.ui.show()
    app.exit(app.exec_())
