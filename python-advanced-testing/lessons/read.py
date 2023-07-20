import pytest
import os


def get_function(path):
    f = open(path)
    data = f.read()
    f.close()
    return data


def test_read_file_found():
    with pytest.raises(Exception) as e:
        get_function('/undefined')

    assert str(e.value) == "[Errno 2] No such file or directory: '/undefined'"


def test_read_directory_not_found():
    with pytest.raises(Exception) as e:
        get_function('/etc')

    assert str(e.value) == "[Errno 21] Is a directory: '/etc'"
