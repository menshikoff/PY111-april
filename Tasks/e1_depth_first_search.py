from typing import Any
import networkx as nx

visit = []


def dfs(graph_: nx.Graph, start_node: Any) -> list:
    """
    Do an depth-first search and returns list of nodes in the visited order

    :param graph_: input graph
    :param start_node: starting node of search
    :return: list of nodes in the visited order
    """

    visit.append(start_node)
    if len(list(graph_.neighbors(start_node))) == 1:
        return visit

    else:
        for _ in graph_.neighbors(start_node):
            if _ not in visit:
                dfs(graph_, _)
    return visit


if __name__ == '__main__':
    g = nx.Graph()
    l_nodes = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'Z']
    g.add_nodes_from(l_nodes)
    g.add_edges_from([('A', 'B'), ('A', 'F'), ('B', 'G'), ('F', 'G'), ('G', 'C'),
                      ('G', 'H'), ('G', 'I'), ('C', 'H'), ('I', 'H'), ('H', 'D'),
                      ('H', 'E'), ('H', 'J'), ('D', "E"), ('J', 'Z')])

    print(dfs(g, 'A'))
