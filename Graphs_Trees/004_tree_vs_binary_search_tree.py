def tree_or_binary_search_tree(tree):
    """
    this is a mockup question which checks if a given tree is in fact a binary search tree
    assuming:
        - tree.root - root node
        - tree.left - left child [None if no child]
        - tree.right - right child [None if no child]

    :param tree: implementation of a tree
    :return: boolean
    """
    # implementation of a post-order traversal
    if tree.left is not None:
        if tree.root < tree.left.root:
            return False
        else:
            tree_or_binary_search_tree(tree.left)

    if tree.right is not None:
        if tree.root > tree.right.root:
            return False
        else:
            tree_or_binary_search_tree(tree.right)

    return True


if __name__ == "__main__":
    from BinaryTree import BinaryTree

    tree = BinaryTree(99)
    tree.insert_left(98)
    tree.insert_right(100)
    tree.left.insert_left(95)

    print(tree_or_binary_search_tree(tree))

    tree = BinaryTree(99)
    tree.insert_left(98)
    tree.insert_right(95)
    tree.left.insert_left(95)

    print(tree_or_binary_search_tree(tree))