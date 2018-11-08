class Solution:
    # 执行时间为92ms的案例
    def numIslands_1(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])

        def dfs(i, j):
            if 0 <= i < m and 0 <= j < n and grid[i][j] == '1':
                grid[i][j] = '0'
                return 1+dfs(i-1, j)+dfs(i+1, j)+dfs(i, j+1)+dfs(i, j-1)
            return 0
        counter=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]=='1':
                    dfs(i,j)
                    counter+=1
        return counter
            