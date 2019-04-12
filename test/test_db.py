import tchelper.db
from unittest import mock
import pytest


@mock.patch('tchelper.db.DB.commit_sql')
@pytest.mark.parametrize('table, col, val', [
                        ('Table1', ('col1', 'col2'), ('val1', 'val2')),
                        ('Location', ('city', 'state', 'country'), ('Miami', 'Florida', "USA")),
                        ('Time', ('Zone'), ('Eastern'))])
def test_add_item(mock_commit_sql, table, col, val):
    """
    Add a single row to the database

    Only inerts a single row into the database. Both column(s) and value(s)
    must be in a tuple.

    :param mock_commit_sql: The mock object for db.DB.commit.sql()
    :param table: The table that the row will be inserted into
    :param col: The column(s) that the value will be inserted under
    :param val: The value(s) that will be inserted into the row
    :type table: str
    :type col: tuple
    :type val: tuple
    """

    item = DB()
    item.add_item(table, col, val)

    mock_commit_sql.assert_called_once_with(None, f'INSERT INTO {table} {col} VALUES {val}')


@mock.patch('tchelper.db.DB.return_sql', return_value='5')
def test_count_rows(mock_return_sql):
    """
    Returns the total number of rows in a Table.

    Returns the number of rows in a table with visibility = True or
    visibility = False.

    :param mock_return_sql: The mock for the db.DB.return_sql() method
    """
    count = DB()
    num_row = count.count_rows('Table1', True)

    mock_return_sql.assert_called_once_with('SELECT count(*) FROM Table1 WHERE visibility = True')
    assert num_row == 5
