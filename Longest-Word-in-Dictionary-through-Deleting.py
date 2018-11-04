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
        d.sort(key=lambda x:(-len(x),x))
        for item in d:
            index=0
            for c in s:
                if index<len(item) and item[index]==c:
                    index+=1
                if index==len(item):
                    return item
        return ""

