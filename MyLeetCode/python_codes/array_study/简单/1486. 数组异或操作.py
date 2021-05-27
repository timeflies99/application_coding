"""
给你两个整数，n 和 start 。
数组 nums 定义为：nums[i] = start + 2*i（下标从 0 开始）且 n == nums.length 。
请返回 nums 中所有元素按位异或（XOR）后得到的结果。

示例 1：
输入：n = 5, start = 0
输出：8
解释：数组 nums 为 [0, 2, 4, 6, 8]，其中 (0 ^ 2 ^ 4 ^ 6 ^ 8) = 8 。
     "^" 为按位异或 XOR 运算符。
"""


class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        a = 0
        for i, num in enumerate([start + 2 * i for i in range(n)]):
            if i == 0:
                a = num
                continue
            a = a ^ num
        return a


if __name__ == '__main__':
    Solution().xorOperation(5, 0)
