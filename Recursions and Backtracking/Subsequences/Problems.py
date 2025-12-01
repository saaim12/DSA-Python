######### subsequencce whose sum equals k #######
def sub_sequences_equals_k(idx,arr,path,res,target,sum):
    if sum==target:
        res.append(list(path))
        return res
    if idx>=len(arr):
        return res
    path.append(arr[idx])
    sum+=arr[idx]
    sub_sequences_equals_k(idx+1,arr,path,res,target,sum)
    path.pop()
    sum-=arr[idx]
    sub_sequences_equals_k(idx+1,arr,path,res,target,sum)
    return res

print(sub_sequences_equals_k(0,[1,2,1],[],[],3,0))

####### Combinational Sum I ########
def combinational_sum_I(arr,target,path,idx,res):
    if target==0:
        res.append(list(path))
        return res
    if idx>=len(arr):
        return res
    if target<0:
        return res
    ## picking
    path.append(arr[idx])
    combinational_sum_I(arr,target-arr[idx],path,idx,res)
    path.pop()
    combinational_sum_I(arr, target , path, idx+1, res)
    return res

print(combinational_sum_I([2,3,6,7],7,[],0,[]))

###### Combinational Sum II #######
def Combinational_Sum_II(arr,target,path,idx,res):
    if target==0:
        res.append(list(path))
        return res
    if idx>=len(arr):
        return res
    if target <0:
        return res
    for i in range(idx,len(arr)):
        if arr[i]>target:
            break
        if i>idx and arr[i]==arr[i-1]:
            continue
        path.append(arr[i])
        Combinational_Sum_II(arr,target-arr[i],path,i+1,res)
        path.pop()
    return res


print(Combinational_Sum_II([1,1,1,2,2],4,[],0,[]))


######## subsets problem ########

def subsets(nums):
    res = []

    def subs(idx, arr, path):
        res.append(list(path))
        for i in range(idx, len(arr)):
             path.append(arr[i])
             subs(i + 1, arr, path)
             path.pop()

        return res

    subs(0, nums, [])
    return res
print(subsets([1,2,3]))
######## subsets problem ########

def subsets2(nums):
    res = []
    nums.sort()
    def subs(idx, arr, path):
        res.append(list(path))
        for i in range(idx, len(arr)):
            if i>idx and arr[i]==arr[i-1]:
                continue
            path.append(arr[i])
            subs(i + 1, arr, path)
            path.pop()

        return res

    subs(0, nums, [])
    return res
print(subsets2([1,1]))

######## subsets sums problem #######
def subsets_sums(nums):
    res = []

    def subs(idx, arr, path,sum_):
        res.append(sum_)
        for i in range(idx, len(arr)):
             path.append(arr[i])
             sum_+=arr[i]
             subs(i + 1, arr, path,sum_)
             sum_-=arr[i]
             path.pop()

        return res

    subs(0, nums, [],0)
    return res
print(subsets_sums([2,3]))


