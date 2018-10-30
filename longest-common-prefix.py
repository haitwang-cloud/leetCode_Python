# Time:  O(n * k), k is the length of the common prefix
# Space: O(1)


# 编写一个函数来查找字符串数组中的最长公共前缀。
# 如果不存在公共前缀，返回空字符串 ""
# Example 1:
# Input: ["flower","flow","flight"]
# Output: "fl"

class Solution:
    # 执行用时为 60 ms 的范例
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) < 1:
            return ""

        max_str = strs[0]
        max_len = len(max_str)
        for item in strs:
            if len(item) > max_len:
                max_len = len(item)
                max_str = item
        for item in strs:
            index = 0
            j = 0
            while j != len(item) and j != len(max_str):
                if item[index] == max_str[index]:
                    index += 1
                j += 1
            max_str = max_str[:index]

        return max_str
    # 执行用时为 44 ms 的范例
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ''

        if len(strs) == 1:
            return strs[0]

        # 只需要比较最大和最小的,
        # 只要a和b有共同前缀,其他中间的都有,只要a和b没有,其他的有也白瞎
        a = min(strs)
        b = max(strs)

        for i in range(len(a)):
            if a[i] != b[i]:
                return a[:i]
        return a
