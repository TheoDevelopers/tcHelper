import configparser
import os
import os.path


class Configr:
    """Wrapper for configparser

    Class that acts as an interface to the `configparser` library for tcHelper.

    :var config_file_location: The location of the config.ini file which by default should reside in the root directory of tcHelper.py.
    """

    config_file_location = 'config.ini'

    @staticmethod
    def file_exist(filename):
        """Tests *filename* to make sure it's an actual file with write and read access.

        Tests to make sure *filename* exists, can be read, and written to. If one of the three conditions fail,
        *file_exist()* returns *False* otherwise it returns *True*.

        :param filename: location for the file to be tested.
        :type filename: str

        :return: Return *True* if file exists, can be read, and can be written to.
        :rtype: Bool

        .. todo: update docstrings
        """

        if os.path.isfile(filename) == False:
            return False
        elif os.access(filename, os.W_OK) == False:
            return False
        elif os.access(filename, os.R_OK) == False:
            return False
        else:
            return True


    def get_value(self, section, key):
        """
        Return the value of a key in config.ini.

        Use `get_value()` when you want to get the key for an
        option from `config.ini`.

        :param section: The section within config.ini.
        :param key: The key of a section that its value will be returned.
        :type section: str
        :type key: str
        :return: Returns the value for the key.
        :rtype: str

        :Example:

        +-----------+-----------+-------------------+
        |  Section  |    Key    |       Value       |
        +-----------+-----------+-------------------+
        |    DB     |  location | /foo/database.thd |
        +-----------+-----------+-------------------+

        >>> config = Configr()
        >>> config.change_value('DB', 'location', '/foo/database.thd')
        >>> config.get_value('DB', 'location')
        '/foo/database.thd'
        """

        if Configr.file_exist():
            config = configparser.ConfigParser()
            config.read(Configr.config_file_location)
            return config[section][key]

    def change_value(self, section, key, value):
        """Method for changing the key of an option in `config.ini`.

        Use `change_value()` when you need to edit an option in config.ini

        :param section: The section within config.ini that contain the option to be changed.
        :param key: The within the section option that is to be changed.
        :param value: The value for the option that will be written.

        :var config_loc: Holds the location for the config.ini file on the user's drive.

        :Example:

        +-----------+-----------+-------------------+
        |  Section  |    Key    |       Value       |
        +-----------+-----------+-------------------+
        |    DB     |  location | /foo/database.thd |
        +-----------+-----------+-------------------+

        >>> config = Configr()
        >>> config.change_value('DB', 'location', '/foo/config.ini')
        >>> config.get_value('DB', 'location')
        '/foo/config.ini'
        """

        config_loc = Configr.config_file_location

        con = configparser.ConfigParser()
        con.read(config_loc)
        con[section][key] = value
        with open(config_loc, 'w') as file:
            con.write(file)
        file.close()

