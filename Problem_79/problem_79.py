import time
from collections import defaultdict


def analyze_keylog(entries: list[str]) -> str:
    """
    Analyze the keylog entries to determine the shortest possible secret passcode.

    Args:
        entries (list[str]): The keylog entries.

    Returns:
        str: The shortest possible secret passcode.
    """
    graph = defaultdict(set)
    nodes = set()
    for entry in entries:
        nodes.update(list(entry))
        for i in range(2):
            graph[entry[i]].add(entry[i+1])
    passcode = ''
    while nodes:
        for node in nodes:
            if not any(node in graph[neighbour] for neighbour in nodes if neighbour != node):
                passcode += node
                nodes.remove(node)
                break
    return passcode


if __name__ == "__main__":
    start_time = time.time()
    with open('Problem_79\\0079_keylog.txt', 'r') as file:
        entries = [line.strip() for line in file]
    print(f"Answer = {analyze_keylog(entries)}")
    print(f"Elapsed time: {time.time() - start_time:.2f} seconds")
