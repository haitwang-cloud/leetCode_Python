# Time:  O(n * sqrt(n))
# Space: O(n)

# Example
#
# Input:
# [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
#
# Output:
# [[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
"""
题目描述：一个学生用两个分量 (h, k) 描述，h 表示身高，k 表示排在前面的有 k 个学生的身高比他高或者和他一样高。
为了在每次插入操作时不影响后续的操作，身高较高的学生应该先做插入操作，否则身高较小的学生原先正确插入第 k 个位置可能会变成第 k+1 个位置。
身高降序、k 值升序，然后按排好序的顺序插入队列的第 k 个位置中。
"""


class Solution(object):
    def reconstructQueue_1(self, people):
        people.sort(key=lambda p: (-p[0], p[1]))
        result = []
        for p in people:
            result.insert(p[1], p)
        return result
