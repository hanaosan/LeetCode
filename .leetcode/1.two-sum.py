#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 答えの候補の数値とインデックスを入れておくための辞書を用意
        dictionary = {}
        # 補数が辞書に存在する場合、そのインデックスと現在のインデックスを返す
        # 補数が存在しない場合、現在の数値とそのインデックスを辞書に追加
        for index, number in enumerate(nums):
            complement = target - number
            if complement in dictionary:
                return [dictionary[complement], index]
            else:
                dictionary[number] = index
# @lc code=end
