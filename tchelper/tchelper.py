#!/usr/bin/env python3.7
from PySide2 import QtWidgets
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import QFile
from config import Config
from tchelperlib import Brother
import database


def check_first_run():
    """

    Return **True** if it's the first time tcHelper runs.

    :return: Value for [APP] [first_time_running]
    :rtype: bool

    """

    file = Config()
    return bool(file.getValue("APP", "first_time_running"))


def set_first_run(value):
    """Sets the first_run value in config.ini

    Sets `False` in `[APP]: first_time_running` to mark that the tcHelper program has run before.

    :param value: The value to set *first_time_running*
    :type value: str

    """

    file = Config()
    file.setValue('APP', 'first_time_running', value)


def set_database_location(location):
    """Sets the location of the database in config.ini

    :param location: The location of the database
    :type location: str
    :return:

    """

    file = Config()
    file.setValue('DB', 'location', location)


def main():
    """Entry point for the tcHelper program."""

    if check_first_run():

        QtWidgets.QApplication()
        file_name = QtWidgets.QFileDialog.getSaveFileName(None, "Save New Database", "New_Database.tcd",
                                                          "tcHelper Database *.tcd")

        if file_name == '':
            print('Please run tcHelper again and select a location to save the database')
            quit()

        set_database_location(file_name[0])
        set_first_run('False')

        db = database.DB()
        db.initDB()

    else:
        print('RUN GUI')


if __name__ == '__main__':
    main()
