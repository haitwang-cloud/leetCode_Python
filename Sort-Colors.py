# Time:  O(n)
# Space: O(1)

class Solution:
    # 执行时间为44ms的案例
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        zero = nums.count(0)
        one = nums.count(1)
        two = nums.count(2)
        nums.clear()
        for i in range(zero):
            nums.append(0)
        for i in range(one):
            nums.append(1)
        for i in range(two):
            nums.append(2)