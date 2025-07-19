


import math as m

# area of circle=pi*r*r
# parameter of circle =2*pi*r

class Circle:
    def __init__(self,radius):
        self.radius=radius
    def getRadius(self):
        return self.radius
    
    def getArea(self):
        area=2*(m.pi)*m.pow((self.radius),2)
        return area
    
    def getPerimeter(self):
        per=2*(m.pi)*(self.radius)
        return per
    def display(self):
        print("Details of Circle are given here:\n")
        print(f"Radius of circle is {self.radius} meter\n")
        
        
        
#  area of rectangle=length*width
# parameter of rectangle =2*(length+width)

class Rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width
        
    def getLength(self):
        return self.length
    
    def getWidth(self):
        return self.width
    
    
    def getArea(self):
        area=self.length*self.width
        return area
    
    def getPerimeter(self):
        per=2*(self.length+self.width)
        return per
    
    def display(self):
        print("Details of Rectangle are given here:\n")
        print(f"Length of Rectangle is {self.getLength()} meter\n Width of Rectangle is {self.getWidth()} meter\n")
        
        
        
        
        
#  area of triangle=(height*base)/2
# parameter of triangle =height+base+length

class Triangle:
    def __init__(self,length,base,height):
        self.length=length
        self.base=base
        self.height=height
        
    def getLength(self):
        return self.length
    
    def getBase(self):
        return self.base
    
    def getHeight(self):
        return self.height
    
    
    def getArea(self):
        area=m.floor((self.height*self.base)/2)
        return area
    
    def getPerimeter(self):
        per=self.length+self.base+self.height
        return per
    
    def display(self):
        print("Details of Triangle  are given here:\n")
        print(f"Length of Trinagel is {self.getLength()} meter\n Base  of Tringle is {self.getBase()} meter\n Height of Triangle is {self.getHeight()} meter\n")
        


def main():
   radius=float(input("Enter radius for circle: "))
   l=float(input("Enter length for triangle and rectangle: "))
   w=float(input("Enter width for rectangle: "))
   h=float(input("Enter height for triangle: "))
   b=float(input("Enter base for triangle: "))
   
   
   circle=Circle(radius)
   
   circle.display()
   print(f"Area of circle is {circle.getArea()} meter square\n")
   print(f"Perimeter  of circle is {circle.getPerimeter()} meter\n")


   rectangle=Rectangle(l,w)
   
   rectangle.display()
   print(f"Area of rectangle is {rectangle.getArea()} meter square\n")
   print(f"Perimeter  of rectangle is {rectangle.getPerimeter()} meter\n")
   
   
   
   triangle=Triangle(l,b,h)
   triangle.display()
   print(f"Area of triangle is {rectangle.getArea()} meter square\n")
   print(f"Perimeter  of triangle is {rectangle.getPerimeter()} meter\n")
        
        
        
if __name__ == "__main__":
    main()
        