import pytest
from ..source.math_ksi import *


def test_mean():
    assert mean([3, 45, 32]) == 26.666666666666668
    assert mean([3]) == 3
    assert mean([]) == None


def test_make_unique():
    assert make_unique([1, 2, 3, 4, 5, 6, 7, 8, 9]) == [
        1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert make_unique([1, 1, 1, 1, 1, 1, 1, 1, 1]) == [1]
    assert make_unique([]) == []


def test_get_binary():
    assert get_binary(3) == '11'
    assert get_binary(2) == '10'
    assert get_binary(1) == '1'
    assert get_binary(None) == None


def test_variance():
    assert variance([3, 45, 32]) == 308.2222222222222
    assert variance([3]) == 0
    assert variance([]) == None
    assert variance(None) == None
