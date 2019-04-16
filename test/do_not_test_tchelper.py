from tchelper.config import Config
import pytest
from unittest import mock


@mock.patch('tchelper.tchelper.Config.getValue')
def test_check_first_run(getValue):

    mock_getValue.return_value = "value"
    pass
