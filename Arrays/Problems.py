###### we can  make Subarrays by O(n^2) Complexity ######
array=[1,2,3]
result=[]
for i in range(len(array)):
    for j in range(i+1,len(array)+1):
        result.append(array[i:j])

print(result)