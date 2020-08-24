# -*-coding:UTF-8-*-
"""
输入一个整数数组，
实现一个函数来调整该数组中数字的顺序，
使得所有奇数位于数组的前半部分，所有偶数位于数组的后半部分。

输入：nums = [1,2,3,4]
输出：[1,3,2,4]
"""


def exchange(nums):
    ou = []
    qi = []
    [ou.append(nums[i]) if nums[i] % 2 == 0 else qi.append(nums[i]) for i in range(len(nums))]
    return qi + ou


if __name__ == '__main__':
    exchange([1, 2, 3, 4])
