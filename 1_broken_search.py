#87544339
def broken_search(nums:list, target:int):
    start_index = 0
    end_index = len(nums) - 1

    while start_index <= end_index:
        midl_index = start_index + ((end_index - start_index) >> 1)

        if nums[midl_index] == target:
            return midl_index

        if nums[start_index] <= nums[midl_index]:
            if nums[start_index] <= target < nums[midl_index]:
                end_index = midl_index - 1
            else:
                start_index = midl_index + 1
        else:
            if nums[midl_index] < target <= nums[end_index]:
                start_index = midl_index + 1
            else:
                end_index = midl_index - 1
    return -1
