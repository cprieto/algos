from typing import List, TypeVar

T = TypeVar('T')


def bubble_sort(elems: List[T]) -> None:
    """Sorts a list using the bubble sort algorithm, this is sort in-place"""
    if not elems:
        return
    
    for mx in range(len(elems), 0, -1):
        for idx in range(1, mx):
            if elems[idx - 1] > elems[idx]:
                elems[idx - 1], elems[idx] = elems[idx], elems[idx - 1]


def selection_sort(elems: List[T]) -> None:
    """Sorts a list using the selection sort algorithm, this is sort in-place"""
    if not elems:
        return

    n = len(elems)
    for i in range(0, n):
        smidx = i
        for j in range(i + 1, n):
            if elems[smidx] > elems[j]:
                smidx = j
        elems[i], elems[smidx] = elems[smidx], elems[i]


def insert_sort(elems: List[T]) -> None:
    """Sorts a list using the insertion sort algorithm, this is sort in-place"""
    if not elems:
        return

    for idx in range(1, len(elems)):
        search_idx, item = idx, elems[idx]
        while search_idx > 0 and elems[search_idx - 1] > item:
            elems[search_idx] = elems[search_idx - 1]
            search_idx -= 1
        elems[search_idx] = item


def counting_sort(elems: List[int], upto: int):
    """Sorts a list of integers using counting sort, this is sort in-place and can be applied only to possitive integers"""
    result = [0] * (upto + 1)
    for i in range(0, len(elems)):
        result[elems[i]] += 1
    
    current = 0
    for i in range(0, len(result)):
        if result[i]:
            for n in range(0, result[i]):
                elems[current] = i
                current += 1
            

__all__ = ['bubble_sort', 'selection_sort', 'insert_sort', 'counting_sort']
