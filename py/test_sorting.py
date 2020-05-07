import random
from sorting import *

entry = random.sample(range(1, 100), 99)
expected = list(range(1, 100))

def test_bubble():
    assert bubble_sort(entry.copy()) == expected


def test_insert():
    assert insert_sort(entry.copy()) == expected


def test_selection():
    assert selection_sort(entry.copy()) == expected
