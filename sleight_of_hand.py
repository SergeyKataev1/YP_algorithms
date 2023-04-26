#86449578
def get_max_points(matrix, k):
    points = 0
    count = [0] * 16
    for number in matrix:
        if number != '.':
            count[int(number)] += 1
    for number in count:
        if 0 < number <= k * 2:
            points += 1
    return points


def read_input():
    k = int(input())
    matrix = [i for i in range(4) for i in input().strip()]
    return matrix, k


def main():
    matrix, k = read_input()
    print(get_max_points(matrix, k))


if __name__ == '__main__':
    main()