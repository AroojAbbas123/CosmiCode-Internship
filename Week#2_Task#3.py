
import math as m

#In this task we are going to compute GCD and LCM using Eucledian Algorithm
# GCD is product of all common factors of two given numbers


def gcd(a,b):
    while b!=0:
        a,b=b,a%b
    return a



#Now we will find Least Common Multiple
# LCM is product of all common and non-common factors of two given numbers

def lcm(a,b):
    lcm=abs(a*b)/gcd(a,b)
    return lcm
    
    
num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))

print(f"Greatest Common Divisior of {num1} and {num2} is {gcd(num1,num2)}")
print(f"Least  Common Multiple of {num1} and {num2} is {lcm(num1,num2)}")

