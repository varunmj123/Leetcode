class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        subset = []

        def backtrack(i):
            if i >= len(s):
                result.append(subset.copy())
                return
            for j in range(i , len(s)):
                if self.isPlai(s, i, j):
                    subset.append(s[i: j + 1])
                    backtrack(j + 1)
                    subset.pop()
        backtrack(0)
        return result
        
    def isPlai(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True