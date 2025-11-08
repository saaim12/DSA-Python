string = "abd"

def subsequences(unprocessed, processed, result):
    if unprocessed == "":
        result.append(list(processed))
        return
    char = unprocessed[0]
    subsequences(unprocessed[1:], processed, result)          # exclude char
    subsequences(unprocessed[1:], processed + char, result)   # include char

result = []
subsequences(string, "", result)
print(result)


def subStrings(nums):
    nums.sort()  # sort to handle duplicates
    res = []
    def dfs(path,i):
        res.append(list(path))
        for j in range(i,len(nums)):
            if j>i and nums[j]==nums[j-1]:
                continue
            path.append(nums[j])
            dfs(path,j+1)
            path.pop()
    dfs([],0)
    return res
print(subStrings([1,2,2]))


def permutation(s):
    if len(s)==1:
        return s
    result=[]
    for i,ch in enumerate(s):
        rest=s[:i]+s[i+1:]
        for p in permutation(rest):
            result.append(ch+p)

    return result

print(permutation("abc"))

#built in method
from itertools import permutations

s = "abc"

# Using set to remove duplicates
perm_strings = set(''.join(p) for p in permutations(s))

print(perm_strings)
