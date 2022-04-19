class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = [[0 for _ in board[0]] for __ in board]
        m, n = len(board), len(board[0])
        def dfs(x, y, w):
            if not w:
                return True
            else:
                visited[x][y] = 1
                if board[x][y] == w[0]:
                    # early check
                    if len(w) == 1:
                        return True
                    # move up
                    if (x > 0) and (not visited[x-1][y]):
                        if dfs(x-1, y, w[1:]):
                            return True
                    # move down
                    if (x < m-1) and (not visited[x+1][y]):
                        if dfs(x+1, y, w[1:]):
                            return True
                    # move left
                    if (y > 0) and (not visited[x][y-1]):
                        if dfs(x, y-1, w[1:]):
                            return True
                    # move right
                    if (y < n-1) and (not visited[x][y+1]):
                        if dfs(x, y+1, w[1:]):
                            return True
                # no finding, quit
                visited[x][y] = 0
                return False
        for i in range(len(board)):
            for k in range(len(board[0])):
                if dfs(i, k, word):
                    return True
        return False