class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        leftOfNums1 = m - 1
        rightOfNums1 = m + n - 1
        rightOfNums2 = n - 1

        while rightOfNums2 >= 0:
            if leftOfNums1 >= 0 and nums1[leftOfNums1] >= nums2[rightOfNums2]:
                nums1[rightOfNums1] = nums1[leftOfNums1]
                leftOfNums1 -= 1
            else:
                nums1[rightOfNums1] = nums2[rightOfNums2]
                rightOfNums2 -= 1
            rightOfNums1 -= 1
