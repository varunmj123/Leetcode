from typing import List

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        maxNum = 0
        left = 0
        current_sum = 0
        tempCheck = set()
        
        for right in range(len(nums)):
            # Add the current element to the set and update the sum
            if nums[right] in tempCheck:
                # Slide the window to the right until there are no duplicates
                while nums[left] != nums[right]:
                    tempCheck.remove(nums[left])
                    current_sum -= nums[left]
                    left += 1
                left += 1  # Remove the duplicate element itself
            else:
                tempCheck.add(nums[right])
                current_sum += nums[right]
                
            # Check if we have a valid window of size `k`
            if right - left + 1 == k:
                maxNum = max(maxNum, current_sum)
                
                # Slide the window by removing the leftmost element
                current_sum -= nums[left]
                tempCheck.remove(nums[left])
                left += 1
        
        return maxNum
