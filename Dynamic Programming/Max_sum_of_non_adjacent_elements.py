def max_sum_of_non_adjacent_elements(arr):
    res=[]
    def subsequence(idx,path):
        res.append(list(path))
        for i in range(idx,len(arr)):
            path.append(arr[i])
            subsequence(i+2,path)
            path.pop()
        return

    subsequence(0,[])
    print(res)

max_sum_of_non_adjacent_elements([1,2,3])