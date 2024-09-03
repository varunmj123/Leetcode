class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        num1Map = {}
        output = [-1] * len(nums1)
        for i in range(len(nums1)):
            num1Map[nums1[i]] = i
        stack = []
        for i in range(len(nums2)):
            while stack and nums2[i] > stack[-1]:
                appendVal = stack.pop()
                if appendVal in num1Map:
                    output[num1Map[appendVal]] = nums2[i]
            if nums2[i] in num1Map:
                stack.append(nums2[i])
        return output
