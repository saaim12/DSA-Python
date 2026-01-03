def Count_partitions_with_difference_D(arr, D):
    total = sum(arr)

    # Check feasibility
    if (total + D) % 2 != 0:
        return 0

    target = (total + D) // 2
    n = len(arr)
    memo = {}

    def count(idx, s):
        if s == 0:
            return 1  # valid subset
        if idx < 0:
            return 0  # no elements left

        if (idx, s) in memo:
            return memo[(idx, s)]

        not_pick = count(idx - 1, s)
        pick = 0
        if arr[idx] <= s:
            pick = count(idx - 1, s - arr[idx])

        memo[(idx, s)] = pick + not_pick
        return pick + not_pick

    return count(n - 1, target)
arr = [1,1,2,3]
D = 1
print(Count_partitions_with_difference_D(arr, D))
# Output: 3
# Explanation: subsets [1,2], [1,2], [3,1] etc. depending on indexing
