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
def Longest_Subarray_with_Sum(arr,k):
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
print(Longest_Subarray_with_Sum(arr, k))

# optimal solution
def longest_Subarray_with_Sum_optimal(arr,k):


# Maximum Subarray (Kadane)
#
# Count Subarrays with Sum = K
#
# Longest Subarray with At Most K Zeros
#
# Subarrays with Exactly K Distinct
#
# Subarray Sum Divisible by K