import configparser
import os
import os.path


class Config:
    """
    Wrapper for configparser

    Class that acts as an interface to the `configparser` library for tcHelper.

    :var config_file_location: The location of the config.ini file which by default should reside in the root directory of tcHelper.py.
    """

    config_file_location = 'config.ini'  # The default location for the configuration file.

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

    def getValue(self, section, key):
        """
        Return the value of a key in config.ini.

        Use `get_value()` when you want to get the key for an
        option from `config.ini`.

        .. todo:: If config file does not exist, raise exception.

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

        >>> config = Config()
        >>> config.setValue('DB', 'location', '/foo/database.thd')
        >>> config.getValue('DB', 'location')
        '/foo/database.thd'
        """

        if Config.file_exist(Config.config_file_location):
            config = configparser.ConfigParser()
            config.read(Config.config_file_location)
            return config[section][key]
        else:
            return False

    def get_value_2(self, section, key):
        """
        A method only for testing

        """

        config = configparser.ConfigParser()
        config.read(Config.config_file_location)
        return config[section, key]

    def setValue(self, section, key, value):
        """Method for changing the key of an option in `config.ini`.

        Use `setValue()` when you need to edit an option in config.ini

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

        >>> config = Config()
        >>> config.setValue('DB', 'location', '/foo/config.ini')
        >>> config.getValue('DB', 'location')
        '/foo/config.ini'
        """

        config_loc = Config.config_file_location

        con = configparser.ConfigParser()
        con.read(config_loc)
        con[section][key] = value
        with open(config_loc, 'w') as file:
            con.write(file)
        file.close()


if __name__ == '__main__':
    print(f'{__name__} is not a script. Do not run directly.')