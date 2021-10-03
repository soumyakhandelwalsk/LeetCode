#Problem: https://leetcode.com/problems/number-of-islands/
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]=="1":
                    visit(i,j,grid,m,n)
                    count+=1
        return count
def visit(i, j, grid, m, n):
    if ((i < m) and (i >=0) and (j < n) and (j>=0) and (grid[i][j] == "1")):
        grid[i][j] = "2"
        visit(i+1, j, grid, m,n )
        visit(i-1, j, grid,m,n)
        visit(i,j+1,grid,m,n)
        visit(i,j-1,grid,m,n)
