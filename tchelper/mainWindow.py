import gui.MainWindow
from PySide2 import QtWidgets


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    test = gui.MainWindow.Ui_MainWindow()
    sys.exit(app.exec_())
