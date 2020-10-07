import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtGui import QIcon


# 窗口主类
class FirstMainWin(QMainWindow):
    i = 1

    # 初始化窗口函数
    def __init__(self):
        # 继承父类方法
        super(FirstMainWin, self).__init__()
        self.setWindowTitle('我的第一个主窗口程序')
        self.resize(300, 300)
        # 设置一个窗口的下提示框
        self.status = self.statusBar()
        self.status.showMessage("只存在5s的消息")
        # 新建一个按钮
        self.button1 = QPushButton("切换状态栏消息")
        self.button1.setText("切换状态栏")
        # 按钮绑定事件
        self.button1.clicked.connect(self.OnsetBarText)
        layout = QVBoxLayout()
        layout.addWidget(self.button1)
        mainFrame = QWidget()
        mainFrame.setLayout(layout)
        self.setCentralWidget(mainFrame)

    def OnsetBarText(self):
        sender = self.sender()
        print(sender.text() + ' 按钮被按下')
        self.status.showMessage("切换状态：" )



if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('pyqt5-master/src/controls/images/doc.ico'))

    main = FirstMainWin()
    main.show()
    sys.exit(app.exec_())
