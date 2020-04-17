from typing import List, TypeVar

T = TypeVar('T')


def bubble_sort(elems: List[T]) -> List[T]:
    """Sorts a list using the bubble sort algorithm"""
    if not elems:
        return elems
    
    for mx in range(len(elems), 0, -1):
        for idx in range(1, mx):
            if elems[idx - 1] > elems[idx]:
                elems[idx - 1], elems[idx] = elems[idx], elems[idx - 1]

    return elems


def selection_sort(elems: List[T]) -> List[T]:
    """Sorts a list using the selection sort algorithm"""
    if not elems:
        return elems
    n = len(elems)
    for i in range(0, n):
        smidx = i
        for j in range(i + 1, n):
            if elems[smidx] > elems[j]:
                smidx = j
        elems[i], elems[smidx] = elems[smidx], elems[i]
    return elems


def insert_sort(elems: List[T]) -> List[T]:
    """Sorts a list using the insertion sort algorithm"""
    if not elems:
        return elems
    for idx in range(1, len(elems)):
        search_idx, item = idx, elems[idx]
        while search_idx > 0 and elems[search_idx - 1] > item:
            elems[search_idx] = elems[search_idx - 1]
            search_idx -= 1
        elems[search_idx] = item
    return elems

__all__ = ['bubble_sort', 'selection_sort', 'insert_sort']

