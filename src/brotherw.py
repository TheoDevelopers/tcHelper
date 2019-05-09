"""Logic for BrotherWindow"""

import gui.BrotherWindow
from PySide2 import QtWidgets


class BrotherWindow(QtWidgets.QDialog, gui.BrotherWindow.Ui_BrotherWindow):
    def __init__(self, parent=None):
        super(BrotherWindow, self).__init__(parent)
        self.setupUi(self)
