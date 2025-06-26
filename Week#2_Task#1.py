
# Use of loops to find prime numbers upto a given number
#In the given task we will find prime numbers upto a given number
#Prime numbers are the numbers which are divisible by 1 or number itself


number=int(input("Enter a number upto which you want to display the prime numbers: "))
print(f"Prime Numbers between 2 and {number} are:\n")
for num in range(2,number+1):
    flag=True
    for i in range(2,num):
        if num%i==0:
            flag=False
            break
    if flag: 
          print(num,end=',')

            
   