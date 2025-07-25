import math as m
import json
import os

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def getRadius(self):
        return self.radius
    
    def getArea(self):
        return m.pi * (self.radius ** 2)
    
    def getPerimeter(self):
        return 2 * m.pi * self.radius
    
    def display(self):
        print("\nCircle Details:")
        print(f"Radius: {self.radius} meters")
        print(f"Area: {self.getArea():.2f} square meters")
        print(f"Circumference: {self.getPerimeter():.2f} meters")
    
    def to_dict(self):
        return {
            'type': 'circle',
            'radius': self.radius,
            'area': self.getArea(),
            'perimeter': self.getPerimeter()
        }

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def getLength(self):
        return self.length
    
    def getWidth(self):
        return self.width
    
    def getArea(self):
        return self.length * self.width
    
    def getPerimeter(self):
        return 2 * (self.length + self.width)
    
    def display(self):
        print("\nRectangle Details:")
        print(f"Length: {self.length} meters")
        print(f"Width: {self.width} meters")
        print(f"Area: {self.getArea():.2f} square meters")
        print(f"Perimeter: {self.getPerimeter():.2f} meters")
    
    def to_dict(self):
        return {
            'type': 'rectangle',
            'length': self.length,
            'width': self.width,
            'area': self.getArea(),
            'perimeter': self.getPerimeter()
        }

class Triangle:
    def __init__(self, length, base, height):
        self.length = length
        self.base = base
        self.height = height
    
    def getLength(self):
        return self.length
    
    def getBase(self):
        return self.base
    
    def getHeight(self):
        return self.height
    
    def getArea(self):
        return (self.height * self.base) / 2
    
    def getPerimeter(self):
        return self.length + self.base + self.height
    
    def display(self):
        print("\nTriangle Details:")
        print(f"Length: {self.length} meters")
        print(f"Base: {self.base} meters")
        print(f"Height: {self.height} meters")
        print(f"Area: {self.getArea():.2f} square meters")
        print(f"Perimeter: {self.getPerimeter():.2f} meters")
    
    def to_dict(self):
        return {
            'type': 'triangle',
            'length': self.length,
            'base': self.base,
            'height': self.height,
            'area': self.getArea(),
            'perimeter': self.getPerimeter()
        }

def save_to_file(shapes, filename="shapes.json"):
    try:
        with open(filename, 'w') as f:
            json.dump([shape.to_dict() for shape in shapes], f, indent=4)
        print(f"\nSuccessfully saved shapes to {filename}")
    except Exception as e:
        print(f"\nError saving to file: {e}")

def load_from_file(filename="shapes.json"):
    try:
        if not os.path.exists(filename):
            print(f"\nFile {filename} not found.")
            return []
        
        with open(filename, 'r') as f:
            data = json.load(f)
        
        shapes = []
        for item in data:
            if item['type'] == 'circle':
                shapes.append(Circle(item['radius']))
            elif item['type'] == 'rectangle':
                shapes.append(Rectangle(item['length'], item['width']))
            elif item['type'] == 'triangle':
                shapes.append(Triangle(item['length'], item['base'], item['height']))
        
        print(f"\nSuccessfully loaded {len(shapes)} shapes from {filename}")
        return shapes
    except Exception as e:
        print(f"\nError loading from file: {e}")
        return []

def display_shapes(shapes):
    for shape in shapes:
        shape.display()
        print()

def main():
    shapes = []
    
    while True:
        print("\nShape Calculator Menu:")
        print("1. Create new shapes")
        print("2. Display current shapes")
        print("3. Save shapes to file")
        print("4. Load shapes from file")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            try:
                radius = float(input("Enter radius for circle (meters): "))
                length = float(input("Enter length for rectangle and triangle (meters): "))
                width = float(input("Enter width for rectangle (meters): "))
                height = float(input("Enter height for triangle (meters): "))
                base = float(input("Enter base for triangle (meters): "))
                
                shapes.extend([
                    Circle(radius),
                    Rectangle(length, width),
                    Triangle(length, base, height)
                ])
                
                print("\nCreated new shapes successfully!")
            except ValueError:
                print("\nInvalid input. Please enter numeric values.")
        
        elif choice == '2':
            if not shapes:
                print("\nNo shapes to display. Create some first!")
            else:
                display_shapes(shapes)
        
        elif choice == '3':
            if not shapes:
                print("\nNo shapes to save. Create some first!")
            else:
                filename = input("Enter filename to save (default: shapes.json): ") or "shapes.json"
                save_to_file(shapes, filename)
        
        elif choice == '4':
            filename = input("Enter filename to load (default: shapes.json): ") or "shapes.json"
            loaded_shapes = load_from_file(filename)
            if loaded_shapes:
                shapes = loaded_shapes
        
        elif choice == '5':
            print("\nExiting program...")
            break
        
        else:
            print("\nInvalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()