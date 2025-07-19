
# Complex numbers are numbers which are in the form a + bj, where 'a' and 'b' are real numbers and 'j' is the imaginary unit in Python.


class Complex:
    def __init__ (self,a,b):
        self.a=a
        self.b=b
        
    def display(self):
        if self.b >= 0:
            print(f"The complex number is {self.a} + {self.b}i\n")
        else:
            print(f"The complex number is {self.a} - {-self.b}i\n")
   
    def  add(self, other):
        real_part = self.a + other.a
        imaginary_part = self.b + other.b
        return Complex(real_part, imaginary_part)
    
    def subtract(self, other):
        real_part = self.a - other.a
        imaginary_part = self.b - other.b
        return Complex(real_part, imaginary_part)
    
    def multiply(self, other):
        real_part = self.a * other.a - self.b * other.b
        imaginary_part = self.a * other.b + self.b * other.a
        return Complex(real_part, imaginary_part)
    
    def divide(self, other):
        denominator = other.a**2 + other.b**2
        if denominator == 0:
            raise ValueError("Cannot divide by zero.")
        real_part = (self.a * other.a + self.b * other.b) / denominator
        imaginary_part = (self.b * other.a - self.a * other.b) / denominator
        return Complex(real_part, imaginary_part)
    
    def equal(self, other):
        return self.a == other.a and self.b == other.b
    
    def notEqual(self, other):
        return not self.equal(other)
    
    
val1=int(input("Enter the real part of the first complex number: "))
val2=int(input("Enter the imaginary part of the first complex number: "))
val3=int(input("Enter the real part of the second complex number: "))
val4=int(input("Enter the imaginary part of the second complex number: "))
c1=Complex(val1, val2)
c2=Complex(val3, val4)

print("Details of the first complex number:\n")
c1.display()
print("Details of the second complex number:\n")
c2.display()


print("Addition of the two complex numbers:\n")
c3= c1.add(c2)
c3.display()

print("Subtraction of the two complex numbers:\n")
c4= c1.subtract(c2)
c4.display()


print("Multiplication of the two complex numbers:\n")
c5= c1.multiply(c2)
c5.display()


print("Division of the two complex numbers:\n")
c6= c1.divide(c2)
c6.display()


print("Checking if the two complex numbers are equal:")
if c1.equal(c2):
    print("The two complex numbers are equal.")
else:
    print("The two complex numbers are not equal.")


