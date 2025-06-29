def most_freq(arr:list) -> int:

    "This functions returns the element of array with most frequency"

    count_freq = {}

    for i in arr:
        if i in count_freq.keys():
            temp = count_freq[i]+1
            count_freq[i]=temp
        else:
            count_freq[i]=1

    max_key = None
    max_value = None
    for key in count_freq:
        if max_value is None or count_freq[key] > max_value:
            max_value = count_freq[key]
            max_key = key
        elif count_freq[key] == max_value and key > max_key:
            max_key = key

    return max_key


def fixed_point(arr:list) -> int:
    "this function returns first fixed point in array if no fixed point then -1"
    for i in range(len(arr)):
        if arr[i]==i:
            return arr[i]
    return -1
    
# print(fixed_point([0,1,2,3,17]))


def fixed_point_binary(arr: list) -> int:
    "Returns first fixed point in sorted, distinct array or -1 if none"
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == mid:
            return mid
        elif arr[mid] < mid:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def appers_once(arr):
    "returns element that appers once"
    memo = {}
    for i in range(len(arr)):
        if arr[i] in memo:
            memo[arr[i]]+=1
        else:
            memo[arr[i]]=1
    for key in memo:
        if memo[key]==1:
            return key
    return -1   



# arr = [1,1,2,2,3,4,4]
# print(appers_once(arr))


#check if an array is sorted

def is_sorted_mine(arr:list) -> bool:
    "returns true if the array is sorted"
    
    if not arr:
        return True

    sorted = True

    for i in range(len(arr)):
        if i == (len(arr)-1):
            if arr[i] < arr[i-1]:
                sorted = False
                return sorted
            
        elif arr[i] > arr[i+1]:
            sorted = False
            return sorted

    return sorted

def is_sorted(arr: list) -> bool:
    "Returns True if the array is sorted in non-decreasing order"
    if not arr:
        return True  # Empty array is considered sorted
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True


# print(is_sorted([1,2,3,4,5,4]))

def merge_sort(nums1:list,m:int,nums2:list,n:int):
    if n == 0:
        return
    
    nums2_last = n-1
    for i in range(((m+n)-1),m-1,-1):
        nums1[i] = nums2[nums2_last]
        nums2_last-=1

    return nums1


# print(merge_sort(
#     nums1=[1,2,3,0,0,0],
#     m=3,
#     nums2=[2,5,6],
#     n = 3
#     ))


#return second largest
def second_largest(arr: list[int]) -> str:
    "returns the largest and second largest element in arr"
    if len(arr) < 2:
        return "Array must have at least two elements"

    largest = second_largest = float('-inf')
    
    for num in arr:
        if num > largest:
            second_largest = largest
            largest = num
        elif largest > num > second_largest:
            second_largest = num

    if second_largest == float('-inf'):
        return "No second largest element (all elements may be equal)"
    return f"largest = {largest}\nsecond largest = {second_largest}"


# print(second_largest([4,2,3,6,1,7,9]))

def increment_array(arr):
    "Increments the array as if it represents a number"
    n = len(arr) - 1
    for i in range(n, -1, -1):
        if arr[i] != 9:
            arr[i] += 1
            return arr
        else:
            arr[i] = 0
    return [1] + arr


arr = [1,8,9,9]
result = increment_array(arr)
print(result)