# Time:  O(n) ~ O(n^2)
# Space: O(1)


class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # nums.sort()
        # return nums[len(nums)-k]

        # import heapq
        # return heapq.nlargest(k,nums)[-1]

        return sorted(nums)[-k]
