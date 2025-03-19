class Solution:
    """
    T: O(log(m*n)), S: O(1)
    """
    def searchMatrixBrutue(self, matrix: list[list[int]], target: int) -> bool:
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == target:
                    return True
        return False

    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        l, r = 0, ROWS * COLS-1

        while l <= r:
            m = l + (r - l)//2
            row, col = m//COLS, m%COLS

            if target > matrix[row][col]:
                l=m+1
            elif target < matrix[row][col]:
                r=m-1
            else:
                return True
        return False


if __name__ == "__main__":
    assert Solution().searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3) == True
    assert Solution().searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13) == False