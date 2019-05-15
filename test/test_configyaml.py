import hashlib


def test_config():
    """Tests to make sure the default config.yaml file does not change

    This test confirms that the default config.yaml file does not change. It
    checks the md5sum of the file aginst what the md5sum should be. if the
    md5sum changes then the config.yaml file was edited by accident. Sometimes
    that happens when running the code directly.

    If the test fails, check the config.yaml file and undo the changes.

    :var hash_original: Holds the md5sum of what the config.yaml should be.

    """

    hash_original = '38d32794bb34ffee29b2a81c68e9d71d'

    file = '../src/config.yaml'
    with open(file, 'rb') as f:
        config_file = f.read()

    hash = hashlib.md5()
    hash.update(config_file)

    assert hash_original == hash.hexdigest()
