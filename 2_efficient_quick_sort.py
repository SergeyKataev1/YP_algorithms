#87573211
def quicksort(users:list, lft:int, rgt:int):
    if lft >= rgt:
        return -1

    left, right = lft, rgt
    pivot = users[lft]

    while left <= right:
        while users[left] < pivot:
            left += 1
        while users[right] > pivot:
            right -= 1
        if left <= right:
            users[left], users[right] = users[right], users[left]
            left += 1
            right -= 1

    quicksort(users, lft, right)
    quicksort(users, left, rgt)


def data_sort(users:list):
    users[1] = -int(users[1])
    users[2] = int(users[2])
    return [users[1], users[2], users[0]]


def read_input():
    n = int(input())
    users = [data_sort(input().split()) for _ in range(n)]
    return users


def main():
    users = read_input()
    quicksort(users, lft=0, rgt=len(users) - 1)
    for username in users:
        print(username[2])


if __name__ == '__main__':
    main()