# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):


class Solution:
    # 执行时间为44ms的案例
    def firstBadVersion_1(self, n):
        """
        :type n: int
        :rtype: int

        如果第 m 个版本出错，则表示第一个错误的版本在 [l, m] 之间，令 h = m；否则第一个错误的版本在 [m + 1, h] 之 间，令 l = m + 1。
        因为 h 的赋值表达式为 h = m，因此循环条件为 l < h。
        """
        left, right = 1, n
        while left < right:
            mid = left+(right-left)//2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid+1

        return left
    # 执行时间为32ms的案例

    def firstBadVersion_2(self, n):
        """
        :type n: int
        :rtype: int
        """
        i = 1
        j = n
        while i < j:
            mid = int((i+j)/2)
            if isBadVersion(mid):
                j = mid-1
            else:
                i = mid+1
        if isBadVersion(i):
            return i
        else:
            return i+1
