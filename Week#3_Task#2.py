
#In this task we are going to reverse an list without using built-in function

def reverse_list(list):
    if(len(list)<=1):
        return list
    else:
        reversed_list=[]
        i=len(list)-1
        while i>=0:
            reversed_list.append(list[i])
            i-=1
        return reversed_list
    
    
list=[]
size=int(input("Enter size of list: "))
for i in range(size):
    n=int(input(f"Enter element {i+1}: "))
    list.append(n)
print("Original list is: ")
print(list)
arr=reverse_list(list)
print("Reversed list is: ")
print(arr)