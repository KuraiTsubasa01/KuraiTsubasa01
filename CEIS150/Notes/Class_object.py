class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.speed = 0

    def accelerate(self, speed_increase):
        self.speed += speed_increase

    def brake(self, speed_decrease):
        self.speed -= speed_decrease
        if self.speed < 0:
            self.speed = 0

    def get_speed(self):
        return self.speed

# Creating an instance of the Car class
my_car = Car("Toyota", "Camry", 2020)

# Accelerating the car
my_car.accelerate(30)
print(f"Current speed: {my_car.get_speed()} mph")  # Output: Current speed: 30 mph

# Braking the car
my_car.brake(10)
print(f"Current speed: {my_car.get_speed()} mph")  # Output: Current speed: 20 mph

# Trying to brake too much
my_car.brake(30)
print(f"Current speed: {my_car.get_speed()} mph")  # Output: Current speed: 0 mph
