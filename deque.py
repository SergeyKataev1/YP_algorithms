#87240413
from typing import Tuple


class FullDequeError(Exception):
    pass


class EmptyDequeError(Exception):
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
            raise FullDequeError
        else:
            self.__queue[self.__tail] = item
            self.__tail = self.count_index(self.__tail)
            self.__size += 1

    def push_front(self, item):
        if self.is_full():
            raise FullDequeError
        else:
            new_head = self.count_index(self.__head, -1)
            self.__queue[new_head] = item
            self.__size += 1
            self.__head = new_head

    def pop_front(self):
        if self.is_empty():
            raise EmptyDequeError
        item = self.__queue[self.__head]
        self.__queue[self.__head] = None
        self.__head = self.count_index(self.__head)
        self.__size -= 1
        return item

    def pop_back(self):
        if self.is_empty():
            raise EmptyDequeError
        item = self.__queue[self.__tail-1]
        self.__queue[self.__tail-1] = None
        self.__tail = self.count_index(self.__tail, -1)
        self.__size -= 1
        return item

def read_input() -> Tuple[int, int]:
    num = int(input())
    n = int(input())
    return num, n

def item_input():
    item = input().split()
    return item

def commands(num, n):
    queue = Deque(n)
    for num_command in range(num):
        try:
            item = item_input()
            a = (getattr(queue, item[0])()) if len(item) == 1 else getattr(
                queue, item[0])(item[1])
            if a:
                print(a)
        except FullDequeError:
            print('error')
        except EmptyDequeError:
            print('error')

def main():
    num , n = read_input()
    commands(num, n)


if __name__ == "__main__":
    main()