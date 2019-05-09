"""YAML wrapper for tcHelper"""

import yaml

FILE = 'config.yaml'  # Default configuration file


def open_config_file():
    """Reads the configuration file _config.yaml

    :return: The configuration file _config.yaml_
    :rtype: str

    """

    with open(FILE, 'r') as f:
        return f.read()


def write_yaml(config):
    """Writes to the configuration file _config.yaml

    Writes to the configuration file passed in and returns true when
    the file is written.

    :param config: The configuration to be written
    :return: True
    :rtype: bool

    """

    with open(FILE, 'w') as f:
        yaml.dump(config, f)
    return True


def get_value(key):
    """Returns the value for the key

    :param key: The _key_ to be returned
    :return: The _value_ of the key passed in

    """

    dict = yaml.safe_load(open_config_file())
    value = dict[key]

    return value


def set_value(key, value):
    """Sets a key value

    Takes the key and value and saves it to the default configuration file.

    :param key: The _key_ to the value that is to be set.
    :param value: The _value_ that is to be set.
    :var config: The content of the configuration file.

    """

    config = yaml.safe_load(open_config_file())

    if key in config:
        config[key] = value
        write_yaml(config)
    else:
        raise ValueError(f'The key {key} does not exist in config.yaml. Use '
                         f'add_value to add the key.')
