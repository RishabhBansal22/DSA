arr = [1, 1, 2,4, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
n = 13

def binary_search(arr,n):
    left = 0
    right = len(arr)-1

    while left<=right:

        mid = (left+right)//2
        if arr[mid] == n:
            return mid
        elif n>arr[mid]:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# print(binary_search(arr,n))

def remove_duplicate(arr):
    write = 0
    read = 1
    while read<len(arr):
        if arr[read] != arr[write]:
            write +=1
            arr[write] = arr[read]
        
        read+=1
    
    return write+1, arr

arr = [1,1,2,2,3,3]
print(remove_duplicate(arr))


