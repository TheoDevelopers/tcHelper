import pytest
from tchelper.database import DB
from tchelper.config import Config


def test_imports():
    """
    Test to see modules can be imported from the module being tested.

    .. warning:: I am not sure if this is a vaild test. There must be a better way of doing this.
    """

    try:
        import sqlalchemy
        import config
    except ModuleNotFoundError as e:
        pytest.fail(e, pytrace=True)
