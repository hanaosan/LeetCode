class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        result = 0
        for i in range(1, 33):
            result = result << 1 | n & 1
            n = n >> 1
        # 内部的には整数として扱われるためreturnすると整数で返却される
        return result
