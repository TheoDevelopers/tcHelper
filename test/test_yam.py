"""Tests for the yam module"""

import scr.yam as yam
from unittest import mock

dict1 = {'first_run': True, 'db_location': '/test/test.db'}
dict2 = {'first_run': False, 'db_location': '/test/test.db'}


@mock.patch('scr.yam.yaml.safe_load')
def test_getValue(mock_safe_load):
    """Test the get_value function"""

    mock_safe_load.return_value = dict1

    data1 = yam.get_value('first_run')
    data2 = yam.get_value('db_location')

    assert data1 == True
    assert data2 == '/test/test.db'


@mock.patch('scr.yam.yaml.safe_load')
@mock.patch('scr.yam.write_yaml')
<<<<<<< HEAD
def test_set_value(write_yaml, mock_safe_load):
    """Tests the set_value function"""
=======
def test_setValue(write_yaml, mock_safe_load):
    """Tests the setValue function"""
>>>>>>> master

    mock_safe_load.return_value = dict1
    key = 'first_run'
    value = False

    yam.set_value(key, value)
    assert write_yaml.called
    write_yaml.assert_called_with(dict2)
