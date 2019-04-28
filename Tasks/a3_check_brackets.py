import Tasks.a0_my_stack as stack


def check_brackets(brackets_row: str) -> bool:

	"""
	Check whether input string is a valid bracket sequence
	:param brackets_row: input string to be checked
	:return: True if valid, False otherwise
	"""

	stack.clear()

	for char in brackets_row.__iter__():
		if char == ')' and not stack.my_stack:
			return False
		if char == '(':
			stack.push(char)
		if char == ')' and stack.my_stack:
			stack.pop()

	if stack.my_stack:
		return False

	return True
