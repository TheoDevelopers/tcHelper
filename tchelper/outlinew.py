"""Logic for OutlineWindow"""

import gui.OutlineWindow
from PySide2 import QtWidgets


class OutlineWindow(QtWidgets.QDialog, gui.OutlineWindow.Ui_OutlineWindow):
    def __init__(self, parent=None):
        super(OutlineWindow, self).__init__(parent)
        self.setupUi(self)
