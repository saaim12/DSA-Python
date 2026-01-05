def Count_subsets_with_sum_K(arr,k):
    n=len(arr)
    def check(idx,target):
        if idx==0:
            if target==0 and arr[0]==0:
               return 2
            if target==0 or target==arr[0]:
                return 1
            else:
                return 0

        not_take=check(idx-1,target)
        take=0
        if arr[idx]<=target:
            take=check(idx-1,target-arr[idx])

        return take+not_take

    return check(n-1,k)

print(Count_subsets_with_sum_K([1,2,3],3))
print(Count_subsets_with_sum_K([0,0,1],1))

def Count_subsets_with_sum_K_with_memo(arr, k):
    n = len(arr)
    dp = {}

    def check(idx, target):
        if idx == 0:
            if target == 0 and arr[0] == 0:
                return 2
            if target == 0 or target == arr[0]:
                return 1
            return 0

        if (idx, target) in dp:
            return dp[(idx, target)]

        not_take = check(idx - 1, target)
        take = 0
        if arr[idx] <= target:
            take = check(idx - 1, target - arr[idx])

        dp[(idx, target)] = take + not_take
        return dp[(idx, target)]

    return check(n - 1, k)

def subsets_with_sum_k_tabulation(arr,k):
    n=len(arr)
    dp=[[0]*(k+1) for i in range(n)]
    if arr[0]==0:
        dp[0][0]=2
    else:
        dp[0][0]=1

    if arr[0]!=0 and arr[0]<=k:
        dp[0][arr[0]]=1

    for i in range(1,n):
        for j in range(1,k+1):
            not_take=dp[i-1][j]
            take=0
            if arr[i]<=j:
                take=dp[i-1][j-arr[i]]
            dp[i][j]=take+not_take

    return dp[n-1][k]
print(Count_subsets_with_sum_K([1,2,3],3))           # Output: 2
print(Count_subsets_with_sum_K([0,0,1],1))           # Output: 4
print(Count_subsets_with_sum_K_with_memo([1,2,3],3)) # Output: 2
print(subsets_with_sum_k_tabulation([0,0,1],1))      # Output: 3
