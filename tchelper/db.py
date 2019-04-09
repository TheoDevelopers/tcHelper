import sqlite3
from PySide2 import QtWidgets
from .configr import Configr


class DB:
    """
    The DB module provides an interface to the project's SQLite3 database.

    :var db_location: The location of the database as recorded in the `config.ini` file.

    .. Warning:: This module is undergoing refactoring. Many of the methods will be
    changing.
    """

    db_location = 'did not update'

    @staticmethod
    def get_path():
        """
        Returns the path of the database located in config.ini

        :return: Returns the path to the database as listed in config.ini.
        :rtype: str
        """
        config = Configr()
        return config.get_value('DB', 'location')

    @staticmethod
    def db_init():
        """
        Initialize a new SQLite database.

        Method to initialize a new database. This method can be invoked when tcHelper runs for the first time or when
        a new database needs to be created. The `db_init()` method does not take any arguments and returns nothing.

        .. todo:: Should return `True` if database was created successfully otherwise return `False`.
        """

        conn = sqlite3.connect(DB.get_path())
        c = conn.cursor()
        c.execute('''CREATE TABLE Assignment (
                                              id INTEGER PRIMARY KEY NOT NULL
                                              UNIQUE,
                                              speaker INTEGER NOT NULL,
                                              talk INTEGER NOT NULL,
                                              congregation INTEGER NOT NULL,
                                              chairman INTEGER NOT NULL,
                                              hospitality INTEGER NOT NULL,
                                              date DATETIME NOT NULL,
                                              FOREIGN KEY(speaker) REFERENCES
                                              Brother(id),
                                              FOREIGN KEY(talk) REFERENCES
                                              Talk(id),
                                              FOREIGN KEY(congregation)
                                              REFERENCES Congregation(id),
                                              FOREIGN KEY(chairman)
                                              REFERENCES Brother(id),
                                              FOREIGN KEY(hospitality)
                                              REFERENCES Hospitality(id)
                                              )''')
        c.execute('''CREATE TABLE Brother (
                                           id INTEGER PRIMARY KEY NOT NULL
                                           UNIQUE,
                                           first_name TEXT NOT NULL,
                                           middle_name TEXT,
                                           last_name TEXT NOT NULL,
                                           email TEXT,
                                           phone TEXT NOT NULL,
                                           congregation NUMERIC NOT NULL,
                                           responsibility TEXT NOT NULL,
                                           speaker BOOL NOT NULL DEFAULT 0,
                                           chairman BOOL NOT NULL DEFAULT 0,
                                           coordinator BOOL NOT NULL DEFAULT 0,
                                           note BLOB,
                                           visibility BOOL NOT NULL DEFAULT
                                           True,
                                           FOREIGN KEY(congregation)
                                           REFERENCES Congregation(id)
                                           )''')
        c.execute('''CREATE TABLE Congregation (
                                           id INTEGER PRIMARY KEY NOT NULL
                                           UNIQUE,
                                           name TEXT NOT NULL,
                                           phone TEXT,
                                           email TEXT,
                                           street TEXT NOT NULL,
                                           city TEXT NOT NULL,
                                           state TEXT NOT NULL,
                                           zip TEXT NOT NULL,
                                           week TEXT NOT NULL,
                                           time TEXT NOT NULL,
                                           long NUMERIC,
                                           lat NUMERIC,
                                           note BLOB,
                                           visibility BOOL NOT NULL DEFAULT True
                                           )''')
        c.execute('''CREATE TABLE Hospitality (
                                               id INTEGER PRIMARY KEY NOT
                                               NULL UNIQUE,
                                               name TEXT NOT NULL,
                                               note TEXT
                                               )''')
        c.execute('''CREATE TABLE SpeakerTalk (
                                               id INTEGER PRIMARY KEY NOT
                                               NULL UNIQUE,
                                               title INTEGER NOT NULL,
                                               speaker INTEGER NOT NULL,
                                               FOREIGN KEY(title) REFERENCES
                                               Talk(id)
                                               FOREIGN KEY(speaker)
                                               REFERENCES Brother(id)
                                               )''')
        c.execute('''CREATE TABLE Talk (
                                        id INTEGER PRIMARY KEY NOT NULL UNIQUE,
                                        number TEXT NOT NULL,
                                        title TEXT,
                                        visibility BOOL NOT NULL DEFAULT True
                                        )''')
        conn.close()

    def add_item(self, table, column, value):
        """
        Takes an item and adds it to the database.

        Inserts a single row into the database useing the
        column(s) and value(s) passed in. The column(s) and
        value(s) must be in a tuple.

        :param table: The table name that the item will be added to
        :param column: The column(s) needed
        :param value: The value(s) that will be added
        :type table: str
        :type column: tuple
        :type value: tuple
        """
        sql = f'INSERT INTO {table} {column} VALUES {value}'

        DB.commit_sql(None, sql)

    def count_rows(self, table, visible=True):
        """
        Return the total number of rows in a table.

        Return the total number if entries, or rows, in a table.

        .. Note:: The row number is returned as a string. The returned count is then converted to an int.

        :param table: The table that will be counted
        :param visible: Count only rows with visibility = True or visibility = False
        :return: The number of rows
        :type table: str
        :type visible: bool
        :rtype: int
        """

        if visible:
            sql = f'SELECT count(*) FROM {table} WHERE visibility = True'
            count = self.return_sql(sql)
            return int(count[0][0])
        else:
            sql = "SELECT Count(*) FROM {Table}".format(Table=table)
            count = self.return_sql(sql)
            return int(count[0][0])

    def modify_item(self, table, column, value, row_id):
        """Modifies an item in the database.

        :param table: The table to be modified.
        :param column: The column being modified.
        :param value: The value being modified.
        :param row_id: The row in the database being modified.
        :type table: str
        :type column: list
        :type value: list
        :type row_id: int

        .. todo:: Make an example
        """

        # Adds =?, to each column so that values can then be unpacked.
        column_new = "=?, ".join(column)
        column_new = column_new + "=?"

        conn = sqlite3.connect()
        c = conn.cursor()
        c.execute("PRAGMA foreign_keys = ON")

        col_len = len(column)
        for x in range(col_len):
            c.execute("UPDATE {} SET {} WHERE id = {}".format(
                table, column_new, row_id), value)
        conn.commit()
        conn.close()

    def return_item(self, table, row_id):
        """
        Returns a specific item from the database.

        :type row_id: int
        :param table: The table the data resides in.
        :param row_id: The ID of the item being retrieved.
        """

        sql = "SELECT * FROM {TABLE} WHERE id={ID}".format(TABLE=table,
                                                           ID=row_id)
        return self.return_sql(sql)

    def delete_data(self):
        """
        Method to delete record from the database.

        Records are never really deleted from the database. Instead records are marked as `Visiable: False`.

        .. Note:: Method has not been implemented.
        """

        pass

    def commit_sql(self, sql):
        """
        Takes the SQL commands and commits it to SQLite

        :param sql: the SQL command that needs to be passed to SQLite.
        """

        print("Commit_sql(): {}".format(sql))
        conn = sqlite3.connect()
        c = conn.cursor()
        c.execute("PRAGMA foreign_keys = ON")
        c.execute("""{}""".format(sql))
        conn.commit()
        conn.close()

    def return_sql(self, sql):
        """
        Returns data from the SQLite database.

        :param sql: the SQL command to pass to SQLite
        :return data: returns a list with each row in a tuple.
        """

        comm = sqlite3.connect()
        c = comm.cursor()
        c.execute("PRAGMA foreign_keys = ON")
        c.execute(sql)
        data = c.fetchall()
        c.close()

        return data
