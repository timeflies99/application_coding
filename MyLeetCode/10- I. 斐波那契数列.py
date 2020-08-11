# -*-coding:UTF-8-*-
"""
示例 1：

输入：n = 2
输出：1
示例 2：

输入：n = 5
输出：5

f(0)=0
f(1)=1
f(n) = f(n-1)+f(n-2),n>=2
"""
import time


class Solution:
    def fib(self, n: int) -> int:
        assert 0 <= n <= 100
        if n == 0:
            return 0

        elif n == 1:
            return 1

        else:
            dp = list()
            dp.append(0)
            dp.append(1)
            for i in range(2, n + 1):
                dp_tmp = (dp[i - 1] + dp[i - 2]) % 1000000007
                dp.append(dp_tmp)
            return dp[n]


if __name__ == '__main__':
    n = int(input("请输入0-100之间的整数，包括0和100："))
    ti = time.time()
    print(Solution().fib(n))
    print(time.time() - ti)
