# Time:  O(n)
# Space: O(n)


class Solution(object):
    # 执行时间为88ms的案例
    def partitionLabels_1(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        lookup = {c: i for i, c in enumerate(S)}
        first, last = 0, 0
        result = []
        for i, c in enumerate(S):
            last = max(last, lookup[c])
            if i == last:
                result.append(i-first+1)
                first = i+1
        return result
     # 执行时间为56ms的案例
    def partitionLabels_2(self, S):
        d = {k:i for i,k in enumerate(list(S))}
        res = []
        lattes = set()
        index = 0
        for i, x in enumerate(list(S)):
            if x not in lattes:
                if all(i > d[k] for k in list(lattes)) and i != 0:
                    lattes = set()
                    res.append(i - sum(res))
                    
                lattes.add(x)
        if res:
            res.append(len(S)-sum(res))
        else:
            res.append(len(S))
        return res
