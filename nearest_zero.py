#86617115
from typing import List, Tuple


def get_distance(houses: List[int], n: int) -> list:
    distanse = [n] * n
    zero = [i for i in range(n) if houses[i] == 0]
    first_zero = zero[0]
    last_zero = zero[-1]

    for number in range(first_zero, n):
        if houses[number] != 0:
            distanse[number] = distanse[number - 1] + 1
        else:
            distanse[number] = 0
    for number in range(last_zero, first_zero, -1):
        if houses[number] != 0:
            distanse[number] = min(distanse[number], distanse[number + 1] + 1)
        else:
            distanse[number] = 0
    for number in range(first_zero - 1, -1, -1):
        distanse[number] = distanse[number + 1] + 1
    return distanse


def read_input() -> Tuple[List[int], int]:
    n = int(input())
    houses = list(int(x) for x in input().split())
    return houses, n


def main():
    houses, n = read_input()
    print(" ".join(map(str, get_distance(houses, n))))


if __name__ == '__main__':
    main()