arr=[3,1,2]
def sub_sequences(idx,arr,path,res):
    if idx>=len(arr):
        res.append(list(path))
        return res
    path.append(arr[idx])
    sub_sequences(idx+1,arr,path,res)
    path.pop()
    sub_sequences(idx+1,arr,path,res)
    return res

print(sub_sequences(0,arr,[],[]))


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

print(sub_sequences_equals_k(0,[1,2,1],[],[],2,0))
