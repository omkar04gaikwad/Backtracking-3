###
# Approach:
# We use backtracking to place queens one row at a time.
# At each step, we try placing a queen in all columns of the current row.
# We maintain three sets to ensure safety:
# - cols: to check if a column already has a queen
# - pos_diag (r + c): to check positive diagonals
# - neg_diag (r - c): to check negative diagonals
# If a valid spot is found, place 'Q' and recurse for the next row.
# After recursion, we backtrack by removing the queen and updating sets.
# Once we reach row n, we convert the board to string format and add to results.
#
# Time Complexity: O(N!) - worst case trying all permutations with pruning
# Space Complexity: O(N²) for the board, O(N) for recursion and sets
###

class Solution:
    def SolveNQueens(self, n):
        res = []
        sol = [["."]*n for _ in range(n)]
        cols = set()
        pos_diag = set()
        neg_diag = set()
        def backtrack(r):
            if r == n:
                res.append(["".join(row) for row in sol])
                return
            for c in range(n):
                if c in cols or (r+c) in pos_diag or (r-c) in neg_diag:
                    continue
                sol[r][c] = "Q"
                cols.add(c)
                pos_diag.add(r+c)
                neg_diag.add(r-c)
                backtrack(r+1)
                sol[r][c] = "."
                cols.remove(c)
                pos_diag.remove(r+c)
                neg_diag.remove(r-c)
        backtrack(0)
        return res
    def main(self):
        boards = self.SolveNQueens(4)
        for board in boards:
            for row in board:
                print(row)
            print()
        print("Total Solutions:", len(boards))

sol = Solution()
sol.main()