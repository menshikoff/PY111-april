"""
My little Queue
"""

my_queue = []


def enqueue(elem) -> None:
	"""
	Operation that add element to the end of the queue

	:param elem: element to be added
	:return: Nothing
	"""
	return my_queue.append(elem)


def dequeue():
	"""
	Return element from the beginning of the queue

	:return: dequeued element
	"""
	global my_queue
	if my_queue:
		x = my_queue[0]
		my_queue = my_queue[1:]
		return x


def peek(ind: int = 0):
	"""
	Allow you to see at the element in the queue without dequeuing it

	:param ind: index of element (count from the beginning)
	:return: peeked element
	"""
	if my_queue:
		return my_queue[ind]


def clear() -> None:
	"""
	Clear my queue

	:return: None
	"""
	global my_queue
	my_queue.clear()

	return None


if __name__ == '__main__':
	print(my_queue)
	enqueue(10)
	enqueue(15)
	enqueue(16)
	print(my_queue)
	print(peek(5))
