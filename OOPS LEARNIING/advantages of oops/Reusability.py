#  Reusing Animal Classes
# Let's reuse our Dog and Cat classes in a new project that also includes Bird objects.

# Reusing the existing Animal class
class Bird(Animal):
    def speak(self):
        return f"{self.name} says Tweet!"

# Create instances (objects) of Dog, Cat, and Bird
dog = Dog("Buddy")
cat = Cat("Whiskers")
bird = Bird("Tweety")

# Use the speak method
print(dog.speak())  # Outputs: Buddy says Woof!
print(cat.speak())  # Outputs: Whiskers says Meow!
print(bird.speak())  # Outputs: Tweety says Tweet!
