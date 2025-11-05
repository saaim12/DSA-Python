#generating all subarrays
arr=[1,2,3]
out=[]
for i in range(len(arr)):
    for j in range(i,len(arr)):
        out.append(arr[i:j+1])

print(out)
