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


if __name__ == "__main__":
    tree = BinaryTree(10)
    tree.insert_left(20)
    tree.insert_left(30)

    tree.preorder_traversal()
    print("*" * 50)
    tree.postorder_traversal()
    print("*" * 50)
    tree.inorder_traversal()
