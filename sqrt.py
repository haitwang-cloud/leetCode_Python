class Solution:
    # 执行时间为72 ms的案例
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 2:
            return x
        l, h = 1, x//2
        while l <= h:
            mid = l+(h-1)//2
            if mid > x/mid:
                h = mid-1
            else:
                l = mid+1
        return h
