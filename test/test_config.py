"""
Test file for config module

"""
from tchelper.config import Config
from unittest import mock
import pytest


def test_imports():
    """
    Test to see modules can be imported from the module being tested.

    .. warning:: I am not sure if this is a vaild test. There must be a better way of doing this.
    """

    try:
        from tchelper.config import configparser
        from tchelper.config import os
        #        from tchelper.config import os.path  # Doesn't want to work.
    except ModuleNotFoundError as e:
        pytest.fail(e, pytrace=True)


@mock.patch('tchelper.config.os.path.isfile')
@mock.patch('tchelper.config.os.access')
@pytest.mark.parametrize('isfile, access, result', [(True, True, True),
                                                    (True, False, False),
                                                    (False, True, False),
                                                    (False, False, False)])
def test_file_exist(mock_isfile, mock_access, isfile, access, result):
    """
    Make sure files exist and has read and write access.

    The Config.file_exist() method returns true when a file exists, has read and write access. If any of those three
    conditions are *False*, Config.file_exist() returns *False*.

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
    assert Config.file_exist(filename) == result


## CANT GET THE TEST BELLOW TO RUN CORRECTLY ##

# @mock.patch('tchelper.config.configparser.ConfigParser')
# def test_get_value_2(mock_ConfigParser):
#
#     mock_ConfigParser.read.return_value = "[APP] " \
#                                           "first_time = NO"
#     # mock_ConfigParser.get.return_value = {'section': {'key': 'test'}}
#     config = Config()
#     value = config.getValue('APP', 'first_time')
#
#     assert value == 'NO'
