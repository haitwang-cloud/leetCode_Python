# Time:  O(n)
# Space: O(n)

# Input:
# "tree"
#
# Output:
# "eert"
import collections

# 执行时间为56ms的案例


class Solution:
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        count = collections.Counter(s).most_common()
        res = ''
        for key, value in count:
            res += key*value
        return res
