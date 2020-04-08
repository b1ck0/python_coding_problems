import collections


def bfs_visible_nodes(graph: dict, start_node: str) -> set:
    visited, deck = set(), collections.deque()
    deck.append(start_node)

    while deck:
        node = deck.popleft()

        if node not in visited:
            visited.add(node)
            deck.extend(graph[node] - visited)

    return visited


def bfs_all_possible_paths(graph: dict, start_node: str, end_node: str) -> list:
    paths = {start_node: [start_node]}
    deck = collections.deque(start_node)

    if start_node == end_node:
        return paths[start_node]

    if end_node not in graph:
        return []

    while deck:
        node = deck.popleft()

        for child in graph[node]:
            if child not in paths:
                paths[child] = paths[node] + [child]
                deck.append(child)

    return paths[end_node]


def bfs_shortest_path(graph: dict, start_node: str, end_node: str) -> list:
    path, deck = {start_node: [start_node]}, collections.deque(start_node)

    if start_node == end_node:
        return path[start_node]

    if end_node not in graph:
        return []

    while deck:
        node = deck.popleft()

        for child in graph[node]:
            if child not in path:
                path[child] = path[node] + [child]
                deck.append(child)

    return path[end_node]


if __name__ == "__main__":
    graph = {
        'A': {'B', 'C'},
        'B': {'A', 'D', 'E'},
        'C': {'A', 'F'},
        'D': {'B'},
        'E': {'B', 'F'},
        'F': {'C', 'E'}
    }

    print(bfs_visible_nodes(graph, 'D'))
    print(bfs_all_possible_paths(graph, 'A', 'F'))
    print(bfs_shortest_path(graph, 'F', 'B'))
