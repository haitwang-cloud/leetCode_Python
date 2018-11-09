class Solution:
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        """
        从边上开始搜索，如果是'O'，那么搜索'O'周围的元素，并将'O'置换为'T'，这样每条边都DFS一遍。
        而内部的'O'是不会改变的。这样下来，没有被围住的'O'全都被置换成了'T'，被围住的'O'还是'O'，没有改变。
        然后遍历一遍，将'O'置换为'X'，将'D'置换为'O'。
        """
        if not board:
            return

        m, n = len(board), len(board[0])

        def dfs(i, j):
            if 0 <= i < m and 0 <= j < n and board[i][j] == 'O':
                board[i][j] = 'T'
                dfs(i-1, j)
                dfs(i+1, j)
                dfs(i, j-1)
                dfs(i, j+1)

        for i in range(m):
            dfs(i, 0)
            dfs(i, n-1)
        for i in range(n):
            dfs(0, i)
            dfs(m-1, i)
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'T':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'
