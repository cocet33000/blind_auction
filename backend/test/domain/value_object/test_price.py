import pytest

from main.domain.value_object import Price


def test_Price型に負の値はNG():
    with pytest.raises(ValueError):
        Price(-100)
