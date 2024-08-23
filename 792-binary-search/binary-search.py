class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right: 
            medium = ((right - left) // 2) + left
            if nums[medium] < target:
                left = medium + 1
            elif nums[medium] > target: 
                right = medium - 1
            else:
                return medium 
        return -1