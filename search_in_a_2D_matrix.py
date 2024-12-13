class Solution:
    # total time complexity o(logm + logn) --> O(log(m*n))

    # time complexity analysis: perform BS within a row, there's n ele in a row-->log(n)
    def binary_search(self, row, target):
        left, right = 0, len(row) - 1

        while left <= right:
            mid = (left + right) // 2
            if row[mid] == target:
                return True
            elif row[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return False

    # time complexity analysis: perform BS over rows --> O(logm)
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        top, bot = 0, rows - 1
        while top <= bot:
            mid_row = (top + bot) // 2
            if target < matrix[mid_row][0]:  # target < the first ele in that row --> go to the row above
                bot = mid_row - 1
            elif target > matrix[mid_row][cols - 1]:
                top = mid_row + 1
            else:
                # check if target is within the current row
                # perform binary search on that row
                return self.binary_search(matrix[mid_row], target)

        # no valid rows
        return False
