import math
# @lc code=start
class Solution:
    def judgeSquareSum_1(self, c: int) -> bool:
        if c==2:
            return True
        left,right = 0,int(math.sqrt(c))
        while left <= right:
            if (left*left+right*right)==c:
                return True
            elif left*left+right*right < c:
                left += 1
            else:
                right -= 1
        return False