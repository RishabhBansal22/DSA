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
