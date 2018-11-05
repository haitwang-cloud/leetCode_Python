# Time:  O(n)
# Space: O(n)
import collections


class Solution(object):
    # 执行用时为 60 ms 的范例
    def topKFrequent_1(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        d = {}
        for i in nums:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        c = sorted(d.items(), key=lambda e: e[1], reverse=True)
        result = []
        for i in range(k):
            result.append(c[i][0])
        return result
        # 执行用时为 56 ms 的范例

    def topKFrequent_2(self, nums, k):
        return [key for key, _ in collections.Counter(nums).most_common(k)]
