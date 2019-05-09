"""Logic for CongregationWindow"""

import gui.CongregationWindow
from PySide2 import QtWidgets


class CongregationWindow(QtWidgets.QDialog,
                         gui.CongregationWindow.Ui_CongregationWindow):

    def __init__(self, parent=None):
        super(CongregationWindow, self).__init__(parent)
        self.setupUi(self)
