## TC is O(n!*n) ans space is O(n!*n)

def next_permutation_brute_force(arr):
    res=[]
    def permute(arr,path):
        if len(arr)==0:
            res.append(list(path))
            return

        for i in range(len(arr)):
            path.append(arr[i])
            permute(arr[:i]+arr[i+1:],path)
            path.pop()
        return
    permute(arr,[])
    return res,res[1]

print(next_permutation_brute_force([3,2,1]))

## better approach if the TC is only O(N!)
def next_permuteation_better(arr):
    res=[]
    def permute(idx):
        if idx>=len(arr):
            res.append(arr[:])
            return
        for i in range(idx,len(arr)):
            arr[i],arr[idx]=arr[idx],arr[i]
            permute(idx+1)
            arr[i], arr[idx] = arr[idx], arr[i]

        return

    permute(0)
    return res,res[1]

print(next_permuteation_better([3,2,1]))

