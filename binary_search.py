arr = [1, 2, 3, 3.5,4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
n = 13
#return index of n in arr

#linear search
# for i in range(len(arr)):
#     if arr[i]==n:
#         # print(i)


#binary search

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

print(binary_search(arr,n))



