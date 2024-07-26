#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
# Space Optimization
# O(1) spaces
# O(n) times 
class Solution:
    def climbStairs(self, n: int) -> int:
        # 早期リターン
        if n == 0 or n == 1:
            return 1
        
        # 変数を用意
        one_step_before, two_steps_before = 1, 1
        for i in range (2, n+1):
            current = one_step_before + two_steps_before
            two_steps_before = one_step_before
            one_step_before = current

        return current

# Tabulation method(表計算)
# O(n) spaces
# O(n) times 
# class Solution:
#     def climbStairs(self, n: int) -> int:
#         # 0段目からn段目までの配列を初期化
#         dp = [ None ] * (n + 1)
#         # 0段目のパターンは1通り(0段目にいて何もしない=動的計算の初期値)
#         dp[0] = 1
#         # 0段目からn段目までのパターンを計算していく
#         # rangeの第2引数は第2引数以下の数まで処理する exc. range(1, 3) → 1,2
#         for i in range(1, n + 1):
#             if i == 1:
#                 # 1段目にいく方法は1通り
#                 dp[i] = 1
#             else:
#                 # 2段目以降に登る方法は1段したの階段まで登るのパターンの合計(1歩登る場合)+2段下の階段まで登るパターンの合計(2歩登る場合)
#                 dp[i] = dp[i - 1] + dp[i -2]

#         # 配列のキーは0から始まるので配列のn+1番目の要素の値が取得される exc. 0,1,2,3,4,5
#         return dp[n]
# @lc code=end

