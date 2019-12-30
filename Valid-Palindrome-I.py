# Time:  O(n)
# Soace: O(1)


# Example :
# Input: "abca"
# Output: True

class Solution(object):
    # 执行时间为232ms的案例
    def validPalindrome(self, s: str) -> bool:
        """
        :type s: str
        :rtype: bool
        """
        def isValid(s,left,right):
            while left< right:
                if s[left] != s[right]:
                    return False
                left,right= left+1,right-1
            return True
        left, right = 0, len(s)-1
        while left < right:
            if s[left] != s[right]:
                return isValid(s, left+1, right) or isValid(s, left, right-1)
            left,right=left+1,right-1
        return True









