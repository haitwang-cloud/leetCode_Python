# Time:  O(n)
# Space: O(1)

"""
Example 1:
Input: [4,2,3]
Output: True
Explanation: You could modify the first 4 to 1 to get a non-decreasing array

在出现 nums[i] < nums[i - 1] 时，需要考虑的是应该修改数组的哪个数，使得本次修改能使 i 之前的数组成为非递
减数组，并且 不影响后续的操作 。优先考虑令 nums[i - 1] = nums[i]，因为如果修改 nums[i] = nums[i - 1] 的
话，那么 nums[i] 这个数会变大，就有可能比 nums[i + 1] 大，从而影响了后续操作。还有一个比较特别的情况就
是 nums[i] < nums[i - 2]，只修改 nums[i - 1] = nums[i] 不能使数组成为非递减数组，只能修改 nums[i] = nums[i
- 1]
"""


class Solution:
    # 执行时间为88ms的案例
    def checkPossibility_1(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        modified, prev = False, nums[0]
        for i in range(1, len(nums)):
            if prev > nums[i]:
                if modified:
                    return False
                elif i-2 < 0 or nums[i-2] <= nums[i]:
                    prev = nums[i]
                modified = True
            else:
                prev = nums[i]
        return True
     # 执行时间为56ms的案例
    def checkPossibility_2(self, nums):
        cal = 0
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                cal += 1
                if 0 < i < len(nums)-2 and (nums[i-1] > nums[i+1] and nums[i] > nums[i+2]):
                    return False
                if cal >= 2:
                    return False
        return True
