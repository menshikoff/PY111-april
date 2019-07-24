import heapq
from typing import Sequence, TypeVar

_Tt = TypeVar("T")


def sort(container: Sequence[_Tt]) -> Sequence[_Tt]:
    """
    Sort input container with merge sort

    :param container: container of elements to be sorted
    :return: container sorted in ascending order
    """
    
    if len(container) < 2:
        
        return container
  
    else:
        arr_l = container[0: len(container) // 2]
        arr_r = container[len(container) // 2: len(container)]
        
        container = [n for n in heapq.merge(sort(arr_l), sort(arr_r))]

    return container


if __name__ == '__main__':

    print(sort([18, 4, 16, 92, 158, 4, 176, 567, 2, 18, 4, 16, 2, 18, 49, 16, -2, -45, 0]))
