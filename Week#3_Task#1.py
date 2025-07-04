# In this task we will use merge technoique to sort array
#Merge Sort: Merge Sort is a divide-and-conquer sorting algorithm that works by recursively splitting an array into smaller subarrays, sorting them, and then merging them back together in order.

def MergeSort(array):
    if len(array) <= 1:
        return array  # Base case: return the array if length is 0 or 1
    
    mid = len(array) // 2
    left = MergeSort(array[:mid])  # Recursively sort left half
    right = MergeSort(array[mid:])  # Recursively sort right half
    
    # Merge the sorted halves
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result


        
        
size=int(input("Enter size of array: "))
array=[]
for i in range(size):
    n=int(input(f"Enter element {i+1}: "))
    array.append(n)
    
print("Original array is: ")
# print("[",end=" ")
# for i in range(size):
#     print(array[i],end=",")
# print("]")
print(array)


array1=MergeSort(array)
print("After merge sort: ")
print(array1)

    
    
    
    