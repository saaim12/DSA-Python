from collections import defaultdict

arr=[1,2,3]
res=[]
# how to make all the subarrays
for i in range(len(arr)):
    for j in range(i+1,len(arr)+1):
        sub=arr[i:j]
        res.append(sub)

print(res)
########   Problems
# Longest Subarray with Sum = K
#  brute force will give TLE error
def Longest_Subarray_len_with_Sum(arr,k):
    res=[]
    for i in range(len(arr)):
        for j in range(i + 1, len(arr) + 1):
            sub = arr[i:j]
            res.append(sub)
    max_length=0
    for array in res:
        if sum(array)==k:
            max_length=max(max_length,len(array))

    return max_length

arr = [1, -1, 5, -2, 3]
k = 3
print("Longest_Subarray_len_with_Sum brute force",Longest_Subarray_len_with_Sum(arr, k))

# optimal solution
def longest_Subarray_len_with_Sum_better(arr,k):
    length=0
    for i in range(len(arr)):
        s=0
        for j in range(i,len(arr)):
            s+=arr[j]
            if s==k:
                length=max(length,j-i+1)

    return length

arr = [1, -1, 5, -2, 3]
k = 3
print("Longest_Subarray_len_with_Sum better",longest_Subarray_len_with_Sum_better(arr, k))
def longest_subarray_sum_optimal(arr,k):
    mp = {}  # prefix_sum -> earliest index
    prefix_sum = 0
    length = 0

    for i in range(len(arr)):
        prefix_sum += arr[i]

        # Case 1: subarray starts from index 0
        # this si only for the first case
        if prefix_sum == k:
            length = i + 1

        # Case 2: subarray exists in between
        if (prefix_sum - k) in mp:
            length = max(length, i - mp[prefix_sum - k])

        # Store earliest occurrence only
        if prefix_sum not in mp:
            mp[prefix_sum] = i

    return length


print("Longest_Subarray_len_with_Sum optimal",longest_subarray_sum_optimal([1, 2, 3, 1, 1, 1, 1, 4, 2, 3], 3))
# Maximum Subarray (Kadane)
#
# Count Subarrays with Sum = K
# still not optimal
def Count_Subarrays(arr,k):
    count = 0
    for i in range(len(arr)):
        s = 0
        for j in range(i, len(arr)):
            s += arr[j]
            if s == k:
                count += 1

    return count
def Count_Subarrays_with_sum_k_optimized(arr,k):
    mp = defaultdict(int)
    prefix_sum = 0
    count = 0
    for i in range(len(arr)):
        prefix_sum+=arr[i]
        if prefix_sum==k:
            count+=1
        count+=mp[prefix_sum-k]
        mp[prefix_sum]=1

    return count
# We use mp[prefix_sum] += 1 instead of mp[prefix_sum] = 1 because mp needs to track how many times each prefix sum has occurred up to the current index.
# Each occurrence of a prefix sum represents a potential starting point for a subarray that sums to k.
# If we were to overwrite the count with = 1 every time, we would lose all information about previous occurrences of the same prefix sum,
# and as a result, we could miss valid subarrays. For example, in an array like [1, 2, 1, 2] with k = 3, the prefix sum 3 occurs more than once.
# Using += 1 allows us to correctly count both subarrays [1, 2] at indices 0–1 and [1, 2] at indices 2–3.
# Therefore, incrementing the count ensures that all possible subarrays that end at the current index
# and sum to k are counted accurately, whereas simply setting it to 1 would undercount and produce incorrect results.
print("count subarrays with sum k ",Count_Subarrays_with_sum_k_optimized([1,2,3],k))



# Longest Subarray with At Most K Zeros
#
# Subarrays with Exactly K Distinct
#
# Subarray Sum Divisible by K