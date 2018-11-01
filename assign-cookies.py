# Time:  O(nlogn)
# Space: O(1)

# Example 1:
# Input: [1,2,3], [1,1]
#
# Output: 1
#


class Solution(object):
        # 执行时间为96ms的案例
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        i, j = 0, 0
        while i < len(g) and j < len(s):
            if g[i] <= s[j]:
                i += 1
            j += 1
        return i
