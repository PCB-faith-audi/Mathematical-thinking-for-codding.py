from collections import deque

# Sample graph represented as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# DFS using recursion
def dfs_recursive(graph, start, visited=None):
    if start not in graph:
        return set()
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=' ')
    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)
    return visited


def bfs(graph, start):
    if start not in graph:
        return set()
    visited = set()
    queue = deque([start])
    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            visited.add(vertex)
            print(vertex, end=" ")
            queue.extend([n for n in graph.get(vertex, []) if n not in visited])
    print()
    return visited


if __name__ == "__main__":
    print("DFS Recursive starting from A:")
    dfs_recursive(graph, 'A')
    print("\n")

    print("BFS Traversal starting from A:")
    bfs(graph, 'A')