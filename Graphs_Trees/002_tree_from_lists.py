def binary_tree(root):
    # return [root, [left_child], [right_child]]
    return [root, [], []]


def get_left_child(root):
    return root[1]


def get_right_child(root):
    return root[2]


def insert_left_child(root, new_left_branch):
    current_left_branch = root.pop(1)

    if len(current_left_branch) > 0:
        root.insert(1, [new_left_branch, current_left_branch, []])
    else:
        root.insert(1, [new_left_branch, [], []])


def insert_right_child(root, new_right_branch):
    current_right_branch = root.pop(2)

    if len(current_right_branch) > 0:
        root.insert(2, [new_right_branch, [], current_right_branch])
    else:
        root.insert(2, [new_right_branch, [], []])


if __name__ == "__main__":
    tree = binary_tree(10)
    insert_left_child(tree, 15)
    insert_left_child(tree[1], 25)
    insert_left_child(tree[1][1], 35)

    print(get_left_child(tree))
