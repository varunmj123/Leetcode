class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        maxNum = 0
        left = 0
        currSum = 0
        numCount = {}
        
        for right in range(len(nums)):
            if nums[right] in numCount:
                numCount[nums[right]] += 1
            else:
                numCount[nums[right]] = 1
            currSum += nums[right]
            
            while numCount[nums[right]] > 1:
                numCount[nums[left]] -= 1
                currSum -= nums[left]
                left += 1
            
            if right - left + 1 == k:
                maxNum = max(maxNum, currSum)
                numCount[nums[left]] -= 1
                currSum -= nums[left]
                left += 1
        
        return maxNum
