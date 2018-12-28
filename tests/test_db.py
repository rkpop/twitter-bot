from CONFIG import TABLE_NAME, DB_URL
from kpopbot.db import Database
import pytest


@pytest.fixture
def instance():
    return Database(DB_URL, TABLE_NAME)


def test_no_entry(instance):
    assert instance.check_table("502fjx") == True


def test_write_something(instance):
    assert instance.write_table("502fjx") == "502fjx"


def test_check_after_entry(instance):
    assert instance.check_table("502fjx") == False

