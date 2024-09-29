# Define a base class called Animal
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

# Define a Dog class that inherits from Animal
class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

# Define a Cat class that inherits from Animal
class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

# Create instances (objects) of Dog and Cat
dog = Dog("Buddy")
cat = Cat("Whiskers")

# Use the speak method
print(dog.speak())  # Outputs: Buddy says Woof!
print(cat.speak())  # Outputs: Whiskers says Meow!

# Define the base class Animal
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

# Modify the Dog class to include a fetch method
class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

    def fetch(self, item):
        return f"{self.name} fetches the {item}!"

# Define the Cat class (unchanged)
class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

# Create instances (objects) of Dog and Cat
dog = Dog("Buddy")
cat = Cat("Whiskers")

# Use the new fetch method
print(dog.speak())  # Outputs: Buddy says Woof!
print(dog.fetch("ball"))  # Outputs: Buddy fetches the ball!
print(cat.speak())  # Outputs: Whiskers says Meow!

