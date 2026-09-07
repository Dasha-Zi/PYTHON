import pytest
from string_utils import StringUtils


string_utils = StringUtils()

# Тесты для функции capitalize
@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected

# Тесты для функции trim

@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    (" skypro", "skypro"),
    ("    skypro", "skypro"),
    ("  hello world", "hello world"),
    ("  skypro   ", "skypro   "),
    ("  123abc", "123abc"),
    ("  ", ""),
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected

@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "skypro"),
    ("", ""),
])
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected

# Тесты для функции contains

@pytest.mark.positive
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("Skypro", "S", True),
    ("skypro", "sky", True ),
    ("123abc", "23", True), 
    ("hello world", " ", True),
])
def test_contains_positive(input_str, symbol, expected):
    assert string_utils.contains(input_str, symbol,) == expected

@pytest.mark.negative
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("Skypro", "U", False),
    ("Skypro", "s", False ),
    ("", "s", False ),
])
def test_contains_negative(input_str, symbol, expected):
    assert string_utils.contains(input_str, symbol,) == expected

# Тесты для функции delete_symbol

@pytest.mark.positive
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("SkyPro", "k", "SyPro"),
    ("SkyPro", "Pro", "Sky"),
    ("hello world", "l", "heo word"),
    ("ababab", "b", "aaa"),
])
def test_delete_symbol_positive(input_str, symbol, expected):
    assert string_utils.delete_symbol(input_str, symbol,) == expected

@pytest.mark.negative
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("SkyPro", "X", "SkyPro"),  
    ("SkyPro", "", "SkyPro"),   
    ("", "A", ""),            
])
def test_delete_symbol_negative(input_str, symbol, expected):
    assert string_utils.delete_symbol(input_str, symbol) == expected