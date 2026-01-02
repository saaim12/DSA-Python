def triangle_problem(arr):
    rows=len(arr)
    # cols varies with every row
    def check(r,j):
        if r ==rows-1:
            return arr[r][j]
        cols_on_this_rows=len(arr[r])
        if j>=cols_on_this_rows:
            return 0
        down=arr[r][j]+check(r+1,j)
        diagonal=arr[r][j]+check(r+1,j+1)
        return min(down,diagonal)
    return check(0,0)

arr=[[2],[3,4],[6,5,7],[4,1,8,3]]
print(triangle_problem(arr))
print(triangle_problem([[-10]]))
def triangle_problem_with_memo(arr):
    rows=len(arr)
    # cols varies with every row
    memo={}
    def check(r,j):
        if r ==rows-1:
            return arr[r][j]
        #cols_on_this_rows=len(arr[r])
        if j>=len(arr[r]):
            return 0
        if (r, j) in memo:
            return memo[(r, j)]
        down=arr[r][j]+check(r+1,j)
        diagonal=arr[r][j]+check(r+1,j+1)
        memo[(r,j)]=min(down,diagonal)
        return memo[(r,j)]
    return check(0,0)
print(triangle_problem_with_memo([[-10]]))
print(triangle_problem_with_memo([[2],[3,4],[6,5,7],[4,1,8,3]]))
def triangle_problem_with_tabulation(grid):
    rows=len(grid)
    dp=[row[:] for row in grid]

    for row in range(rows-2,-1,-1):
        for col in range(row+1):
            down=grid[row][col]+dp[row+1][col]
            dg=grid[row][col]+dp[row+1][col+1]
            dp[row][col]=min(down,dg)

    return dp[0][0]


print(triangle_problem_with_tabulation([[2],[3,4],[6,5,7],[4,1,8,3]]))
print(triangle_problem_with_tabulation([[-10]]))