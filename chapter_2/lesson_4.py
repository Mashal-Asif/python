class Spaceship:
    def __init__(self, name, crew_capacity, speed):
        self.name = name
        self.crew_capacity = crew_capacity
        self.speed = speed

    def increase_speed(self):
        self.speed += 10
        print(f"{self.speed} is the new speed!")

    def set_crew_capacity(self, new_capacity):
        print(f"Previous Capacity: {self.crew_capacity}")
        self.crew_capacity = new_capacity
        print(f"New Capacity: {self.crew_capacity}")  

    def state_name(self):
        print(f"Spacecraft Name: {self.name}")
        

# Object creation
spaceship = Spaceship("Starship", crew_capacity=100, speed=500)

# Method calls
spaceship.state_name()
spaceship.set_crew_capacity(120)
spaceship.increase_speed()