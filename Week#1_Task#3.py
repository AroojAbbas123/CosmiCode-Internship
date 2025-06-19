#In this task I am going to implement the if-else statement.

number1=int(input("Enter frist number: "))
number2=int(input("Enter second number: "))
number3=int(input("Enter third number: "))

if(number1<number2 and number1<number3):
    print(number1," is smallest ammong all of three numbers!")
elif(number2<number1 and number2<number3):
    print(number2," is  smallest ammong all of three numbers!")
else:
    print(number3," is smallest ammong all of three numbers!")
    
    
if(number1>number2 and number1>number3):
    print(number1," is largest ammong all of three numbers!")
elif(number2>number1 and number2>number3):
    print(number2," is largest ammong all of three numbers!")
else:
    print(number3," is largest ammong all of three numbers!")


