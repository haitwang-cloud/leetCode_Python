"""
题目描述：一个有序数组只有一个数不出现两次，找出这个数。要求以 O(logN) 时间复杂度进行求解。
令 index 为 Single Element 在数组中的位置。如果 m 为偶数，并且 m + 1 < index，那么 nums[m] == nums[m +1]；m + 1 >= index，
那么 nums[m] != nums[m + 1]。从上面的规律可以知道，如果 nums[m] == nums[m + 1]，那么 index 所在的数组位置为 [m + 2, h]，
此时令 l = m+ 2；如果 nums[m] != nums[m + 1]，那么 index 所在的数组位置为 [l, m]，此时令 h = m。
因为 h 的赋值表达式为 h = m，那么循环条件也就只能使用 l < h 这种形式。
"""


class Solution:
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums)-1
        while left < right:
            mid = left+(right-left)//2
            if mid % 2 == 1:
                #  保证 left/right/mid 都在偶数位，使得查找区间大小一直都是奇数
                mid = mid-1
            if nums[mid] == nums[mid+1]:
                left = mid+2
            else:
                right = mid
        return nums[left]
