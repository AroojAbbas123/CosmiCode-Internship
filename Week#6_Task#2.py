import math as m

class Circle:
    def __init__(self, radius):
        try:
            if radius <= 0:
                raise ValueError("Radius must be positive")
            self.radius = float(radius)
        except ValueError as e:
            print(f"Error creating Circle: {e}")
            raise

    def getRadius(self):
        return self.radius
    
    def getArea(self):
        try:
            area = m.pi * (self.radius ** 2)
            return round(area, 2)
        except Exception as e:
            print(f"Error calculating circle area: {e}")
            return None
    
    def getPerimeter(self):
        try:
            perimeter = 2 * m.pi * self.radius
            return round(perimeter, 2)
        except Exception as e:
            print(f"Error calculating circle perimeter: {e}")
            return None
    
    def display(self):
        print("\nDetails of Circle:")
        print(f"Radius: {self.radius} meters")

class Rectangle:
    def __init__(self, length, width):
        try:
            if length <= 0 or width <= 0:
                raise ValueError("Length and width must be positive")
            self.length = float(length)
            self.width = float(width)
        except ValueError as e:
            print(f"Error creating Rectangle: {e}")
            raise

    def getLength(self):
        return self.length
    
    def getWidth(self):
        return self.width
    
    def getArea(self):
        try:
            area = self.length * self.width
            return round(area, 2)
        except Exception as e:
            print(f"Error calculating rectangle area: {e}")
            return None
    
    def getPerimeter(self):
        try:
            perimeter = 2 * (self.length + self.width)
            return round(perimeter, 2)
        except Exception as e:
            print(f"Error calculating rectangle perimeter: {e}")
            return None
    
    def display(self):
        print("\nDetails of Rectangle:")
        print(f"Length: {self.length} meters")
        print(f"Width: {self.width} meters")

class Triangle:
    def __init__(self, length, base, height):
        try:
            if any(side <= 0 for side in [length, base, height]):
                raise ValueError("All sides must be positive")
            if not (length + base > height and length + height > base and base + height > length):
                raise ValueError("Invalid triangle - violates triangle inequality theorem")
            self.length = float(length)
            self.base = float(base)
            self.height = float(height)
        except ValueError as e:
            print(f"Error creating Triangle: {e}")
            raise

    def getLength(self):
        return self.length
    
    def getBase(self):
        return self.base
    
    def getHeight(self):
        return self.height
    
    def getArea(self):
        try:
            area = (self.height * self.base) / 2
            return round(area, 2)
        except Exception as e:
            print(f"Error calculating triangle area: {e}")
            return None
    
    def getPerimeter(self):
        try:
            perimeter = self.length + self.base + self.height
            return round(perimeter, 2)
        except Exception as e:
            print(f"Error calculating triangle perimeter: {e}")
            return None
    
    def display(self):
        print("\nDetails of Triangle:")
        print(f"Length: {self.length} meters")
        print(f"Base: {self.base} meters")
        print(f"Height: {self.height} meters")

def get_positive_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Value must be positive. Please try again.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a number.")

def main():
    try:
        print("Shape Calculator\n")
        
        radius = get_positive_input("Enter radius for circle (meters): ")
        length = get_positive_input("Enter length for rectangle and triangle (meters): ")
        width = get_positive_input("Enter width for rectangle (meters): ")
        height = get_positive_input("Enter height for triangle (meters): ")
        base = get_positive_input("Enter base for triangle (meters): ")

        # Create shapes
        circle = Circle(radius)
        rectangle = Rectangle(length, width)
        triangle = Triangle(length, base, height)

        # Display results
        circle.display()
        print(f"Area: {circle.getArea()} square meters")
        print(f"Circumference: {circle.getPerimeter()} meters")

        rectangle.display()
        print(f"Area: {rectangle.getArea()} square meters")
        print(f"Perimeter: {rectangle.getPerimeter()} meters")

        triangle.display()
        print(f"Area: {triangle.getArea()} square meters")
        print(f"Perimeter: {triangle.getPerimeter()} meters")

    except Exception as e:
        print(f"\nProgram encountered an error: {e}")
    finally:
        print("\nCalculation complete.")

if __name__ == "__main__":
    main()