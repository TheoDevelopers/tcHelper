"""Tests for the yam module"""

import scr.yam as yam
from unittest import mock

dict1 = {'first_run': True, 'db_location': '/test/test.db'}
dict2 = {'first_run': False, 'db_location': '/test/test.db'}


@mock.patch('scr.yam.yaml.safe_load')
def test_getValue(mock_safe_load):
    """Test the getValue function"""

    mock_safe_load.return_value = dict1

    data1 = yam.getValue('first_run')
    data2 = yam.getValue('db_location')

    assert data1 == True
    assert data2 == '/test/test.db'


@mock.patch('scr.yam.yaml.safe_load')
@mock.patch('scr.yam.write_yaml')
def test_setValue(write_yaml, mock_safe_load):
    """Tests the setValue function"""

    mock_safe_load.return_value = dict1
    key = 'first_run'
    value = False

    yam.setValue(key, value)
    assert write_yaml.called
    write_yaml.assert_called_with(dict2)
