
def left_bound(elem_, arr_):
	left = -1
	right = len(arr_)

	while right - left > 1:
		middle = (left + right) // 2

		if arr_[middle] < elem_:
			left = middle
		else:
			right = middle

	return left


def right_bound(elem_, arr_):
	left = -1
	right = len(arr_)

	while right - left > 1:

		middle = (left + right) // 2

		if arr_[middle] <= elem_:
			left = middle
		else:
			right = middle

	return right


def binary_search(elem, arr):
	"""
	Performs binary search of given element inside of array

	:param elem: element to be found
	:param arr: array where element is to be found
	:return: Index of element if it's presented in the arr, None otherwise
	"""

	if right_bound(elem, arr) - left_bound(elem, arr) == 1:
		return None
	else:
		return left_bound(elem, arr) + 1  # Чтобы пройти тест было решено выводить только одно первое найденное значение
