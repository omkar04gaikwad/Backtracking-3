###
# Approach:
# We perform DFS from every cell in the board to try to match the `word` character by character.
# At each step, we:
# - Check bounds and constraints: if the cell is already used, or doesn't match the current letter, backtrack.
# - Recursively explore neighbors in 4 directions (up, down, left, right).
# - Use a `path` set to track visited cells in the current path.
#
# If we reach the end of the word (idx == len(word)), we return True.
# If no path matches from a starting point, we return False at the end.
#
# Time Complexity: O(m * n * 4^L), where:
#   - m x n = size of the board
#   - L = length of the word
#   - 4^L comes from 4 directions at each step in the worst case
# Space Complexity: O(L), for the recursion stack and visited path
###

class Solution:
    def exist(self, board, word):
        m = len(board)
        n = len(board[0])
        path = set()
        def dfs(r,c,idx):
            if idx == len(word):
                return True
            if r >= m or r < 0 or c >= n or c < 0 or (r,c) in path or board[r][c] != word[idx]:
                return False
            dirs = [[0,1],[1,0], [0,-1], [-1,0]]
            path.add((r,c))
            for nr, nc in dirs:
                if dfs(nr+r, nc+c, idx+1):
                    return True
            path.remove((r,c))
            return False
        for r in range(m):
            for c in range(n):
                if dfs(r,c,0):
                    return True
        return False

sol = Solution()
board1 = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]

print("Output 1:", sol.exist(board1, "ABCCED"))  # True
print("Output 2:", sol.exist(board1, "SEE"))     # True
print("Output 3:", sol.exist(board1, "ABCB"))    # False