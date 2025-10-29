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