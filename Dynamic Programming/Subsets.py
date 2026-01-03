def making_subsets(arr):
    res=[]
    def subs(idx,path):
        res.append(list(path))
        for i in range(idx,len(arr)):
            path.append(arr[i])
            subs(i+1,path)
            path.pop()

    subs(0,[])
    return res

print(making_subsets([1,2,3]))
#this expects true or false
def subsequence_contain_k(arr,k):
    def check(idx,target):
        if target==0:
            return True
        if idx==0:
            return arr[0]==target

        not_take=check(idx-1,target)
        take=False
        if target>=arr[idx]:
            take=check(idx-1,target-arr[idx])

        return not_take or take
    return check(len(arr),k)

def subsequence_contain_k(arr, k):
    n = len(arr)
    memo = {}
    def check(idx, target):
        if target == 0:
            return True
        if idx == 0:
            return arr[0] == target
        if (idx, target) in memo:
            return memo[(idx, target)]
        not_take = check(idx - 1, target)
        take = False
        if target >= arr[idx]:
            take = check(idx - 1, target - arr[idx])
        memo[(idx, target)] = not_take or take
        return memo[(idx, target)]
    return check(n - 1, k)

def subsequence_contain_k_tabulation(arr, k):
    n = len(arr)
    dp = [[False] * (k + 1) for _ in range(n)]

    # sum = 0 always possible
    for i in range(n):
        dp[i][0] = True

    # first element
    if arr[0] <= k:
        dp[0][arr[0]] = True
    print(dp)
    # fill dp table
    for i in range(1, n):
        for j in range(1, k + 1):
            not_take = dp[i - 1][j]
            take = False
            if j >= arr[i]:
                take = dp[i - 1][j - arr[i]]
            dp[i][j] = not_take or take
    print(dp)
    return dp[n - 1][k]

print(subsequence_contain_k_tabulation([1,2,3],4))
