import pytest
from app.users.models import User


def test_create_user():
    User.create_user(email='test@test.com', password='abc123')


def test_assert():
    assert True is True


def test_equal():
    assert 1 == 1


# def tests_equal():
#     assert 1 != 1


def test_invalid_assert():
    with pytest.raises(AssertionError):
        assert True is not True
