"""
Priority Queue

Queue priorities are from 0 to 5
"""

pri_queue = {x: [] for x in range(0, 6)}


def enqueue(elem, priority: int = 0) -> None:
	"""
	Operation that add element to the end of the queue

	:param elem: element to be added
	:param priority: priority of the element
	:return: Nothing
	"""

	pri_queue[priority].append(elem)

	return None


def dequeue():
	"""
	Return element from the beginning of the queue

	:return: dequeued element
	"""

	if not any(pri_queue[ind] for ind in range(0, 6)):
		return None

	for ind in range(0, 6):
		if pri_queue[ind]:
			buff = pri_queue[ind][0]
			pri_queue[ind] = pri_queue[ind][1:]
			return buff


def peek(ind: int = 0, priority: int = 0):
	"""
	Allow you to see at the element in the queue without dequeuing it

	:param ind: index of element (count from the beginning)
	:param priority: mining of the queue priority
	:return: peeked element
	"""

	try:
		return pri_queue[priority][ind]

	except IndexError:
		return None


def clear() -> None:
	"""
	Clear my queue

	:return: None
	"""

	for ind in range(0, 6):
		pri_queue[ind].clear()

	return None
