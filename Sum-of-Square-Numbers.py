# Time:  O(sqrt(c) * logc)
# Space: O(1)
#
# Example 1:
# Input: 5
# Output: True
# Explanation: 1 * 1 + 2 * 2 = 5
import math


class Solution:
    # 执行时间为260ms的案例
    def judgeSquareSum(self, c: int) -> bool:
        lt = 0
        rt = int(math.sqrt(c))
        while lt <= rt:
            s = lt*lt +rt*rt 
            if s > c:
                rt -= 1
            elif s < c:
                lt += 1
            else:
                return True
        return False

        
