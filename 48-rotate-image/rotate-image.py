from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        def layerRotation(r, c, rows, cols):
            # Store values
            top = [matrix[r][i] for i in range(c, cols)]
            right = [matrix[i][cols - 1] for i in range(r + 1, rows)]
            bottom = [matrix[rows - 1][i] for i in range(cols - 1, c - 1, -1)]
            left = [matrix[i][c] for i in range(rows - 1, r, -1)]
            
            # Rotate values
            # top -> right
            for i in range(len(top)):
                matrix[r + i][cols - 1] = top[i]
            # right -> bottom
            for i in range(len(right)):
                matrix[rows - 1][cols - 1 - i] = right[i]
            # bottom -> left
            for i in range(len(bottom)):
                matrix[rows - 1 - i][c] = bottom[i]
            # left -> top
            for i in range(len(left)):
                matrix[r][c + i] = left[i]

        n = len(matrix)
        for r in range(n // 2):
            for c in range(r, n - r - 1):
                # Store the current cell in a temporary variable
                temp = matrix[r][c]
                # Move values from left to top
                matrix[r][c] = matrix[n - 1 - c][r]
                # Move values from bottom to left
                matrix[n - 1 - c][r] = matrix[n - 1 - r][n - 1 - c]
                # Move values from right to bottom
                matrix[n - 1 - r][n - 1 - c] = matrix[c][n - 1 - r]
                # Assign temp to right
                matrix[c][n - 1 - r] = temp