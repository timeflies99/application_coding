"""
给你一个整数数组 nums 。
如果一组数字 (i,j) 满足 nums[i] == nums[j] 且 i < j ，就可以认为这是一组 好数对 。
返回好数对的数目。
 
示例 1：

输入：nums = [1,2,3,1,1,3]
输出：4
解释：有 4 组好数对，分别是 (0,3), (0,4), (3,4), (2,5) ，下标从 0 开始
"""
from typing import List


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums)):
            for val in nums[i+1:]:
                if nums[i] == val:
                    count += 1
        return count


if __name__ == '__main__':
    print(Solution().numIdenticalPairs([1, 2, 3, 1, 1, 3]))
