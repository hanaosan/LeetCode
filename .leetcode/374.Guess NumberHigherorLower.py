# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        # 初期値としてlowに1, highにnを設定する
        low, high = 1, n
        # 右に1シフトすると2で整数除算してるのと同じ意味になる
        middle = (low + high) >> 1
        while (result := guess(middle)) != 0:
            if result == 1:
                low = middle + 1
            elif result == -1:
                high = middle - 1
            middle = (low + high) >> 1

        return middle
