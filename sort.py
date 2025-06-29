arr = [2,3,1,5,4,7,6]

def selection_sort(arr:list[int]):
    "sorts array by selection sort algorithm"

    for i in range(len(arr)-1):
        min_idx = i

        for j in range(i+1,len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    
    return arr




def bubble_sort(arr:list[int]) -> list:
    

    for i in range(len(arr)-1):
        arr[i], arr[i+1] = arr[i+1], arr[i]
    
    return arr

print(bubble_sort(arr))