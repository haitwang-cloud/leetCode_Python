# Time:  O((d * l) * logd), l is the average length of words
# Space: O(1)


# Example 1:
# Input:
# s = "abpcplea", d = ["ale","apple","monkey","plea"]

class Solution(object):
    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        def is_sub(a, b):
            i, n = 0, len(a)
            for c in b:
                if i < n and a[i] == c:
                    i += 1
            return i == n
        result = ''
        for string in d:
            if is_sub(string, s):
                if len(string) > len(result):
                    result = string
                elif len(string) == len(result) and string < result:
                    result = string
        return result

