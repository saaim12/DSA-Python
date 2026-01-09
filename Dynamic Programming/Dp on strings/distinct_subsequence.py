def distinct_subsequences(s1,s2):
    n=len(s1)
    m=len(s2)
    def check(i,j):
        if j<0:
            return 1
        if i <0:
            return 0

        if s1[i]==s2[j]:
            return check(i-1,j-1)+check(i-1,j)
        else:
            return check(i-1,j)

    return check(n-1,m-1)

print(distinct_subsequences(s1 = "rabbbit", s2 = "rabbit")) # 3
print(distinct_subsequences(s1 = "babgbag", s2 = "bag")) # 5

def distinct_subsequences_with_memo(s1,s2):
    n=len(s1)
    m=len(s2)
    memo={}
    def check(i,j):
        if j == 0:
            return 1
        if i == 0:
            return 0
        if (i, j) in memo:
            return memo[(i, j)]
        if s1[i - 1] == s2[j - 1]:
            memo[(i, j)] = check(i - 1, j - 1) + check(i - 1, j)
        else:
            memo[(i, j)] = check(i - 1, j)
        return memo[(i, j)]

    return check(n,m)


print(distinct_subsequences_with_memo("rabbbit", "rabbit")) # 3

def distinct_subsequences_with_tabulation(s1,s2):
    n=len(s1)
    m=len(s2)
    dp=[[0] *(m+1) for i in range(n+1)]
    for i in range(n+1):
        dp[i][0]=1

    for i in range(1,n+1):
        for j in range(1,m+1):
            if s1[i-1]==s2[j-1]:
                dp[i][j]=dp[i-1][j-1]+dp[i-1][j]
            else:
                dp[i][j]=dp[i-1][j]

    return dp[n][m]