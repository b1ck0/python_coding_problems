class BinaryTree(object):

    def __init__(self, root):
        self.root = root
        self.left = None
        self.right = None

    def insert_left(self, node):
        if self.left is None:
            self.left = BinaryTree(node)
        else:
            new_left = BinaryTree(node)
            new_left.left = self.left
            self.left = new_left

    def insert_right(self, node):
        if self.right is None:
            self.right = BinaryTree(node)
        else:
            new_right = BinaryTree(node)
            new_right.right = self.right
            self.right = new_right

    def preorder_traversal(self):  # depth - first traversal
        print(self.root)
        if self.left is not None:
            self.left.preorder_traversal()
        if self.right is not None:
            self.right.preorder_traversal()

    def postorder_traversal(self):
        if self.left is not None:
            self.left.postorder_traversal()
        if self.right is not None:
            self.right.postorder_traversal()
        print(self.root)

    def inorder_traversal(self):
        if self.left is not None:
            self.left.inorder_traversal()
        print(self.root)
        if self.right is not None:
            self.right.inorder_traversal()


def print_tree(tree):
    if not tree:
        return

    nodes = [tree]

    current_count = 1
    next_count = 0

    while len(nodes) != 0:
        current_node = nodes.pop(0)
        current_count -= 1

        print(current_node.root, end=' ')

        if current_node.left:
            nodes.append(current_node.left)
            next_count += 1

        if current_node.right:
            nodes.append(current_node.right)
            next_count += 1

        if current_count == 0:
            print()
            current_count, next_count = next_count, current_count


if __name__ == "__main__":
    tree = BinaryTree(1)
    tree.insert_left(2)
    tree.insert_right(3)
    tree.left.insert_left(4)
    tree.left.insert_right(5)
    tree.right.insert_left(6)
    tree.right.insert_right(7)

    print_tree(tree)
