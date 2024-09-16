class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stackS = []
        stackT = []
        for c in s:
            if c == "#" and stackS:
                stackS.pop()
            elif c != "#":
                stackS.append(c)
        for c in t:
            if c == "#" and stackT:
                stackT.pop()
            elif c != "#":
                stackT.append(c)

        return stackS == stackT