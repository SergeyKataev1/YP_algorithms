def read_inputs():
    a = int(input())
    b = int(input())
    return a, b


def get_sum(a, b):
    return a + b


def main():
    a, b = read_inputs()
    print(get_sum(a, b))


if __name__ == '__main__':
    main()