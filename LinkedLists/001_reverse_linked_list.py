class Node(object):

    def __init__(self, value):
        self.value = value
        self.child = None


def reverse_linked_list(head: Node) -> Node:
    previous_pointer, current_node, next_pointer = None, head, None

    while current_node:
        next_pointer = current_node.child
        current_node.child = previous_pointer
        previous_pointer = current_node
        current_node = next_pointer

    return previous_pointer


if __name__ == "__main__":
    a = Node(1)
    b = Node(2)
    c = Node(3)

    print("{0.value}, {1.value}, {2.value}".format(a, b, c))

    a.child = b
    b.child = c

    a = reverse_linked_list(a)

    print("{0.value}, {1.value}, {2.value}".format(a, b, c))
