import random
from sorting import *


entry = random.sample(range(1, 1_000), 999)
expected = list(range(1, 1_000))

def test_bubble_sort(benchmark):
    assert benchmark(bubble_sort, entry.copy()) == expected

def test_select_sort(benchmark):
    assert benchmark(selection_sort, entry.copy()) == expected

def test_insert_sort(benchmark):
    assert benchmark(insert_sort, entry.copy()) == expected

