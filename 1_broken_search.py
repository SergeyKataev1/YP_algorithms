def broken_search(nums, target):
    left = 0
    right = len(nums) - 1
    while left <= right:
        midl = (left + right) // 2
        if nums[midl] == target:
            return midl
        elif nums[left] <= nums[midl]:
            if nums[left] <= target < nums[midl]:
                right = midl - 1
            else:
                left = midl + 1
        else:
            if nums[midl] < target <= nums[right]:
                left = midl + 1
            else:
                right = midl - 1
    return -1


def read_input():
    _ = int(input())
    k = int(input())
    nums = list(map(int, input().split()))
    return k, nums


def main():
    k, nums = read_input()
    print(broken_search(nums, k))


if __name__ == '__main__':
    main()