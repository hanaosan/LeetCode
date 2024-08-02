class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashSet = set()
        for num in nums:
            if num in hashSet:
                return True
            hashSet.add(num)

        return False

# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         for count in Counter(nums).values():
#             if count > 1:
#                 return True

#         return False
