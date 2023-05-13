import operator

OPERATORS = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.floordiv
}


class Stack:
    def __init__(self):
        self.array = []
        self.size = 0

    def push(self, item):
        self.size += 1
        self.array.append(item)

    def pop(self):
        if self.is_empty:
            raise IndexError
        self.size -= 1
        return self.array.pop()

    @property
    def is_empty(self):
        return self.size == 0


def calculator(input_data):
    
    stack = Stack()
    for item in input_data:
        operation = OPERATORS.get(item)
        stack.push(
            operation(*[stack.pop(), stack.pop()][::-1])
            if operation else int(item)
        )
    return stack.pop()


if __name__ == '__main__':
    input_data = input().split()
    print(calculator(input_data))