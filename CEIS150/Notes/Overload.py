class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        return "Some generic animal sound"

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def sound(self):
        return "Bark"

# Example usage:
generic_animal = Animal("Generic Animal")
print(generic_animal.sound())  # Output: Some generic animal sound

dog = Dog("Rex", "German Shepherd")
print(dog.sound())  # Output: Bark

