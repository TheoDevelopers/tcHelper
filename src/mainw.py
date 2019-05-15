"""All of the logic for the MainWindow GUI"""

from PySide2.QtWidgets import QApplication
from PySide2 import QtWidgets
import gui.MainWindow as MainWindow  # Generated with QtDesigner
from brotherw import BrotherWindow
from databasew import DatabaseWindow
from congregationw import CongregationWindow
from outlinew import OutlineWindow
import sys


class MainWindow(QtWidgets.QMainWindow, MainWindow.Ui_MainWindow):
    """The main window of tcHelper when tcHelper starts

    From MainWindow all functions of tcHelper is accessed by the end user.

    """

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.center_on_screen()

        # TOOL BAR ACTIONS
        # Connects the tool-bar buttons to functions that are responsible
        # of opening the corresponding dialog.

        self.actionDatabase.triggered.connect(
            self.show_database_window)  # Database Manager
        self.actionBrothers.triggered.connect(
            self.show_brother_window)  # Brother Manager
        self.actionCongregation.triggered.connect(
            self.show_congregation_window)  # Congregation Manager
        self.actionTalks.triggered.connect(
            self.show_outline_window)  # Talk-Outline Manager

    def center_on_screen(self):
        """Center the main window on the user's screen at boot-up"""

        screen_resolution = QtWidgets.QDesktopWidget().screenGeometry()
        center_horizontal = ((screen_resolution.width() / 2) - (self.frameSize().width() / 2))
        center_vertical = ((screen_resolution.height() / 2) - (self.frameSize().height() / 2))
        self.move(center_horizontal, center_vertical)

    def show_database_window(self):
        """Method that opens the Database manager"""

        self.db_window = DatabaseWindow()
        self.db_window.show()

    def show_brother_window(self):
        """Method that opens the Brother manager"""

        self.bro_window = BrotherWindow()
        self.bro_window.show()

    def show_congregation_window(self):
        """Method that opens the Congregation manager"""

        self.congregation_window = CongregationWindow()
        self.congregation_window.show()

    def show_outline_window(self):
        """Method that opens the List manager"""

        self.outline_window = OutlineWindow()
        self.outline_window.show()


def run():
    """Construct the MainWindow"""

    app = QApplication(sys.argv)
    my_app = MainWindow()
    my_app.show()
    sys.exit(app.exec_())
