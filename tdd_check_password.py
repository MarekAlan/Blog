import pytest


def check_password(password):
    special = """!@#$%^&*()_+=-}{][|":\\';?></.,|"""
    big = any([x for x in password if x.isupper()])
    small = any([x for x in password if x.islower()])
    digit = any([x for x in password if x.isdigit()])
    special = any([x for x in password if x in special])
    return len(password) >= 7 and big and small and digit and special


@pytest.mark.parametrize("password, result", [
    ("aaaa@A7", True),
    ("aaaaaa", False),
    ("aaaaaaa", False),
    ("AAAAAAA", False),
    ("aaaAAAA", False),
    ("aaa4AAA", False),
])
def test_check_password(password, result):
    assert check_password(password) == result
