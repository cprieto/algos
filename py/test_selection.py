from selection import selection_sort

def test_selection_sort_unsorted_returns_sorted():
    assert selection_sort([5, 1, 4, 2, 8]) == [1, 2, 4, 5, 8]

def test_selection_sort_empty_returns_empty():
    assert selection_sort([]) == []

def test_selection_sort_none_returns_none():
    assert selection_sort(None) == None
