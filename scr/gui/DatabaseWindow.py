# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DatabaseWindow.ui',
# licensing of 'DatabaseWindow.ui' applies.
#
# Created: Fri Apr 26 00:08:33 2019
#      by: pyside2-uic  running on PySide2 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_DatabaseWindow(object):
    def setupUi(self, DatabaseWindow):
        DatabaseWindow.setObjectName("DatabaseWindow")
        DatabaseWindow.resize(144, 128)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(DatabaseWindow.sizePolicy().hasHeightForWidth())
        DatabaseWindow.setSizePolicy(sizePolicy)
        DatabaseWindow.setSizeGripEnabled(False)
        self.gridLayout = QtWidgets.QGridLayout(DatabaseWindow)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_3 = QtWidgets.QPushButton(DatabaseWindow)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 2, 2, 1, 1)
        self.pushButton = QtWidgets.QPushButton(DatabaseWindow)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 2, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(DatabaseWindow)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 1, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 3, 1, 1)

        self.retranslateUi(DatabaseWindow)
        QtCore.QMetaObject.connectSlotsByName(DatabaseWindow)

    def retranslateUi(self, DatabaseWindow):
        DatabaseWindow.setWindowTitle(QtWidgets.QApplication.translate("DatabaseWindow", "Database", None, -1))
        self.pushButton_3.setToolTip(QtWidgets.QApplication.translate("DatabaseWindow", "Load a backup.", None, -1))
        self.pushButton_3.setText(QtWidgets.QApplication.translate("DatabaseWindow", "Load Backup", None, -1))
        self.pushButton.setToolTip(QtWidgets.QApplication.translate("DatabaseWindow", "Create a new database.", None, -1))
        self.pushButton.setText(QtWidgets.QApplication.translate("DatabaseWindow", "New Database", None, -1))
        self.pushButton_2.setToolTip(QtWidgets.QApplication.translate("DatabaseWindow", "Backup your data.", None, -1))
        self.pushButton_2.setText(QtWidgets.QApplication.translate("DatabaseWindow", "Backup", None, -1))

