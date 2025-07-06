#In this task we are going to implement binary search 


def position(arr,target):
    
    left=0
    right=len(arr)-1
    while(left<=right):
        mid=int((left+right)/2)
        if (arr[mid]==target):
           return mid
        elif (target>arr[mid]):
           right=mid-1
        else:
            left=mid+1
    return -1


array=[]
size=int(input("Enter size of list: "))
target=int(input("Enter your target value: "))

for i in range(size):
    n=int(input(f"Enter element {i+1}:"))
    array.append(n)
    
print("Original list is: ")
print(array)

if(position(array,target)==-1):
    print("Not Found!")
else:
    print(f"Your target value {target } is at position {position(array,target)}")    

        
        