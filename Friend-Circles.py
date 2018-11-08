import numpy as np


class Solution:
    # 执行时间为182ms的案例
    def findCircleNum_1(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        def dfs(M, i, hasVisited):
            hasVisited[i] = 1
            for j in range(n):
                if M[i][j] == 1 and not hasVisited[j]:
                    dfs(M, j, hasVisited)
        n = len(M)
        hasVisited = np.zeros(n)
        counter = 0
        for i in range(n):
            if not hasVisited[i]:
                dfs(M, i, hasVisited)
                counter += 1
        return counter
    # 执行时间为76ms的案例

    def findCircleNum_2(self, M):
        v = [0]*len(M)
        cnt = 0
        for i in range(len(M)):
            if v[i] == 0:
                cnt = cnt+1
                dfs(M, i, v)
        return cnt

        def dfs(self, M, i, v):
            for j in range(len(M)):
                if M[i][j] == 1 and v[j] == 0:
                    v[j] = 1
                    self.dfs(M, j, v)
