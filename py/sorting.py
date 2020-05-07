from typing import List, TypeVar

T = TypeVar('T')


def bubble_sort(elems: List[T]) -> List[T]:
    """Sorts a list using the bubble sort algorithm"""
    if not elems:
        return elems
    
    items = elems.copy()
    for mx in range(len(items), 0, -1):
        for idx in range(1, mx):
            if items[idx - 1] > items[idx]:
                items[idx - 1], items[idx] = items[idx], items[idx - 1]

    return items


def selection_sort(elems: List[T]) -> List[T]:
    """Sorts a list using the selection sort algorithm"""
    if not elems:
        return elems
    n, items = len(elems), elems.copy()
    for i in range(0, n):
        smidx = i
        for j in range(i + 1, n):
            if items[smidx] > items[j]:
                smidx = j
        items[i], items[smidx] = items[smidx], items[i]
    return items


def insert_sort(elems: List[T]) -> List[T]:
    """Sorts a list using the insertion sort algorithm"""
    if not elems:
        return elems
    items = elems.copy()

    for idx in range(1, len(items)):
        search_idx, item = idx, items[idx]
        while search_idx > 0 and items[search_idx - 1] > item:
            items[search_idx] = items[search_idx - 1]
            search_idx -= 1
        items[search_idx] = item
    return items

__all__ = ['bubble_sort', 'selection_sort', 'insert_sort']

