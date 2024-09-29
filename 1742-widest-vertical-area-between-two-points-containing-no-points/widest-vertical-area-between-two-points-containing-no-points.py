from typing import List

class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        # Extract and sort unique x-coordinates
        x_coords = sorted(set(point[0] for point in points))
        
        # Initialize maximum width
        max_width = 0
        
        # Iterate through sorted x-coordinates to find the maximum gap
        for i in range(1, len(x_coords)):
            width = x_coords[i] - x_coords[i - 1]
            max_width = max(max_width, width)
        
        return max_width
