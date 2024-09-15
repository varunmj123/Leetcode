class Solution:
    def countDivisibleSubstrings(self, word: str) -> int:
        output = 0
        numMap = {
            "a": 1, "b": 1, "c": 2, "d": 2, "e": 2, "f": 3,
            "g": 3, "h": 3, "i": 4, "j": 4, "k": 4, "l": 5,
            "m": 5, "n": 5, "o": 6, "p": 6, "q": 6, "r": 7,
            "s": 7, "t": 7, "u": 8, "v": 8, "w": 8, "x": 9,
            "y": 9, "z": 9
        }

        # Check all substrings
        for left in range(len(word)):
            currSum = 0
            for right in range(left, len(word)):
                currSum += numMap[word[right]]
                if currSum % (right - left + 1) == 0:
                    output += 1

        return output
