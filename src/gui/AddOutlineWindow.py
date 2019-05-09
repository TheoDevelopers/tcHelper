# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AddOutlineWindow.ui',
# licensing of 'AddOutlineWindow.ui' applies.
#
# Created: Thu May  9 15:25:15 2019
#      by: pyside2-uic  running on PySide2 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_AddOutlineWindow(object):
    def setupUi(self, AddOutlineWindow):
        AddOutlineWindow.setObjectName("AddOutlineWindow")
        AddOutlineWindow.resize(424, 140)
        self.gridLayout_2 = QtWidgets.QGridLayout(AddOutlineWindow)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.button_cancel = QtWidgets.QPushButton(AddOutlineWindow)
        self.button_cancel.setObjectName("button_cancel")
        self.gridLayout_2.addWidget(self.button_cancel, 2, 1, 1, 1)
        self.button_save = QtWidgets.QPushButton(AddOutlineWindow)
        self.button_save.setObjectName("button_save")
        self.gridLayout_2.addWidget(self.button_save, 2, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 2, 0, 1, 1)
        self.frame = QtWidgets.QFrame(AddOutlineWindow)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.line_number = QtWidgets.QLineEdit(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_number.sizePolicy().hasHeightForWidth())
        self.line_number.setSizePolicy(sizePolicy)
        self.line_number.setMinimumSize(QtCore.QSize(10, 0))
        self.line_number.setObjectName("line_number")
        self.gridLayout.addWidget(self.line_number, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 2, 1, 1)
        self.line_title = QtWidgets.QLineEdit(self.frame)
        self.line_title.setObjectName("line_title")
        self.gridLayout.addWidget(self.line_title, 2, 1, 1, 2)
        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 3)

        self.retranslateUi(AddOutlineWindow)
        QtCore.QObject.connect(self.button_cancel, QtCore.SIGNAL("clicked()"), AddOutlineWindow.close)
        QtCore.QMetaObject.connectSlotsByName(AddOutlineWindow)

    def retranslateUi(self, AddOutlineWindow):
        AddOutlineWindow.setWindowTitle(QtWidgets.QApplication.translate("AddOutlineWindow", "Add an Outline", None, -1))
        self.button_cancel.setText(QtWidgets.QApplication.translate("AddOutlineWindow", "Cancel", None, -1))
        self.button_save.setText(QtWidgets.QApplication.translate("AddOutlineWindow", "Save", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("AddOutlineWindow", "Outline title:", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("AddOutlineWindow", "Outline number:", None, -1))

