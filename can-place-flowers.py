class Solution:
    # 执行时间为104ms的案例
    def canPlaceFlowers_1(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        for i in range(len(flowerbed)):
            if flowerbed[i]==0 and (i==0 or flowerbed[i-1]==0) and (i==len(flowerbed)-1 or flowerbed[i+1]==0):
                flowerbed[i]=1
                n-=1
        return True if n <=0 else False
    # 执行时间为56ms的案例    
    def canPlaceFlowers_2(self, flowerbed, n):
        i,length=0,len(flowerbed)
        while i<length:
            if flowerbed[i]==0:
                if ((i-1>=0 and flowerbed[i-1]==0) or i==0) and ((i+1< length and flowerbed[i+1]==0) or i==length-1):
                    n-=1
                    i+=2
                else:
                    i+=1
            else:
                i+=2
            if n<=0:
                return True
        return False

            

