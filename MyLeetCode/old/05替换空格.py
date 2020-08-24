# -*-coding:UTF-8-*-

"""
示例 1：

输入：s = "We are happy."
输出："We%20are%20happy."
"""
from typing import List

import re


# todo 正则比str的replace要快很多倍

class Solution(object):
    def replaceSpace(self, s: str) -> str:
        return re.sub(" ", "%20", s)


if __name__ == '__main__':
    s = "We are happy."
    print(Solution().replaceSpace(s))
