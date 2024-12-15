'''
Original Question LC34: Find First and Last Position of Element in Sorted Array
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
If target is not found in the array, return [-1, -1].
You must write an algorithm with O(log n) runtime complexity.
Follow-up: 1. What changes are needed if the array is sorted in decreasing order?
ANS: Adjust the comparison logic in the binary_search function since the direction of "less than" and "greater than" is reversed.
'''

def searchRangeDecreasingOrder(nums, target):
    def binary_search(nums, target, is_searching_left):
        left = 0
        right = len(nums) - 1
        idx = -1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] > target:
                # right = mid - 1
                left = mid + 1
            elif nums[mid] < target:
                # left = mid + 1
                right = mid - 1
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
# arr_1 = [1, 5, 6, 8, 8, 12]
arr_1 = [12, 8, 8, 6, 5, 1]
target = 8
output = searchRangeDecreasingOrder(nums = arr_1, target = target)
print(output) # [1, 2]
