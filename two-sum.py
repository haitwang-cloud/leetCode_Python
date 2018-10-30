# Time:  O(n)
# Space: O(n)

# 给定一个整数数组和一个目标值，找出数组中和为目标值的两个数。

# 你可以假设每个输入只对应一种答案，且同样的元素不能被重复利用
#
# 示例:
# Given nums = [2, 7, 11, 15], target = 9,
#
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].


class Solution(object):
    #执行用时1436ms，时间有点儿长
    def twoSum_1(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i,num in enumerate(nums):
            sub_num=target-num
            if sub_num in nums:
                index=nums.index(sub_num)
                if i !=index:
                    return [i,index]

    # 执行用时52ms的案例
    def twoSum_2(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic={}
        for i in range(len(nums)):
            if nums[i] in dic:
                return [dic[nums[i]],i]
            else:
                dic[target-nums[i]] = i
    # 执行用时为36ms的案例
    def twoSum_3(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}
        for i, num in enumerate(nums):
            if (target - num) in dic:
                return i,dic[target - num]
            dic[num] = i
