def broken_search(nums, target):
    start_index = 0
    end_index = len(nums) - 1

    while start_index <= end_index:
        mid_index = start_index + ((end_index - start_index) >> 1)

        if nums[mid_index] == target:
            return mid_index

        if nums[start_index] <= nums[mid_index]:
            if nums[start_index] <= target < nums[mid_index]:
                end_index = mid_index - 1
            else:
                start_index = mid_index + 1
        else:
            if nums[mid_index] < target <= nums[end_index]:
                start_index = mid_index + 1
            else:
                end_index = mid_index - 1
    return -1


def test():
    arr = [19, 21, 100, 101, 1, 4, 5, 7, 12]
    assert broken_search(arr, 5) == 6


if __name__ == '__main__':
    test()