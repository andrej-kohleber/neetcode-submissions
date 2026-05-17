class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        row = self.findRow(matrix, target)
        print(row)
        if row:
            left = 0
            right = len(row) - 1
            while left <= right:
                middle = left + (right - left) // 2
                if row[middle] == target:
                    return True
                elif row[middle] < target:
                    left = middle + 1
                else:
                    right = middle - 1

        return False

    def findRow(self, matrix: List[List[int]], target: int) -> List[int]:
        first_row = 0
        last_row = len(matrix) - 1

        while first_row <= last_row:
            middle = first_row + (last_row - first_row)

            if matrix[middle][0] <= target and matrix[middle][len(matrix[0]) - 1] >= target:
                return matrix[middle]

            if matrix[middle][0] < target:
                first_row = middle + 1
            else:
                last_row = middle - 1

        return []
        