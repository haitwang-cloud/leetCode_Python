# Time:  O(1)
# Space: O(1)

# 判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数
# Example
# Input: 121
# Output: true

class Solution:
    #执行时间为392ms的案例
    def isPalindrome_1(self, x):
        """
        :type x: int
        :rtype: bool
        """
        m=str(x)
        n=m[::-1]
        return m==n
    #执行时间为288ms的案例
    def isPalindrome_2(self,x):
        return x >= 0 and str(x) == str(x)[::-1]