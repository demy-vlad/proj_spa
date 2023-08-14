import pytest
from main.validators import validate_username, validate_email, is_valid_html

@pytest.mark.parametrize("username, expected_result", [
    ("John", True),
    ("john123", True),
])
def test_validate_username(username, expected_result):
    assert validate_username(username) == expected_result

@pytest.mark.parametrize("email, expected_result", [
    ("user@example.com", True)
])
def test_validate_email(email, expected_result):
    assert validate_email(email) == expected_result

@pytest.mark.parametrize("html, expected_result", [
    ("<a href='https://example.com'>Link</a><i>Italic</i>", True)
])
def test_is_valid_html(html, expected_result):
    assert is_valid_html(html) == expected_result

@pytest.mark.xfail
@pytest.mark.parametrize("username, expected_result", [
    ("J", False),
    ("test test", False),
    ("user@name", False),
    ("a" * 257, False),
    ("~!@#$%^&*()_<>?|", False)
])
def test_validate_username_xfail(username, expected_result):
    assert validate_username(username) == expected_result

@pytest.mark.xfail
@pytest.mark.parametrize("email, expected_result", [
    ("invalid.email", False),
    ("a" * 51, False),
])
def test_validate_xfail(email, expected_result):
    assert validate_email(email) == expected_result
