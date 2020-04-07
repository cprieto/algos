from sorting import *

def test_bubble_sort_is_none_when_none():
    assert bubble_sort(None) == None

def test_bubble_sort_sorted_list_is_sorted():
    assert bubble_sort([1, 2]) != None
    assert bubble_sort([1, 2]) == [1, 2]

def test_bubble_sort_unsorted_list_is_sorted():
    assert bubble_sort([5, 1, 4, 2, 8]) == [1, 2, 4, 5, 8]

def test_bubble_sort_empty_list_is_empty():
    assert bubble_sort([]) == []

def test_selection_sort_unsorted_returns_sorted():
    assert selection_sort([5, 1, 4, 2, 8]) == [1, 2, 4, 5, 8]

def test_selection_sort_empty_returns_empty():
    assert selection_sort([]) == []

def test_selection_sort_none_returns_none():
    assert selection_sort(None) == None
