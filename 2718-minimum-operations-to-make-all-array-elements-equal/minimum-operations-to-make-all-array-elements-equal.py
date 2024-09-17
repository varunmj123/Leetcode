class Solution:
    def minOperations(self, nums: List[int], queries: List[int]) -> List[int]:
    # Sort the array of numbers
        nums.sort()

        # Manually compute the prefix sums
        prefix = [0] * (len(nums) + 1)
        for i in range(1, len(nums) + 1):
            prefix[i] = prefix[i - 1] + nums[i - 1]

        ans = []
        n = len(nums)
        
        # Implementing binary search manually
        def binary_search(x):
            left, right = 0, n
            while left < right:
                mid = (left + right) // 2
                if nums[mid] < x:
                    left = mid + 1
                else:
                    right = mid
            return left
        
        # Process each query
        for x in queries:
            i = binary_search(x)
            # Calculate the result for this query
            ans.append(x * (2 * i - n) + prefix[n] - 2 * prefix[i])
        
        return ans
