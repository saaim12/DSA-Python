arr1=[[3, 6, 1], [2, 3, 4], [5, 5, 1]]
def maximumPath(arr):
    rows=len(arr)
    cols=len(arr[0])
    def check(r,c):
        if r==rows-1:
            return arr[r][c]

        # on each row every col
        maxi=0
        for col in range(cols):
            maxi=max(maxi,arr[r][c]+check(r+1,col))

        return maxi
    return max(check(0,c) for c in range(cols))

print(maximumPath(arr1))
def maximum_path_with_memo(arr):
    rows = len(arr)
    cols = len(arr[0])
    memo = {}

    def check(r, c):
        # Base case: last row
        if r == rows - 1:
            return arr[r][c]

        if (r, c) in memo:
            return memo[(r, c)]

        maxi = 0
        # Move to any column in the next row
        for next_c in range(cols):
            maxi = max(maxi, arr[r][c] + check(r + 1, next_c))

        memo[(r, c)] = maxi
        return maxi

    # Try all starting columns in top row
    return max(check(0, c) for c in range(cols))


arr1 = [[3, 6, 1],
        [2, 3, 4],
        [5, 5, 1]]

print(maximum_path_with_memo(arr1))  # 15
