class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            middle = (right + left) // 2
            if nums[middle] > target: 
                right = middle - 1
            elif nums[middle]  < target:
                left = middle + 1
            else:
                return middle
        return left