# Time:  O(nlogn)
# Space: O(1)

# Example:
#
# Input:
# [[10,16], [2,8], [1,6], [7,12]]
#
# Output:
# 2
#
"""
题意：
气球放在水平轴上，给出气球在水平轴的坐标（xstart , xend），表示气球的起始位置和终止位置。
先用箭来击破气球，当箭的位置x落在xstart ≤ x ≤ xend 的时候，就能击破气球。  
先给出一堆气球的坐标，问至少需要多少箭能将所有的气球击破。

【解法】：
其实这道题实际是求所有坐标区间中，一共有多少个并集。有多少个并集，就需要多少支箭。
对points按照左端点进行排序是个关键。用end保存箭右端点的位置，若气球的左端点<=end, 则这个气球在射击范围内。若气球的左端点>end, 则不在范围内，需要重新设置一个箭。
"""


class Solution(object):
    # 执行时间为128ms的案例
    def findMinArrowShots_1(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        ans = 0
        points.sort(key=lambda p: p[1])
        arrowEnd = float("inf")  # 箭的右端点
        for start, end in points:
            if start > arrowEnd:  # 若气球的左端点大于箭的右端点，需要增加一次射击。
                ans += 1
                arrowEnd = end  # 更新当前箭的右端点
        return ans
    # 执行时间为136ms的案例

    def findMinArrowShots_2(self, points):
        if not points:
            return 0
        points.sort(key=lambda p: p[1])
        curr_pos = points[0][1]
        ans = 1
        for i in range(len(points)):
            if curr_pos >= points[i][0]:
                continue
            curr_pos = points[i][1]
            ans += 1
        return ans
