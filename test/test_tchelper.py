import yam
import pytest
from unittest import mock
import tchelper.tchelper as tchelper

dict1 = {'first_run': True, 'db_location': '/test/test.db'}
dict2 = {'first_run': False, 'db_location': '/test/test.db'}

# yam.setValue() & yam.getValue() are being testing in test_yam.py
