import time
from typing import List, Tuple

import networkx as nx


def calculate_subset_pairs(edges: List[Tuple[int, int, int]]) -> int:
    """
    Calculate the maximum saving by removing redundant edges from the network.

    Args:
        edges (List[Tuple[int, int, int]]): A list of tuples representing the edges of the network.
            Each tuple contains two integers representing the nodes connected by the edge and
            a third integer representing the weight of the edge.

    Returns:
        int: The maximum saving achieved by removing redundant edges.
    """
    G = nx.Graph()
    [G.add_edge(edge[0], edge[1], weight=edge[2]) for edge in edges]
    MST = nx.minimum_spanning_tree(G)
    return int(G.size(weight='weight') - MST.size(weight='weight'))


def read_network_file(file_path: str) -> List[Tuple[int, int, int]]:
    """
    Read the network data from a file.

    Args:
        file_path (str): The path to the file containing the network data.

    Returns:
        List[Tuple[int, int, int]]: A list of tuples representing the edges of the network.
    """
    with open(file_path, 'r') as file:
        return [(i, j, int(weight)) for i, line in enumerate(file.readlines())
                for j, weight in enumerate(line.strip().split(',')) if weight != '-']


if __name__ == "__main__":
    start_time = time.time()
    print(f"Answer = {calculate_subset_pairs(read_network_file('Problem_107/0107_network.txt'))}")
    print(f"Elapsed time: {time.time() - start_time:.2f} seconds")
    