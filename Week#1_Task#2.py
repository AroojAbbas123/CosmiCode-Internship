
#In this task I am going to implement the advanced arithmetic operations like power,
# modulus using functions.

#What  about Functions?
#Function is simply a block of code which performs a specific task.Its a resuable part of
#code.

#In the Task I am going to implement the given below aritmetic operations:
#1.Addition
#2.Subtraction
# 3.Multiplication
# 4.Division
# 5.Modulus
# 6.Power

#We cxan also use module "Math" to implemet these arithmetic operations diectly But I
# prefer to implement it mannualy for better understanding.


def sum(a,b):
    return a+b

def subtraction(a,b):
    return a-b

def multiplication(a,b):
    return a*b
    
    
def div(a,b):
    if(b!=0):
        return a/b
    else:
        print("Undefined!")
        return -1
        
def Power(a,b):
    return a**b

def modulus(a,b):
    return a%b


number1=int(input("Enter your first number: "))
number2=int(input("Enter your second number: "))
print("Here is the menue!")
print("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Power\n6.Modulus")
choice=int(input("Which operation do you want to perform on given numbers?"))
if (choice<1 or choice>6):
    print("Choose the option between 1-6 only!")
else:
    # while(choice<=6 or choice>0):
    #     print("Here is the menue!")
    #     print("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Power\n6.Modulus")
    #     choice=int(input("Which operation do you want to perform on given numbers?"))
        if (choice==1):
            print("Sum of  " ,number1, " and ",number2, " is: ",sum(number1,number2))
        elif(choice==2):
            print("Difference of ",number1, " and ",number2, " is: ",subtraction(number1,number2))
        elif(choice==3):
            print("Product of ",number1, " and ",number2, " is: ",multiplication(number1,number2))
        elif(choice==4):
            print("Division of ",number1, " and ",number2, " is: ",div(number1,number2))
        elif(choice==5):
            print(number1,"to the raise power of ",number2,"is: ",Power(number1,number2))
        else:
            print("Modulus of ",number1," and ",number2, "is: ", modulus(number1,number2))
            
        
        
