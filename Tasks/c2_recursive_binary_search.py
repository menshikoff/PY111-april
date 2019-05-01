def binary_search(elem, arr):
	"""
	Performs binary search of given element inside of array (using recursive way)

	:param elem: element to be found
	:param arr: array where element is to be found
	:return: Index of element if it's presented in the arr, None otherwise
	"""

	if arr[len(arr)//2] == elem:
		return len(arr)//2

	if not len(arr)-1 and arr[0] != elem:
		return None

	if arr[len(arr)//2] > elem:
		return None if binary_search(elem, arr[: len(arr) // 2]) is None \
			else binary_search(elem, arr[: len(arr)//2])
	if arr[len(arr)//2] < elem:
		return None if binary_search(elem, arr[len(arr)//2:]) is None \
			else (binary_search(elem, arr[len(arr)//2:]) + len(arr)//2)
