# longest Common Substring
def longest_common_subsequence_bruteforce(s1, s2):
    def generate_subsequences(s):
        res = []

        def dfs(idx, path):
            if idx == len(s):
                res.append(path)
                return
            # take current character
            dfs(idx + 1, path + s[idx])
            # not take current character
            dfs(idx + 1, path)
        dfs(0, "")
        return res

    subs1 = generate_subsequences(s1)
    subs2 = generate_subsequences(s2)
    ans = 0
    for sub in subs1:
        if sub in subs2:
            ans = max(ans, len(sub))

    return ans



print(longest_common_subsequence_bruteforce("abcde","ace"))

def longest_common_subsequence_recursive(s1,s2):
    def check(idx1,idx2):
        if idx1<0 or idx2<0:
            return 0

        if s1[idx1]==s2[idx2]:
            return 1+ check(idx1-1,idx2-1)

        return max(check(idx1-1,idx2),check(idx1,idx2-1))

    return check(len(s1)-1,len(s2)-1)

print(longest_common_subsequence_recursive("abcde","ace"))

def longest_common_subsequence_recursive_with_memorization(s1,s2):
    dp=[[-1]*len(s2) for i in range(len(s1))]
    def check(idx1,idx2):
        if idx1==0 or idx2==0:
            return 0
        if dp[idx1-1][idx2-1]!=-1:
            return dp[idx1-1][idx2-1]
        if s1[idx1-1]==s2[idx2-1]:
            dp[idx1-1][idx2-1]=1+ check(idx1-1,idx2-1)
            return dp[idx1-1][idx2-1]
        dp[idx1-1][idx2-1]=max(check(idx1-1,idx2),check(idx1,idx2-1))
        return dp[idx1-1][idx2-1]

    return check(len(s1),len(s2))

print(longest_common_subsequence_recursive_with_memorization("abcde","ace"))

def longest_common_subsequence_with_tabulation(s1,s2):
    n,m=len(s1),len(s2)
    dp=[[0]*(m+1) for i in range(n+1)]
    print(dp)

    for i in range(1,n+1):
        for j in range(1,m+1):
            if s1[i-1]==s2[j-1]:
                dp[i][j]=1+dp[i-1][j-1]
            else:
                dp[i][j]=max(dp[i-1][j],dp[i][j-1])


    return dp[n][m]

print(longest_common_subsequence_with_tabulation("abcde","ace"))


def longest_common_subsequence_with_lcs_reconstruction_recursive_way(s1,s2):
    def check(idx1,idx2):
        if idx1<0 or idx2<0:
            return ""

        if s1[idx1]==s2[idx2]:
            return s1[idx1]+check(idx1-1,idx2-1)

        left=check(idx1-1,idx2)
        right=check(idx1,idx2-1)

        return left if len(left)>len(right) else right

    return check(len(s1)-1,len(s2)-1)

print(longest_common_subsequence_with_lcs_reconstruction_recursive_way("abcde","ace"))

def longest_common_subsequence_reconstruction(s1,s2):
    n, m = len(s1), len(s2)
    dp = [[0] * (m + 1) for i in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    i,j=n,m
    str=""
    while i>0 and j>0:
        if s1[i-1]==s2[j-1]:
            str=str+s1[i-1]
            i-=1
            j-=1
        elif dp[i-1][j]>dp[i][j-1]:
            i-=1
        else:
            j-=1
    return str

print(longest_common_subsequence_reconstruction("abcde","bdqekw"))





