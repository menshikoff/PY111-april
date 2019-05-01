def factorial_recursive(n: int) -> int:
	"""
	Calculate factorial of number n (> 0) in recursive way
	:param n: int > 0
	:return: factorial of n
	"""

	if n < 0:
		raise ValueError("Input argument should be positive!")
	if n == 1:
		return 1
	return factorial_recursive(n-1)*n


def factorial_iterative(n: int) -> int:
	"""
	Calculate factorial of number n (> 0) in iterative way

	:param n: int > 0
	:return: factorial of n
	"""

	if n < 0:
		raise ValueError("Input argument should be positive!")

	if n == 1:
		res = 1
	else:
		res = 1
		for i in range(2, n+1):
			res *= i

	return res
