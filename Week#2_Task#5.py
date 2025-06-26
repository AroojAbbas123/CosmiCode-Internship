

# In this task we are going to find maximum sum subarray using Kadane's Algorithm

def Kadane_Algo(arr,size):
    current_max=arr[0]
    new_max=arr[0]
    for i in range(1,size):
        current_max=max(arr[i],current_max+arr[i])
        if(current_max>new_max):
           new_max=current_max
    return new_max


size=int(input("Enter size of your array: "))
array=[]
for i in range(size):
    n=int(input(f"Enter {i+1} element of array: "))
    array.append(n)
    
print(f"Maximum subarray sum is {Kadane_Algo(array,size)}")
     
