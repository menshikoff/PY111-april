from typing import Sequence, TypeVar
import random
import heapq

_Tt = TypeVar("T")


def sort(container: Sequence[_Tt]) -> Sequence[_Tt]:
	"""
	Sort input container with quick sort

	:param container: container of elements to be sorted
	:return: container sorted in ascending order
	"""
	
	if len(container) < 2:
		return container
	
	else:
	
		pivot = random.choice(container)
	
		lp = 0
		rp = len(container) - 1
	
		while lp != rp:
	
			if container[lp] <= pivot:
				lp += 1
	
			elif container[lp] >= pivot:
				if container[rp] > pivot:
					rp -= 1
				elif container[rp] <= pivot:
					container[lp], container[rp] = container[rp], container[lp]
					lp += 1
	
	container_l = container[0: lp]
	container_r = container[lp: len(container)]
		
	container = [n for n in heapq.merge(sort(container_l), sort(container_r))]
	
	
	return container


if __name__ == '__main__':
	
	print(sort([1, 4, 15, 12, 6, 9, 56, 43, 2, 34, 23, 8, 11, 7, 35, 41, 22, 33, 89]))
