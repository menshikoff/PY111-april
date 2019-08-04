from typing import Any
import networkx as nx
import math
import Tasks.a1_my_queue as mq


def dijkstra_algo(graph_weigted: nx.DiGraph, starting_node: Any) -> dict:
	"""
	Count shortest paths from starting node to all nodes of graph g
	:param graph_weigted: Graph from NetworkX
	:param starting_node: starting node from g
	:return: dict like {'node1': 0, 'node2': 10, '3': 33, ...} with path costs, where nodes are nodes from g
	"""

	for node in graph_weigted:
		graph_weigted.nodes[node]['way'] = math.inf
	graph_weigted.nodes[starting_node]['way'] = 0
	
	mq.enqueue(starting_node)
	
	while mq.my_queue:
		c_node = mq.dequeue()
		for _ in graph_weigted.neighbors(c_node):
			if graph_weigted.nodes[c_node]['way'] + \
					graph_weigted.get_edge_data(c_node, _)['weight'] < graph_weigted.nodes[_]['way']:
				graph_weigted.nodes[_]['way'] = graph_weigted.nodes[c_node]['way'] + \
												graph_weigted.get_edge_data(c_node, _)['weight']
				mq.enqueue(_)

	dict_ = {x: graph_weigted.nodes[x]['way'] for x in list(graph_weigted.nodes)}

	print(graph_weigted, starting_node)
	return dict_


if __name__ == '__main__':

	graph_w = nx.DiGraph()
	graph_w.add_nodes_from("ABCDEFG")
	graph_w.add_weighted_edges_from([
		("A", "B", 1),
		("B", "C", 3),
		("C", "E", 4),
		("E", "F", 3),
		("B", "E", 8),
		("C", "D", 1),
		("D", "E", 2),
		("B", "D", 2),
		("D", "G", 1),
		("D", "A", 2)])

	# nx.draw(graph_w, with_labels=True)
	# plt.show()
	# print(graph_w.adj)
	# print(graph_w.get_edge_data('B', 'C')['weight'])
	print(dijkstra_algo(graph_w, 'A'))
