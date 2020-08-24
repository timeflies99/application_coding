# -*-coding:UTF-8-*-

"""
一只青蛙一次可以跳上1级台阶，也可以跳上2级台阶。求该青蛙跳上一个 n 级的台阶总共有多少种跳法。

答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。

"""


class Solution(object):
    def __init__(self):
        self.f1 = 1
        self.f2 = 2
        self.list = []

    def numWays(self, n):
        if n == 1 or n == 0:
            return 1
        elif n == 2:
            return 2

        else:
            self.list.append(0)
            self.list.append(1)
            self.list.append(2)
            for i in range(3, n + 1):
                res = (self.list[i - 1] + self.list[i - 2]) % 1000000007
                self.list.append(res)
            return self.list[n]


if __name__ == '__main__':
    r = Solution().numWays(4)
    print(r)
