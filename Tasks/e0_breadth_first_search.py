from typing import Any
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import Tasks.a1_my_queue as mq


def bfs(g: nx.Graph, start_node: Any) -> list:
	"""
	Do an breadth-first search and returns list of nodes in the visited order

	:param g: input graph
	:param start_node: starting node for search
	:return: list of nodes in the visited order
	"""

	visit = [start_node]
	mq.enqueue([start_node])
	dict_ = {x: [] for x in g.nodes}

	while mq.my_queue:
		edges_ = list(g.edges(mq.dequeue()))

		for item in edges_:
			if item[1] not in visit:
				visit.append(item[1])
				dict_[item[1]] = dict_[item[0]] + list(item[0])
				mq.enqueue(item[1])

	print(g, start_node)
	print(dict_)
	return visit


if __name__ == '__main__':

	g = nx.Graph()
	l_nodes = ['A', 'B', 'C', 'D', 'E']
	g.add_nodes_from(l_nodes)
	g.add_edge('A', 'B')
	g.add_edge('A', 'C')
	g.add_edge('B', 'D')
	g.add_edge('C', 'D')
	g.add_edge('D', 'E')

	print(bfs(g, 'A'))
