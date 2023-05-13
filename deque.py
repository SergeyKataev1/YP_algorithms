from typing import Tuple


class FullDekError(Exception):
    pass


class EmptyDekError(Exception):
    pass


class Deque:
    def __init__(self, max_size):
        self.__queue = [None] * max_size
        self.__max_n = max_size
        self.__head = 0
        self.__tail = 0
        self.__size = 0

    def is_empty(self):
        return self.__size <= 0

    def is_full(self):
        return self.__size >= self.__max_n

    def count_index(self, current_index, minus=1):
        result = (current_index + 1 * minus) % self.__max_n
        return result

    def push_back(self, item):
        if self.is_full():
            raise FullDekError
        else:
            self.__queue[self.__tail] = item
            self.__tail = self.count_index(self.__tail)
            self.__size += 1

    def push_front(self, item):
        if self.is_full():
            raise FullDekError
        else:
            new_head = self.count_index(self.__head, -1)
            self.__queue[new_head] = item
            self.__size += 1
            self.__head = new_head

    def pop_front(self):
        if self.is_empty():
            raise EmptyDekError
        item = self.__queue[self.__head]
        self.__queue[self.__head] = None
        self.__head = self.count_index(self.__head)
        self.__size -= 1
        return item

    def pop_back(self):
        if self.is_empty():
            raise EmptyDekError
        item = self.__queue[self.__tail-1]
        self.__queue[self.__tail-1] = None
        self.__tail = self.count_index(self.__tail, -1)
        self.__size -= 1
        return item

def read_input() -> Tuple[int, int]:
    num = int(input())
    n = int(input())
    queue = Deque(n)
    for num_command in range(num):
        command, *value = [x for x in input().strip().split()]
        try:
            a = getattr(queue, command)(*value)
            if a:
                print(a)
        except FullDekError:
            print('error')
        except EmptyDekError:
            print('error')


if __name__ == "__main__":
    read_input()