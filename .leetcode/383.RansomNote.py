# 計算量 time: O(n+m), memory: O(n+m)
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomNoteCount, magazineCount = Counter(ransomNote), Counter(magazine)
        return ransomNoteCount & magazineCount == ransomNoteCount

# 別解
# 計算量 time: O(n+m), memory: O(n+m)
# class Solution:
#     def canConstruct(self, ransomNote: str, magazine: str) -> bool:
#         ransomNoteCount = Counter(ransomNote)
#         magazineCount = Counter(magazine)
#         for character, count in ransomNoteCount.items():
#             if magazineCount[character] < count:
#                 return False

#         return True
