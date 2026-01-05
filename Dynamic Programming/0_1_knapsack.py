def knapsack(W, val, wt):
    n=len(wt)
    def check(idx, bag_w):
        if idx < 0:
            return 0
        not_pick = check(idx - 1, bag_w)
        pick = float('-inf')
        if wt[idx] <= bag_w:
            pick = val[idx] + check(idx - 1, bag_w - wt[idx])

        return max(pick, not_pick)

    return check(n - 1, W)