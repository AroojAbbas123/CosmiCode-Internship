#In the given task we are going to generate a fabcconi sequence upto a user defined limit.
#Fabcconi Sequence is the sequence in which each number is sum of the two preceeding numbers


# First I am going to use iterative approach

def fabconni(target):
    if (target>0):
         first_number=0
         second_num=1
         for i in range(1,target+1):
            print(first_number,end=',')     
            new_num=first_number+second_num
            first_number=second_num
            second_num=new_num
            



# ----------------------------------------------------------------------------------


#Now we are using Recursive method to solve above problem

def recursive_fabconi(num):
    if num==0:
        return 0
    elif num==1:
        return 1
    else:
        return recursive_fabconi(num-1)+recursive_fabconi(num-2)
    

num=int(input("Enter your desired number upto which you want to generate a fabcconi series: "))

print("Recursive Approch")

print(f"Here is the Fabcconi series upto {num} numbers")

for i in range(num+1):
    print(recursive_fabconi(i),end=',')
print("\n")   

print("Iterative Approch")    
fabconni(num)

    