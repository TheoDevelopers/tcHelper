#!/usr/bin/env python3.7
from PySide2 import QtWidgets
from configr import Configr
from database import DB
from tchelperlib import Brother


def main():
    """
    Entry point for the tcHelper program.
    """
    config_file = Configr()
    if config_file.getValue('APP', 'first_time_running') == 'True':

        QtWidgets.QApplication()
        file_name = QtWidgets.QFileDialog.getSaveFileName(None, "Save New Database", "New_Database.tcd",
                                                          "tcHelper Database *.tcd")
        # TODO: Doesn't work, need to be fixed
        if file_name == '':
            print('Please run tcHelper again and select a location to save the database')
            quit()

        config_file.setValue('DB', 'location', file_name[0])
        config_file.setValue('APP', 'first_time_running', 'False')

        db = DB()
        db.setDB(file_name[0])




    else:
        print('RUN GUI')


if __name__ == '__main__':
    main()
