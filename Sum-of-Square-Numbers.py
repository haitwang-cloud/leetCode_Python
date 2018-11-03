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
    def judgeSquareSum_1(self, c):
        i, j = 0, int(math.sqrt(c))+1
        while i < j:
            powSum = i*i+j*j
            if (powSum == c):
                return True
            elif powSum < c:
                i += 1
            else:
                j -= 1
        return False

        
