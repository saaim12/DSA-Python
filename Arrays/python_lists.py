list=[1,2,3,4,5]

# two sum
# first approach
def two_sum(arr, target):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i != j and arr[i] + arr[j] == target:
                return [i, j]
    return -1

print(two_sum(list,3))
#optimized approach
# start _end pointer O (n log n)
#log n for sort and n for search
def two_sum_better(arr,target):
        if not arr:
            return []
        # copy of first arr
        arr2=arr[:]
        arr.sort()
        st=0
        end=len(arr)-1
        result=[-1,-1]
        while(st<end):
            sum=arr[st]+arr[end]
            if sum == target:
                result[0]=arr[st]
                result[1]=arr[end]
                break
            elif sum > target:
                end -=1
            else:
                st+=1
        end_result = [-1, -1]
        found = 0
        for i in range(len(arr2)):
            if arr2[i] == result[0] and end_result[0] == -1:
                end_result[0] = i
                found += 1
            elif arr2[i] == result[1] and end_result[1] == -1:
                end_result[1] = i
                found += 1
            if found == 2:
                break

        return end_result

print(two_sum_better(list,3))
def missing_and_repeating_values(arr):
    # Step 1: Flatten the 2D list
    flat_list = []
    for row in arr:
        for val in row:
            flat_list.append(val)
    print(flat_list)
    # Step 2: Detect repeating value
    seen = set()
    repeating = -1
    for val in flat_list:
        if val in seen:
            repeating = val
        seen.add(val)

    # Step 3: Compute sums
    actual_sum = sum(seen) + repeating  # Add repeating value manually
    n = len(flat_list)
    expected_sum = (n * (n + 1)) // 2

    missing = expected_sum + repeating - actual_sum
    print(seen)
    print(repeating)
    print(missing)
print(missing_and_repeating_values([[9,1,7],[8,9,2],[3,4,6]]))

