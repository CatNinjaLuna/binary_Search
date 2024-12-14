'''
Original Question LC34: Find First and Last Position of Element in Sorted Array
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
If target is not found in the array, return [-1, -1].
You must write an algorithm with O(log n) runtime complexity.
Follow-up: What if the array has duplicates, but we only want to find one occurrence of the target?
ANS: The moment we find the target, we return its index --> avoid further exploration
'''
def searchRange(nums, target):
    def binary_search(nums, target):
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
                return mid

        # target not found
        return -1

    # Output could be any one index of 8 (e.g., 3 or 4)
    return binary_search(nums, target)


# TEST
arr_1 = [1, 5, 6, 8, 8, 12]
target = 8
output = searchRange(nums = arr_1, target = target)
print(output) # 4
