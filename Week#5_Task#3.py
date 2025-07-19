# Concept of inheritence 
#Parent Class
from hashlib import new


class Vehicle:
    def __init__(self, brand, model,price):
        self.brand = brand
        self.model = model
        self.price = price

    def display_info(self):
        print(f"Vehicle Brand: {self.brand}\nModel: {self.model}\nPrice: {self.price}")


class Car(Vehicle):
    def __init__(self, brand, model, price, seats, owner):
        super().__init__(brand, model, price)
        self.seats = seats
        self.owner = owner
    def display_info(self):
        super().display_info()
        print(f"Car Seats: {self.seats}\nOwner: {self.owner}")
        


class Bike(Vehicle):
    def __init__(self, brand, model, price,owner):
        super().__init__(brand, model, price)
        self.owner = owner
    def display_info(self):
        super().display_info()
        print(f"Owner: {self.owner}")
        
        
 
 
def main():
    print("Welcome to the Vehicle Management System")
    print("Please select a vehicle type to enter details:")
    print("1. Car")
    print("2. Bike")
    print("3. Exit")
    
    choice = input("Enter your choice (1/2/3): ")
    
    if choice == '1':
        b = "car"
    elif choice == '2':
        b = "bike"
    elif choice == '3':
        print("Exiting the system.")
        return
    else:
        print("Invalid choice. Please try again.")
        main()
        return
    if b == "car":
        brand = input("Enter the brand of the car: ")
        model = input("Enter the model of the car: ")
        price = float(input("Enter the price of the car: "))
        seats = int(input("Enter the number of seats in the car: "))
        owner = input("Enter the owner's name: ")
    
        car = Car(brand, model, price, seats, owner)
        car.display_info()

    elif b == "bike":
        brand = input("Enter the brand of the bike: ")
        model = input("Enter the model of the bike: ")
        price = float(input("Enter the price of the bike: "))
        owner = input("Enter the owner's name: ")
    
        bike = Bike(brand, model, price, owner)
        bike.display_info()
    
    print("Thank you for using the Vehicle Management System!")
    
    
if __name__ == "__main__":
    main()
    