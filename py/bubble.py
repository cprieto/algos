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
