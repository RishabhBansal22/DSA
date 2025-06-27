
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


arr = [1, 1, 2, 3, 3]
slow = 0
for fast in range(1, len(arr)):
    if arr[fast] != arr[slow]:
        slow += 1
        arr[slow] = arr[fast]

# print(arr)


#reverse the elements of array in place
# Input: [1, 2, 3, 4, 5]
# Output: [5, 4, 3, 2, 1]

def reverse(arr):
    left = 0
    right = len(arr)-1
    while left<right:
        arr[left], arr[right] = arr[right], arr[left]
        left+=1
        right-=1
    
    return arr

# print(reverse([1,2,3,4,5]))

#check if array reads same forward and backward
# Input: [1, 2, 3, 2, 1]
# Output: True

def palindrome(arr:list[int]) -> bool:
    "check if array reads same forward and backward"

    left = 0
    right = len(arr)-1
    is_palindrome = None

    while left<right:

        if arr[left] == arr[right]:
            is_palindrome = True
            left+=1
            right-=1
        else:
            return False
        
    return is_palindrome

# print(palindrome([1, 2, 3, 2, 2]))

#: Given an array and a value, remove all instances of that value in-place and return the new length.
# Input: nums = [3,2,2,3], val = 3
# Output: 2 → nums = [2,2]

def remove_val(arr:list, val):
    i = 0
    for j in range(len(arr)):
        if arr[j] != val:
            arr[i] = arr[j]
            i+=1
    return i, arr

# print(remove_val([3,2,2,3],3))
      

# **Problem**: Given a sorted array, remove duplicates in-place.

# ```python
# Input: [1,1,2,2,3,4,4]
# Output: 4 → [1,2,3,4]
# ```

def remove_duplicate(arr):
    i = 0
    for j in range(1,len(arr)):
        if arr[j] != arr[j-1]:
           i += 1
           arr[i] = arr[j]
    return i+1, arr

print(remove_duplicate([1,1,2,2,3,4,4]))



