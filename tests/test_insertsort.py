import pytest
from insert_sort.insertionsort import insertionsort

def test_insert_sort():
    array = [8,4,23,42,16,15]
    actual = insertionsort(array)
    expected = [4, 8, 15, 16, 23, 42]
    assert actual == expected

def test_insert_uniques():
    array = [5,12,7,5,5,7]
    actual = insertionsort(array)
    expected = [5, 5, 5, 7, 7, 12]
    assert actual == expected

def test_insert_nearly_sorted():
    array = [2,3,5,7,13,11]
    actual = insertionsort(array)
    expected = [2, 3, 5, 7, 11, 13]
    assert actual == expected