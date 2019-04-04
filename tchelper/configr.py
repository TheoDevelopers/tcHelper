import configparser


class Configr:
    """Wrapper for configparser

    Class that acts as an interface to the `configparser` library for tcHelper.

    :var config_file_location: The location of the config.ini file which by default should reside in the root directory of tcHelper.py.
    """

    config_file_location = 'config.ini'

    @staticmethod
    def file_exist(loc = config_file_location):
        """Test to make sure the file exists and is not write protected.

        Tests to make sure the file exists and can be written to. If the
        file does not exists or can't be access, possibly due to write protection
        the method will display an error and exit completely.

        :param loc: location for the database. Defaults to the config_file_location if no arguments are passed.
        :type loc: str

        :return: Return 'True' if file exists and isn't write protected.
        :rtype: Bool

        .. todo: Implement a elegant to exit when file is not accessible.
        """

        # Testing the file with exceptions rather than os.access() due to security risk.
        # Source: https://docs.python.org/3.4/library/os.html#os.X_OK
        try:
            open(loc)

        except FileNotFoundError:
            print("-" * 80)
            print("The config.ini file was not found.")
            print("-" * 80)
            print("Something may have gone wrong with the installation.\n"
                  "Make sure the config.ini file is located in the "
                  "application's root directory.")
            quit()

        except PermissionError:
            print("-" * 80)
            print("Permission problem.")
            print("-" * 80)
            print("You do not have sufficient permission for the config.ini file.")
            print("Fix the problem then run {} again.".format(name))
            quit()

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

