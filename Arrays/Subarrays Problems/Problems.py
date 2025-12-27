# making all subarrays
arr=[1,2,3]
res=[]
for i in range(len(arr)):
    for j in range(i+1,len(arr)+1):
        res.append(arr[i:j])

print(res)

##########################################
# followings are the sub arrays problems #
##########################################

###################################
# Q1: longest subarray with sum k #
###################################
## brute Force Solution O(n*3)
def longest_subarray_with_sum_k_brute_force(arr,k):
    res=[]
    for i in range(len(arr)):
        for j in range(i + 1, len(arr) + 1):
            sub = arr[i:j]
            res.append(sub)
    max_length=0
    sub_arr=None
    for array in res:
        if sum(array)==k:
            if len(array)>max_length:
                 max_length=len(array)
                 sub_arr=array

    return max_length,sub_arr

print(longest_subarray_with_sum_k_brute_force([1,2,3,1,1,1,1,4,2,3],3))
## better Solution O(n*2)
def longest_subarray_with_sum_k_better(arr,k):
    max_length=float('-inf')
    sub_arr=None
    n=len(arr)
    s=0
    for i in range(n):
        s=0
        for j in range(i,n):
            s+=arr[j]
            if s==k:
                if j-i+1>max_length:
                   max_length=j-i+1
                   sub_arr=arr[i:j+1]
    return max_length,sub_arr


print(longest_subarray_with_sum_k_better([1,2,3,1,1,1,1,4,2,3],3))


## optimized Solution O(n) but also space complexity of O(n)
def longest_subarray_with_sum_k_optimized(arr,k):
    max_length=0
    sub_arr=None
    mp={}
    n=len(arr)
    prefix_sum=0
    for i in range(n):
        prefix_sum+=arr[i]
        if prefix_sum==k:
            max_length=i+1
            sub_arr=arr[0:i+1]
        if (prefix_sum-k) in mp:
            length=i-mp[prefix_sum-k]
            if length>max_length:
                max_length=i-mp[prefix_sum-k]
                sub_arr=arr[mp[prefix_sum-k]+1:i+1]
        if prefix_sum not in mp:
            mp[prefix_sum] = i



    return max_length,sub_arr

print(longest_subarray_with_sum_k_optimized([1,2,3,1,1,1,1,4,2,3],3))
print(longest_subarray_with_sum_k_optimized([1,2,3],6))
## this only works for non_negative numbers
def longest_subarray_with_sum_k_two_pointer(arr,k):
    summed=arr[0]
    left=0
    right=0
    length=0
    while right<len(arr):
        while left<=right and summed>k:
            summed-=arr[left]
            left+=1
        if summed==k:
            length=max(length,right-left+1)
        right+=1
        if right <len(arr):
            summed+=arr[right]

    return length


print(longest_subarray_with_sum_k_two_pointer([1,2,3,1,1,1,1,4,2,3],3))
print(longest_subarray_with_sum_k_two_pointer([1,2,3],6))


##########################
## maximum subarray Sum ##
##########################
# Kadane 's algorithm
def Max_subarray_sum(arr):
    if len(arr)==1:
        return arr[0]
    st=0
    ans_st=0
    max_sum=float('-inf')
    sum=0
    ans_end=0
    for i in range(len(arr)):
        if sum==0:
            st=i
        sum+=arr[i]
        if sum>max_sum:
            max_sum=sum
            ans_st=st
            ans_end=i
        if sum<0:
            sum=0


    return max_sum,arr[ans_st:ans_end+1]

print(Max_subarray_sum([-2,-3,4,-1,-2,1,5,-3]))


