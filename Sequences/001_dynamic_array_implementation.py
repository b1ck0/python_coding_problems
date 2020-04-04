import ctypes


class DynamicArray(object):
    """
    Own implementation of a dynamic array similar to build-in list data structure in Python
    """

    def __init__(self):
        self.n = 0
        self.capacity = 1
        self.A = self.make_array(self.capacity)

    def __len__(self):
        return self.n

    def __getitem__(self, item):
        if not 0 <= item < self.n:
            return IndexError(f'Element {item} is out of bounds!')

        return self.A[item]

    def append(self, item):
        if self.n == self.capacity:
            self._resize()

        self.A[self.n] = item
        self.n += 1

    def _resize(self):
        new_capacity = self.capacity * 2

        B = self.make_array(new_capacity)

        for i in range(self.n):
            B[i] = self.A[i]

        self.A = B
        self.capacity = new_capacity

    @staticmethod
    def make_array(new_capacity):
        return (new_capacity * ctypes.py_object)()


if __name__ == '__main__':
    array = DynamicArray()
    array.append(1)
    array.append(2)
    print(len(array))
