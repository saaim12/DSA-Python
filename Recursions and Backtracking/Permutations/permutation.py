# This line creates a NEW array at every recursive step, which is:
#
# ❌ Extra memory
# ❌ Extra time
# ❌ O(n) slicing at every level
# ❌ Overall complexity = O(n · n!)
def permutation(arr):
    res=[]
    def permute(arr,path):
        if not arr:
            res.append(list(path))
            return
        for i in range(len(arr)):
            path.append(arr[i])
            permute(arr[:i]+arr[i+1:],path)
            path.pop()
        return
    permute(arr,[])
    return res

print(permutation([1,2,3]))

# Most optimized approach (NO slicing)
#
# Use in-place swapping.
#
# ✔ No array copy
# ✔ No arr[:i] + arr[i+1:]
# ✔ Very efficient → O(n!) time with minimal overhead
# ✔ Commonly used in interviews and LeetCode
# ⭐ Optimized In-Place Permutation Code

def permutation_2(arr):
    res=[]
    def permute_2(idx):
        if idx>=len(arr):
            res.append(arr[:])
            return
        for i in range(idx,len(arr)):
            arr[i],arr[idx]=arr[idx],arr[i]
            permute_2(idx+1)
            arr[i],arr[idx]=arr[idx],arr[i]

        return
    permute_2(0)
    return res
print(permutation_2([1,2,3]))

######## dont know shit about this ust did it remembering #####
import math
def getPermutation( n, k):
    nums = [str(i) for i in range(1, n + 1)]
    k -= 1
    res = []
    for i in range(n, 0, -1):
        fact = math.factorial(i - 1)
        index = k // fact
        res.append(nums[index])
        nums.pop(index)
        k %= fact

    return "".join(res)

print(getPermutation(4,13))