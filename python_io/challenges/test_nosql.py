import os
from nosql import get_, set_
import pytest


@pytest.fixture()
def db(tmpdir):
    path = os.path.join(tmpdir, 'nosql.db')
    open(path, 'w')
    return path


def test_write_read(db):
    set_(db, 'key', 'value')
    set_(db, 'key2', 'value2')
    set_(db, 'key3', 'value3')

    assert get_(db, 'key') == 'value'
    assert get_(db, 'key2') == 'value2'
    assert get_(db, 'key3') == 'value3'


def test_rewrite(db):
    set_(db, 'key', 'very very very long value')
    set_(db, 'key', 'short value')

    assert get_(db, 'key') == 'short value'


def test_no_interception(db):
    set_(db, 'one', 'two')
    set_(db, 'two', 'some data')
    set_(db, 'three', 'another data')

    assert get_(db, 'one') == 'two'
