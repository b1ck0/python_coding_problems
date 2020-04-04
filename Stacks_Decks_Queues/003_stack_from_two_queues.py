class Stack2Queues(object):

    def __init__(self):
        self.queue_a = []
        self.queue_b = []

    def push(self, element):
        self.queue_a.insert(0, element)

    def pop(self):
        self.queue_b = [self.queue_a.pop(0) for i in range(len(self.queue_a))]
        latest_element = self.queue_b.pop(0)
        self.queue_a = [self.queue_b.pop(0) for i in range(len(self.queue_b))]
        return latest_element


if __name__ == "__main__":
    stack = Stack2Queues()

    for i in range(10):
        stack.push(i)

    for i in range(10):
        print(stack.pop())
