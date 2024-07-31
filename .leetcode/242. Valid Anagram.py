class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sCount, tCount = Counter(s), Counter(t)
        if sCount == tCount:
            return True
        return False
