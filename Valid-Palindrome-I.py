# Time:  O(n)
# Soace: O(1)


# Example :
# Input: "abca"
# Output: True

class Solution(object):
    # 执行时间为232ms的案例
    def validPalindrome_1(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def isValid(s, left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left, right = left+1, right-1
            return False
        left, right = 0, len(s)-1
        while left < right:
            if s[left] != s[right]:
                return isValid(s, left+1, right) or isValid(s, left, right-1)
        return True
    # 执行时间为84ms的案例
    def validPalindrome_2(self, s):
        a = s[::-1]
        for i in range(len(s)):
            if s[i] != a[i]:
                temp_1 = s[:i]+s[i+1:]
                temp_2 = a[:i]+a[i+1:]
                return temp_1 == temp_1[::-1] or temp_2 == temp_2[::-1]
