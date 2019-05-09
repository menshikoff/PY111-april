def stairway_path(stairway: list) -> int:
	"""
	Calculate min cost of getting to the top of stairway if agent can go on next or through one step.

	:param stairway: list of ints, where each int is a cost of appropriate step
	:return: minimal cost of getting to the top
	"""

	cost = [stairway[0], stairway[1]]

	for i in range(2, len(stairway)):
		cost.append(stairway[i]+min(cost[i-1], cost[i-2]))

	return cost[-1]


if __name__ == '__main__':

	print(stairway_path([5, 11, 43, 2, 23, 43, 22, 12, 6, 8]))
