
def append(arr:list[int],val:int) -> list[int]:
    "appends the value val at end of array arr"

    arr_copy = [0]*(len(arr)+1)
    for i in range(len(arr)):
        arr_copy[i] = arr[i]
    
    arr_copy[len(arr)] = val
    arr = arr_copy
    return arr

def insert(arr:list, index:int, val:int) -> list:
    "inserts the value val at index in array arr"

    arr_copy = [0]*(len(arr)+1)
    for i in range(index):
        arr_copy[i] = arr[i]
    
    arr_copy[index] = val

    for i in range(index,len(arr)):
        arr_copy[i + 1] = arr[i]

    arr = arr_copy
    return arr

def pop(arr:list):
    "removes element from last in array"
    return arr[:(len(arr)-1)]

def pop_index(arr:list, index:int) -> list:
    "removes element at index in array"

    if index < 0 or index >= len(arr):
        raise IndexError("Index out of range")
    
    arr_copy = [0]*(len(arr)-1)
    

    for i in range(index):
        arr_copy[i] = arr[i]
    
    for i in range(index+1,len(arr)):
        arr_copy[i-1] = arr[i]
    
    return arr_copy

class Array_operation:
    def __init__(self, arr:list):
        self.arr = arr

    def total(self) -> int:
        total = 0
        for i in self.arr:
            total += i
        return total
    
    def total_even(self) -> int:
        total = 0
        for i in self.arr:
            if i%2 == 0:
                total += i
        
        return total
    
    def maximum(self) -> int:
        maximum = float("-inf")

        for i in range(len(self.arr)):
            if self.arr[i] > maximum:
                maximum = self.arr[i]

        return maximum
    
    def minimum(self) -> int:
        minimum = self.arr[0]

        for i in range(1,len(self.arr)):
            if self.arr[i] < minimum:
                minimum = self.arr[i]
        
        return minimum
     
    def count(self, value:int=None):
        "counts and return frequency of given element "

        count_dict = {}

        for val in self.arr:
            if val not in count_dict.keys():
                count_dict[val] = 1
            else:
                count_dict[val]+=1
        
        return count_dict[value] if value else count_dict




arr = Array_operation([22,2,3,4,5,2])
print("sum = ",arr.total())
print("sum of evens = ",arr.total_even())
print("maximum = ", arr.maximum())
print("minimum = ", arr.minimum())
print('frequency count = ', arr.count(value=22))