"""Tests for the yam module"""

from unittest import mock
import pytest
import scr.yam as yam

# Dictionaries for testing purposes
DICT1 = {'first_run': True, 'db_location': '/test/test.db'}
DICT2 = {'first_run': False, 'db_location': '/test/test.db'}


@mock.patch('scr.yam.yaml.safe_load')
def test_get_value(mock_safe_load):
    """Test the get_value function"""

    mock_safe_load.return_value = DICT1

    data1 = yam.get_value('first_run')
    data2 = yam.get_value('db_location')

    assert data1
    assert data2 == '/test/test.db'


@mock.patch('scr.yam.yaml.safe_load')
@mock.patch('scr.yam.write_yaml')
def test_set_value(write_yaml, mock_safe_load):
    """Tests the set_value function"""

    mock_safe_load.return_value = DICT1
    key = 'first_run'
    value = False

    yam.set_value(key, value)
    assert write_yaml.called
    write_yaml.assert_called_with(DICT2)

@mock.patch('scr.yam.yaml.safe_load')
@mock.patch('scr.yam.write_yaml')
def test_set_value_missing_key(mock_write_yaml, mock_safe_load):
    """Tests exception when key passed is missing

    mock_write_yaml is included as an argument but not used so that the test
    won't be able to write to the actual config.yaml file in the case which
    the correct key is passed in.

    Ignore Pylint's warning of unused-argument unless you know a better way
    of avoiding accidentally writing to the configuration file.

    """

    mock_safe_load.return_value = DICT1
    with pytest.raises(Exception) as e_error:
        yam.set_value('wrong_key', True)
        print(e_error)
