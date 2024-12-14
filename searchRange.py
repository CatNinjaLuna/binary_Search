def searchRange(nums, target):
    def binary_search(nums, target, is_searching_left):
        left = 0
        right = len(nums) - 1
        idx = -1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:  # nums[mid] == target
                idx = mid
                if is_searching_left:
                    right = mid - 1
                else:
                    left = mid + 1

        return idx

    left = binary_search(nums, target, True)
    right = binary_search(nums, target, False)

    return [left, right]

# TEST
arr_1 = [1, 5, 6, 8, 8, 12]
target = 8
output = searchRange(nums = arr_1, target = 8)
print(output)
