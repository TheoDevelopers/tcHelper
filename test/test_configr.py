"""
Test file for configr module

"""
from tchelper.configr import Configr
import tchelper.configr
from unittest import mock
import pytest


@mock.patch('tchelper.configr.os.path.isfile')
@mock.patch('tchelper.configr.os.access')
@pytest.mark.parametrize('isfile, access, result', [(True, True, True),
                                                    (True, False, False),
                                                    (False, True, False),
                                                    (False, False, False)])
def test_file_exist(mock_isfile, mock_access, isfile, access, result):
    """
    Make sure files exist and has read and write access.

    The Configr.file_exist() method returns true when a file exists, has read and write access. If any of those three
    conditions are *False*, Configr.file_exist() returns *False*.

    :param mock_isfile: The mock object that mocks the os.path.isfile() method.
    :param mock_access: The mock object that mocks the os.access() method.
    :param isfile: The return_value for the mock_isfile mock object.
    :param access: The return_value for the mock_access mock object.
    :param result: The expect result for each test.
    :type isfile: bool
    :type access: bool
    :type result: bool
    """
    mock_isfile.return_value = isfile
    mock_access.return_value = access

    filename = 'anyfile.ini'
    assert Configr.file_exist(filename) == result

@mock.patch('tchelper.configr.Configr.file_exist')
@mock.patch('tchelper.configr.configparser.ConfigParser.read')
def test_get_value(mock_file_exist, mock_read):

    mock_file_exist.return_value = True

    section = 'sec'
    key = 'key'

    config = Configr()
    config.get_value(section, key)
