import math
class Solution(object):
    # 执行时间为56 ms的案例
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        """
        这道题是考察四平方和定理,每个正整数均可表示为4个整数的平方和
        参考链接：https://www.cnblogs.com/grandyang/p/4800552.html
        """
        while n % 4 == 0:
            n //= 4
        while n % 8 == 7:
            return 4
        for i in range(0, int(math.sqrt(n))+1):
            j = int(math.sqrt(n-i*i))
            if i*i+j*j == n:
                return 2 if not not i and not not j else 1
        return 3
