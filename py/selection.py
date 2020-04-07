from typing import List, TypeVar
T = TypeVar('T')

def selection_sort(elems: List[T]) -> List[T]:
    """Sorts a list using the selection sort algorithm"""
    if not elems:
        return elems
    n = len(elems)
    for i in range(0, n):
        smidx = i
        for j in range(i + 1, n):
            print(j)
            if elems[smidx] > elems[j]:
                smidx = j
        elems[i], elems[smidx] = elems[smidx], elems[i]
    return elems
