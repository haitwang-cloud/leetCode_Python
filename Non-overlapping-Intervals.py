# Time:  O(nlogn)
# Space: O(1)

# You may assume the interval's end point is always bigger than its start point.
# Intervals like [1,2] and [2,3] have borders "touching" but they don't overlap each other.
# Example 1:
# Input: [ [1,2], [2,3], [3,4], [1,3] ]
#
# Output: 1
"""
计算最多能组成的不重叠区间个数，然后用区间总个数减去不重叠区间的个数。
在每次选择中，区间的结尾最为重要，选择的区间结尾越小，留给后面的区间的空间越大，那么后面能够选择的区间个数也就越大。
按区间的结尾进行排序，每次选择结尾最小，并且和前一个区间不重叠的区间
"""


class Solution:
    # 执行时间为72ms的案例
    def eraseOverlapIntervals_1(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        # 按区间的开头进行排序
        intervals.sort(key=lambda intervals: intervals.start)
        result, pre = 0, 0
        for i in range(1, len(intervals)):
            if intervals[i].start < intervals[pre].start:
                if intervals[i].end < intervals[pre].end:
                    pre = i
                result += 1
            else:
                pre = i
        return result
    # 执行时间为72ms的案例
    def eraseOverlapIntervals_2(self, intervals):
        if len(intervals) == 0:
            return False
        # 按区间的结尾进行排序
        intervals.sort(key=lambda intervals: intervals.end)
        cnt,end=1,intervals[0].end
        for i in range(1,len(intervals)):
            if intervals[i].start<end:
                continue
            end=intervals[i].end
            cnt+=1
        return len(intervals)-cnt

