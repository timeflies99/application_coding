"""
给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有和为 0 且不重复的三元组。

注意：答案中不可以包含重复的三元组。

 

示例 1：

输入：nums = [-1,0,1,2,-1,-4]
输出：[[-1,-1,2],[-1,0,1]]

"""
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result_list = []
        if len(nums) < 3:
            return result_list
        for i in range(len(nums)):
            new_nums1 = nums[0:i] + nums[i + 1:]
            for j in range(0, len(new_nums1)):
                new_nums2 = new_nums1[:j] + new_nums1[j + 1:]
                sums = -(nums[i] + new_nums1[j])
                if sums in new_nums2:
                    result_list.append([nums[i], new_nums1[j], sums])

        dd = {}
        result = []
        for res in result_list:
            set_res = frozenset(res)
            if set_res in dd:
                continue
            else:
                dd[set_res]=1
                result.append(res)

        return result


if __name__ == '__main__':
    r = Solution().threeSum([-1, 0, 1, 2, -1, -4, -2, -3, 3, 0, 4])
    print(r)
    """[[-4,0,4],[-4,1,3],[-3,-1,4],[-3,0,3],[-3,1,2],[-2,-1,3],[-2,0,2],[-1,-1,2],[-1,0,1]]"""
