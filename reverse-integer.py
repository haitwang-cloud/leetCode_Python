# Time:  O(logn) = O(1)
# Space: O(1)
#
#给定一个 32 位有符号整数，将整数中的数字进行反转
#
# Example1: x = 123, return 321
# Example2: x = -123, return -321
#


class Solution:
    # 运行时间为76ms的案例
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        a=str(x if x>0 else -x)
        nums=int(a[::-1]) if x>0 else -int(a[::-1])
        return nums if -2147483648<nums<2147483647 else 0
    # 运行时间为68ms的案例
    def reverse2(self, x):
        """
        :type x: int
        :rtype: int
        """
        sum=0
        y=abs(x)
        len_x=len(str(y))
        for i in range(1,len_x+1):
            a=int(y%10**i/10**(i-1))*10**(len_x-i)
            sum=sum+a
        if x<0:
            sum=-sum
        if sum<-2**31 or sum>2**31-1:
            return 0   
        else:
            return sum
        # 运行时间为52ms的案例        
    def reverse3(self, x):
        """
        :type x: int
        :rtype: int
        """
        result = 0
        if x >= 0 : 
            result =  int(str(x)[::-1])
        else:
            x = -x
            result =  0 - int(str(x)[::-1])
        
        if result > 2**31 - 1 or result < 0 - 2**31:
            return 0
        return result