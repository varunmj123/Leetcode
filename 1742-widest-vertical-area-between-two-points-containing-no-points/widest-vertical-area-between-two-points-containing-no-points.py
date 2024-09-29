from typing import List

class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        # Sort points based on their x-coordinates
        points.sort(key=lambda x: x[0])
        
        # Initialize maximum width
        max_width = 0
        
        # Iterate through sorted points to find maximum gap
        for i in range(1, len(points)):
            width = points[i][0] - points[i - 1][0]
            max_width = max(max_width, width)
        
        return max_width
