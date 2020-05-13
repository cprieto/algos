import random
from sorting import *

expected = list(range(1, 100))

def test_bubble_sort():
    entry = random.sample(range(1, 100), 99)
    bubble_sort(entry)
    assert entry == expected


def test_insert_sort():
    entry = random.sample(range(1, 100), 99)
    selection_sort(entry)
    assert entry == expected


def test_selection_sort():
    entry = random.sample(range(1, 100), 99)
    insert_sort(entry)
    assert entry == expected

# def test_quick_sort():
#     pass

# def test_merge_sort():
#     pass

# def test_counting_sort():
#     pass
