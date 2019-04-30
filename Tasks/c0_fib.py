def fib_recursive(n: int) -> int:
	"""
	Calculate n-th number of Fibonacci sequence using recursive algorithm

	:param n: number of item
	:return: Fibonacci number
	"""

	if n < 0 or type(n) != int:
		raise ValueError("Input argument should be positive and int!")

	if n == 0:
		return 0
	if n == 1:
		return 1

	return fib_recursive(n-1) + fib_recursive(n-2)


def fib_iterative(n: int) -> int:
	"""
	Calculate n-th number of Fibonacci sequence using iterative algorithm

	:param n: number of item
	:return: Fibonacci number
	"""
	if n < 0 or type(n) != int:
		raise ValueError("Input argument should be positive and int!")

	if n == 0:
		return 0
	if n == 1:
		return 1

	fib_l = [0, 1]

	for i in range(2, n+1):
		fib_l.append(fib_l[i-2] + fib_l[i-1])

	return fib_l.pop()
