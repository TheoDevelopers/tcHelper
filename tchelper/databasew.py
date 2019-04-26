"""Logic for DatabaseWindow"""

import gui.DatabaseWindow
from PySide2 import QtWidgets


class DatabaseWindow(QtWidgets.QDialog, gui.DatabaseWindow.Ui_DatabaseWindow):
    def __init__(self, parent=None):
        super(DatabaseWindow, self).__init__(parent)
        self.setupUi(self)
