import sys
# 引用生成的py文件 py
import day2.designer.VectorFlowMapping as vector
# 引用组件
from PyQt5.QtWidgets import QApplication, QMainWindow

# 设置主函数 py
if __name__ == '__main__':
    # 代表整个应用程序
    app = QApplication(sys.argv)
    # 创建一个mainWindow对象
    mainWindow = QMainWindow()
    # 引用导出的py文件中的Ui_MainWindow
    ui = vector.Ui_MainWindow()
    # 调用vector中的ui组件
    ui.setupUi(mainWindow)
    # 显示窗口
    mainWindow.show()
    # 执 行
    sys.exit(app.exec_())
