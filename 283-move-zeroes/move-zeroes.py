class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        right = 1

        while right < len(nums) :
            currLeft = nums[left]
            currRight = nums[right]
            if currLeft == 0 and currRight != 0:
                nums[left] = currRight
                nums[right] = currLeft
                left += 1
                right +=1
            elif currLeft != 0 and currRight != 0:
                left += 2
                right += 2
            elif currLeft == 0 and currRight == 0:
                right += 1
            elif currLeft != 0 and currRight == 0:
                left += 1
                right += 1

