from collections import Counter
## majority elements
def majority_elements_bruteForce(arr):
    map={}
    for num in arr:
        if num in map:
            map[num]+=1
        else:
            map[num]=1

    max_no=0
    element=0
    for k,v in map.items():
        if v>max_no:
            max_no=v
            element=k

    return max_no,element


## we can also use Counter builtin in python
arr=[1,2,3,4,5,1,2,3,3,3,3,4,4]
print(Counter(arr))
print("max no of occourance , number ",majority_elements_bruteForce([2,2,3,3,1,1,2,2]))


