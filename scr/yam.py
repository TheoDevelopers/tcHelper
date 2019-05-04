"""YAML wrapper for tcHelper"""

import yaml

file = 'config.yaml'


def open_config_file():

    with open(file, 'r') as f:
        return f.read()


def write_yaml(config):
    """Write to config.yaml"""

    with open(file, 'w') as f:
        yaml.dump(config, f)
    return True


def getValue(key):
    """Returns the value for the key"""

    dict = yaml.safe_load(open_config_file())
    value = dict[key]

    return value


def setValue(key, value):
    """Sets a key value
    Takes the key and value and saves it to config.yaml.

    """

    dict = yaml.safe_load(open_config_file())

    if key in dict:
        dict[key] = value
        write_yaml(dict)
    else:
        raise ValueError(
            f'The key {key} does not exist in config.yaml. Use addValue to add the key.')
