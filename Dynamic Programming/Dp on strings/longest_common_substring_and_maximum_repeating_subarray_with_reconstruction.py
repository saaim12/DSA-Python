def longest_common_substring_recursive(s1, s2):
    n, m = len(s1), len(s2)
    memo = {}
    def helper(i, j, curr):
        if i < 0 or j < 0:
            return curr
        if (i, j, curr) in memo:
            return memo[(i, j, curr)]
        if s1[i] == s2[j]:
            match = helper(i - 1, j - 1, curr + 1)
        else:
            match = curr
        skip = max(
            helper(i - 1, j, 0),
            helper(i, j - 1, 0)
        )
        memo[(i, j, curr)] = max(match, skip)
        return memo[(i, j, curr)]
    return helper(n - 1, m - 1, 0)

print(longest_common_substring_recursive("abcde", "ace"))       # 1
print(longest_common_substring_recursive("abcdef", "zabcf"))    # 3

def longest_Common_substring_with_tab(s1,s2):
    n,m=len(s1),len(s2)
    dp=[[0]*(m+1) for i in range(n+1)]
    ans=0
    for i in range(1,n+1):
        for j in range(1,m+1):
            if s1[i-1]==s2[j-1]:
                dp[i][j]=1+dp[i-1][j-1]
                ans=max(ans,dp[i][j])
            else:
                dp[i][j]=0


    return ans



def longest_Common_substring_with_tab_with_reconstruction(s1,s2):
    n,m=len(s1),len(s2)
    dp=[[0]*(m+1) for i in range(n+1)]
    ans=0
    max_len=0
    end_i=0
    for i in range(1,n+1):
        for j in range(1,m+1):
            if s1[i-1]==s2[j-1]:
                dp[i][j]=1+dp[i-1][j-1]
                if dp[i][j]>ans:
                    ans=dp[i][j]
                    max_len=dp[i][j]
                    end_i=i
            else:
                dp[i][j]=0


    return ans,s1[end_i-max_len:end_i]

print(longest_Common_substring_with_tab_with_reconstruction("abcde", "ace"))       # ""
print(longest_Common_substring_with_tab_with_reconstruction("abcdef", "zabcf"))    # "abc"





