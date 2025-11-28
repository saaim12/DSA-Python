### combinational sum I and II problems ###
def combinationsl_sum_I(arr,target,res,path,idx):
    if target==0:
        res.append(list(path))
        return res
    if idx>=len(arr) or target<0:
        return res

    ## picking element
    path.append(arr[idx])
    combinationsl_sum_I(arr,target-arr[idx],res,path,idx)
    ## not picking element
    path.pop()
    combinationsl_sum_I(arr,target,res,path,idx+1)
    return res

print(combinationsl_sum_I([2,3,6,7],7,[],[],0))
def combinational_sum_II(arr,target,path,res,idx):
    if target == 0:
        res.append(list(path))
        return res
    if idx >= len(arr) or target < 0:
        return res
    if idx>0 and arr[idx]==arr[idx-1]:
        combinational_sum_II(arr,target,path,res,idx+1)
        return res
    path.append(arr[idx])
    combinational_sum_II(arr,target-arr[idx],path,res,idx+1)
    path.pop()
    combinational_sum_II(arr,target,path,res,idx+1)
    return res

print(combinational_sum_II(sorted([10,1,2,7,6,1,5]),8,[],[],0))

