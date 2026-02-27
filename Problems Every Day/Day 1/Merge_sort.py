arr=[5,2,6,4]
def merge_sort(arr,low,high):
    if low>=high:
        return
    mid=(low+high)//2
    merge_sort(arr,low,mid)
    merge_sort(arr,mid+1,high)
    merge(arr,low,mid,high)
    return
def merge(arr,low,mid,high):
    temp=[]
    left=low
    right=mid+1
    while left<=mid and right<=high:
        if arr[left]<=arr[right]:
            temp.append(arr[left])
            left+=1
        else:
            temp.append(arr[right])
            right+=1

    while left<=mid:
        temp.append(arr[left])
        left+=1
    while right<=high:
        temp.append(arr[right])
        right+=1
    for i in range(len(temp)):
        arr[low+i]=temp[i]

    return


######## code usign slicing method



merge_sort(arr,0,len(arr)-1)
print(arr)



### code using slicing method
def sortArray(self, nums):
    if len(nums) <= 1:
        return nums

    mid = len(nums) // 2

    left = self.sortArray(nums[:mid])
    right = self.sortArray(nums[mid:])

    return self.merge(left, right)


def merge( left, right):
    temp = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            temp.append(left[i])
            i += 1
        else:
            temp.append(right[j])
            j += 1

    temp.extend(left[i:])
    temp.extend(right[j:])

    return temp

# LC ---> 912 , 21 ,88
