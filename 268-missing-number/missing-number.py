class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        numMap = {}
        for i in range(len(nums)):
            numMap[nums[i]] = i

        for i in range(len(nums) + 1):
            if i not in numMap:
                return i
