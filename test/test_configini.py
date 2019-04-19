import hashlib


def test_config():
    """Tests to make sure the default config.ini file does not change

    This test confirms that the default config.ini file does not change.
    It checks the md5sum of the file aginst what the md5sum should be.
    if the md5sum changes then the config.ini file was edited by accident.
    Sometimes that happens when running the code directly.

    If the test fails, check the config.ini file and undo the changes.

    :var hash_original: Holds the md5sum of what the config.ini should be.

    """

    hash_original = '808d9b463eaed5d8f58f869c8c8c4fd9'

    file = '../tchelper/config.ini'
    with open(file, 'rb') as f:
        config_file = f.read()

    hash = hashlib.md5()
    hash.update(config_file)

    assert hash_original == hash.hexdigest()
