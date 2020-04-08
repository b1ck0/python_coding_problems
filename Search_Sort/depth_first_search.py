def dfs_visible_nodes(graph: dict, start_node: str) -> set:
    """
    :param graph:
    :param start_node:
    :return: set of nodes which are accessible from the start_node
    """
    visited, stack = set(), [start_node]  # using sets as setA - setB = difference between sets

    # while there are elements in the stack
    while stack:

        # get the most-recently added element
        node = stack.pop()

        # mark as visited if necessary
        if node not in visited:
            visited.add(node)

            # add the children of the current node which are not already visited at the end of the stack
            stack.extend(graph[node] - visited)

    # return the list/set of visited nodes
    return visited


def dfs_visible_nodes_recursive(graph: dict, start_node: str, visited=None) -> set:
    if visited is None:
        visited = set()

    visited.add(graph[start_node])

    for child in graph[start_node] - visited:
        dfs_visible_nodes_recursive(graph, child, visited)

    return visited


def dfs_all_possible_paths(graph: dict, start_node: str, end_node: str) -> list:
    stack = [(start_node, [start_node])]
    paths = []

    while stack:
        vertex, path = stack.pop()

        for next in graph[vertex] - set(path):
            if next == end_node:
                paths.append(path + [next])
            else:
                stack.append((next, path + [next]))

    return paths


def dfs_all_possible_paths_recursive(graph: dict, start_node: str, end_node: str, path=[]) -> list:
    path = path + [start_node]

    if start_node == end_node:
        return [path]

    if start_node not in graph:
        return []

    paths = []

    for node in graph[start_node]:
        if node not in path:
            new_paths = dfs_all_possible_paths_recursive(graph, node, end_node, path)

            for new_paths in new_paths:
                paths.append(new_paths)

    return paths


if __name__ == "__main__":
    # children of the nodes are sets due to reasons explained above
    graph = {
        'A': {'B', 'C'},
        'B': {'A', 'D', 'E'},
        'C': {'A', 'F'},
        'D': {'B'},
        'E': {'B', 'F'},
        'F': {'C', 'E'}
    }

    print(dfs_visible_nodes(graph, 'D'))
    print(dfs_all_possible_paths(graph, 'A', 'F'))
    print(dfs_all_possible_paths_recursive(graph, 'D', 'A'))
