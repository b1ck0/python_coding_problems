import unittest


def river_sizes(matrix):
    sizes = []
    visited = [[False for value in row] for row in matrix]

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if visited[i][j]:
                continue
            else:
                traverse_node(i, j, matrix, visited, sizes)

    return sizes


def traverse_node(i, j, matrix, visited, sizes):
    current_river_size = 0
    nodes_to_explore = [[i, j]]  # stack (depth-first-search)
    while len(nodes_to_explore):
        current_node = nodes_to_explore.pop()
        i = current_node[0]
        j = current_node[1]
        if visited[i][j]:
            continue
        else:
            visited[i][j] = True

        if matrix[i][j] == 0:
            continue
        else:
            current_river_size += 1

            unvisited_neighbours = get_unvisited_neighbours(i, j, matrix, visited)

            for neighbour in unvisited_neighbours:
                nodes_to_explore.append(neighbour)

    if current_river_size > 0:
        sizes.append(current_river_size)


def get_unvisited_neighbours(i, j, matrix, visited):
    unvisited_neighbours = []
    if i > 0 and not visited[i - 1][j]:
        unvisited_neighbours.append([i - 1, j])
    if i < len(matrix) - 1 and not visited[i + 1][j]:
        unvisited_neighbours.append([i + 1, j])
    if j > 0 and not visited[i][j - 1]:
        unvisited_neighbours.append([i, j - 1])
    if j < len(matrix[i]) - 1 and not visited[i][j + 1]:
        unvisited_neighbours.append([i, j + 1])

    return unvisited_neighbours


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        testInput = [[0]]
        expected = []
        self.assertEqual(sorted(river_sizes(testInput)), expected)

    def test_case_2(self):
        testInput = [[1]]
        expected = [1]
        self.assertEqual(sorted(river_sizes(testInput)), expected)

    def test_case_3(self):
        testInput = [[1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0]]
        expected = [1, 2, 3]
        self.assertEqual(sorted(river_sizes(testInput)), expected)

    def test_case_4(self):
        testInput = [[1, 0, 0, 1], [1, 0, 1, 0], [0, 0, 1, 0], [1, 0, 1, 0]]
        expected = [1, 1, 2, 3]
        self.assertEqual(sorted(river_sizes(testInput)), expected)

    def test_case_5(self):
        testInput = [[1, 0, 0, 1, 0], [1, 0, 1, 0, 0], [0, 0, 1, 0, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 0]]
        expected = [1, 2, 2, 2, 5]
        self.assertEqual(sorted(river_sizes(testInput)), expected)

    def test_case_6(self):
        testInput = [
            [1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0],
            [1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0],
            [0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1],
            [1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0],
            [1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1],
        ]
        expected = [1, 1, 2, 2, 5, 21]
        self.assertEqual(sorted(river_sizes(testInput)), expected)

    def test_case_7(self):
        testInput = [
            [1, 0, 0, 0, 0, 0, 1],
            [0, 1, 0, 0, 0, 1, 0],
            [0, 0, 1, 0, 1, 0, 0],
            [0, 0, 0, 1, 0, 0, 0],
            [0, 0, 1, 0, 1, 0, 0],
            [0, 1, 0, 0, 0, 1, 0],
            [1, 0, 0, 0, 0, 0, 1],
        ]
        expected = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        self.assertEqual(sorted(river_sizes(testInput)), expected)

    def test_case_8(self):
        testInput = [
            [1, 0, 0, 0, 0, 0, 1],
            [0, 1, 0, 0, 0, 1, 0],
            [0, 0, 1, 0, 1, 0, 0],
            [0, 0, 1, 1, 1, 0, 0],
            [0, 0, 1, 0, 1, 0, 0],
            [0, 1, 0, 0, 0, 1, 0],
            [1, 0, 0, 0, 0, 0, 1],
        ]
        expected = [1, 1, 1, 1, 1, 1, 1, 1, 7]
        self.assertEqual(sorted(river_sizes(testInput)), expected)

    def test_case_9(self):
        testInput = [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
        ]
        expected = []
        self.assertEqual(sorted(river_sizes(testInput)), expected)

    def test_case_10(self):
        testInput = [
            [1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1],
        ]
        expected = [49]
        self.assertEqual(sorted(river_sizes(testInput)), expected)

    def test_case_11(self):
        testInput = [[1, 1, 0, 0, 0, 0, 1, 1], [1, 0, 1, 1, 1, 1, 0, 1], [0, 1, 1, 0, 0, 0, 1, 1]]
        expected = [3, 5, 6]
        self.assertEqual(sorted(river_sizes(testInput)), expected)

    def test_case_12(self):
        testInput = [
            [1, 1, 0],
            [1, 0, 1],
            [1, 1, 1],
            [1, 1, 0],
            [1, 0, 1],
            [0, 1, 0],
            [1, 0, 0],
            [1, 0, 0],
            [0, 0, 0],
            [1, 0, 0],
            [1, 0, 1],
            [1, 1, 1],
        ]
        expected = [1, 1, 2, 6, 10]
        self.assertEqual(sorted(river_sizes(testInput)), expected)


if __name__ == "__main__":
    unittest.main()
