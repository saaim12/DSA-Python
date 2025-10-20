# combinational sum
def combinational_sum(arr,target):
    res=[]
    def cs(start,target,path):
        if target == 0:
            res.append(list(path))
            return
        if target < 0:
            return

        for i in range(start, len(arr)):
            path.append(arr[i])
            cs(i, target - arr[i], path)  # allow reuse of same candidate
            path.pop()
    cs(0,target,[])
    return res

def subsets(nums):
    res = []

    def back(start, path):
        res.append(list(path))

        for i in range(start, len(nums)):
            path.append(nums[i])
            back(i + 1, path)
            path.pop()

    back(0, [])
    return res
print(combinational_sum([2,3,5],8))
print(subsets([1,2,3]))

