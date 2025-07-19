class Animal:
    def speak(self):
        raise NotImplementedError("Subclass must implement this method")

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

def animal_sound(animal: Animal):
    return animal.speak() 

dog = Dog()
cat = Cat()

print("Sound of Dog is", animal_sound(dog))
print("Sound of Cat is", animal_sound(cat))