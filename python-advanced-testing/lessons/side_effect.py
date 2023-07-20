import os
import pytest
import shutil
from prettify_html_file import prettify


# BEGIN (write your solution here)
def get_fixture_path(filename):
    return os.path.join('fixtures', filename)


def read(filename):
    with open(get_fixture_path(filename), 'r') as f:
        data = f.read()
        return data


before = get_fixture_path('before.html')


@pytest.fixture
def get_after():
    after = read('after.html')
    return after


@pytest.fixture
def get_before_temp(tmpdir):
    before_temp = tmpdir.join('before.html')
    shutil.copyfile(before, before_temp)
    return before_temp


def test_prettify(get_after, get_before_temp):
    prettify(get_before_temp)
    print(read(get_before_temp))
    expected = get_after
    print(expected)

    assert read(get_before_temp) == expected
# END
