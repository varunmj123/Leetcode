class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        arrayPointer = 0
        sequencePointer = 0
        while sequencePointer <= len(s) - 1 and arrayPointer <= len(t) - 1:
            if t[arrayPointer] != s[sequencePointer]:
                arrayPointer += 1
            else:
                arrayPointer += 1
                sequencePointer += 1
        if sequencePointer < len(s):
            return False
        else:
            return True
