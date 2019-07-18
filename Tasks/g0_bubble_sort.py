from typing import Sequence, TypeVar

_Tt = TypeVar("T")


def sort(container: Sequence[_Tt]) -> Sequence[_Tt]:
    """
    Sort input container with bubble sort

    :param container: container of elements to be sorted
    :return: container sorted in ascending order
    """

    for i in range(len(container)-1):

        n = 0

        while not n == len(container)-1:
            if container[n] > container[n+1]:
                container[n], container[n+1] = container[n+1], container[n]
            n += 1

    return container


if __name__ == '__main__':

    print(sort([10, 4, 5, 6, 9, 8, 56, 67, 0, -2]))

