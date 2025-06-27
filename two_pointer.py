
def two_sum(arr,n):
    "find and returns the elements whose sum matches with n in arr using two pointer technique"
    left = 0
    right = len(arr)-1
    
    while left<right:
        pointers_sum = arr[left]+arr[right]

        if pointers_sum == n:
            return [arr[left],arr[right]]
        elif pointers_sum < n:
            left+=1
        else:
            right-=1
    
    return -1

# print(two_sum(arr,n))


arr = [2,3,1,4,5,6,7,8,9]

sum_arr = []

for i in range(len(arr)):

    if len(sum_arr)==0:
        sum_arr.append(arr[i])
    else:
        sum_arr.append(arr[i]+sum_arr[i-1])

q = [1,3]
re = sum_arr[3]-sum_arr[q[0]-1]
print(re)




