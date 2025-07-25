import threading
import time

class Animal:
    def speak(self):
        raise NotImplementedError("Subclass must implement this method")

class Dog(Animal):
    def speak(self):
        time.sleep(1)  # Simulate some processing time
        return "Woof!"

class Cat(Animal):
    def speak(self):
        time.sleep(1)  # Simulate some processing time
        return "Meow!"

class Cow(Animal):
    def speak(self):
        time.sleep(1)  # Simulate some processing time
        return "Moo!"

def animal_sound(animal: Animal, name: str):
    sound = animal.speak()
    print(f"Sound of {name} is {sound}")

def main():
    # Create animal instances
    dog = Dog()
    cat = Cat()
    cow = Cow()

    # Create threads for each animal
    thread1 = threading.Thread(target=animal_sound, args=(dog, "Dog"))
    thread2 = threading.Thread(target=animal_sound, args=(cat, "Cat"))
    thread3 = threading.Thread(target=animal_sound, args=(cow, "Cow"))

    # Start all threads
    thread1.start()
    thread2.start()
    thread3.start()

    # Wait for all threads to complete
    thread1.join()
    thread2.join()
    thread3.join()

    print("All animals have spoken!")

if __name__ == "__main__":
    start_time = time.time()
    main()
    end_time = time.time()
    print(f"Total execution time: {end_time - start_time:.2f} seconds")