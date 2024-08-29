class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        expectedTotal = 0
        for i in range(len(nums) + 1):
            expectedTotal += i
        cuurentTotal = 0
        for num in nums:
            cuurentTotal += num
        return expectedTotal - cuurentTotal 
