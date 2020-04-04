class Queue2Stacks(object):

    def __init__(self):
        self.stack_a = []
        self.stack_b = []

    def enqueue(self, element):
        self.stack_a.append(element)  # storing an element at the end of stack_a

    def dequeue(self):
        self.stack_b = [self.stack_a.pop() for i in range(len(self.stack_a))]  # reversing stack_a into stack_b
        first_in_element = self.stack_b.pop()
        self.stack_a = [self.stack_b.pop() for i in range(len(self.stack_b))]  # reversing stack_b into stack_a
        return first_in_element


if __name__ == "__main__":
    queue = Queue2Stacks()

    for i in range(10):
        queue.enqueue(i)

    for i in range(10):
        print(queue.dequeue())
