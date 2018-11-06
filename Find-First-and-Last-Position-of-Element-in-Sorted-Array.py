class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        #先寻找左侧端点区间值
        left = self.binarySearch(lambda x, y: x >= y, nums, target)
        if left >= len(nums) or nums[left] != target:
            return [-1, -1]
        # Find the first idx where nums[idx] > target
        #再寻找右侧端点区间值
        right = self.binarySearch(lambda x, y: x > y, nums, target)
        return [left, right - 1]

    def binarySearch(self, compare, nums, target):
        left, right = 0, len(nums) #注意nums的初始值
        while left < right:
            mid = left + (right - left) // 2
            if compare(nums[mid], target):
                right = mid
            else:
                left = mid + 1
        return left  