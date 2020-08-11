# -*-coding:UTF-8-*-
"""
输入：[3,4,5,1,2]
输出：1
"""


class Solution:
    def minArray(self, numbers_list):
        for i in range(len(numbers_list)):
            if numbers_list[-2 + i] > numbers_list[-1 + i]:
                return numbers_list[-1 + i]


if __name__ == '__main__':
    l = [3, 4, 5, 1, 2]
    print(Solution().minArray(l))
