'''
Given an array of integers nums that is unsorted,
find the starting and ending position of a given target value.
If target is not found in the array, return [-1, -1].
Propose a brute force solution with O(n) time complexity
'''

'''
def searchRangeUnsorted(nums, target):
    target_counter = 0 # count occrence of target
    res = []
    for i in range(len(nums)):
        # comparison between nums[i] and target
        if nums[i] == target:
            target_counter += 1
            res.append(i)

    return res
'''


def searchRangeUnsorted(nums, target):
    # O(nlogn) time
    nums = sorted(nums) # nums.sort

    def binary_search(nums, target, is_search_left):
        left, right = 0, len(nums)-1
        idx = -1
        while left <= right:
            mid = (left + right) // 2
            if target < nums[mid]: # search on left half
                right = mid - 1
            elif nums[mid] < target: # search on right half
                left = mid + 1
            else: # target ==  nums[mid], continue search for occren idx
                idx = mid
                if is_search_left:
                    right = mid - 1
                else:
                    left = mid + 1
        return idx

    left = binary_search(nums, target, True) # O(logn)
    right = binary_search(nums, target, False) # O(logn)
    return [left, right]




# TEST
arr_1 = [5, 1, 3, 6, 2, 9, 1]  # [1,1,2,3,5,6,9]
target = 1
output = searchRangeUnsorted(nums = arr_1, target = 1)
print(output) # [0,1]


