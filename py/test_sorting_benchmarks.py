import random
from sorting import *


def setup():
    return (random.sample(range(1, 1_000), 999),), {}

def test_bubble_sort(benchmark):
    benchmark.pedantic(bubble_sort, setup=setup)

def test_selection_sort(benchmark):
    benchmark.pedantic(selection_sort, setup=setup)

def test_insert_sort(benchmark):
    benchmark.pedantic(insert_sort, setup=setup)

def test_counting_sort(benchmark):
    def setup_counting():
        return (random.sample(range(1, 1_000), 999),999), {}
    benchmark.pedantic(counting_sort, setup=setup_counting)
