class Solution:
    def romanToInt(self, s: str) -> int:
        symbolMap = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000           
        }

        specialMap = {
            "IV": 4,
            "IX" : 9,
            "XL" : 40,
            "XC" : 90,
            "CD" : 400,
            "CM" : 900
        }
        output = 0
        i = 0
        
        while i < len(s):
            # Check if the next two characters form a special case
            if i + 1 < len(s) and s[i:i+2] in specialMap:
                output += specialMap[s[i:i+2]]
                i += 2
            else:
                output += symbolMap[s[i]]
                i += 1
        
        return output
