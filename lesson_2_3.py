#Excersise: 1
'''
fuel_remaining = 33.42
oxygen_levels = 21
fuel_remaining = int(fuel_remaining)
oxygen_levels = float(oxygen_levels)
print("Fuel remaining:", str(fuel_remaining) + " L")
print("Oxygen levels:", str(oxygen_levels) + " kPa")
'''
#Excersise: 2
#array manipulation
values = [1, 2, 3, 4, 5]
del values[len(values)-1]
values[1]=8
values[::-1]
values.append(9)
values.append(5)
print(values)
#Excersise: 3

thrust = float(input("Enter thrust of engine: "))
mass_flow_rate = float(input("Enter mass flow rate of propellant: "))
specific_impulse = thrust / (mass_flow_rate * 9.81)
exhaust_velocity = specific_impulse * 9.81
print("Specific Impulse: " + str(specific_impulse))
print("Exhaust Velocity: " + str(exhaust_velocity))

# Control Structure
planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
for planet in planets:
    print(planet)
#Excersise: 4
# Dictionary: celestial object name → luminosity value
celestial_objects = {
    "Sirius": 25,
    "Andromeda Galaxy": 1000000,
    "Jupiter": 0.00006,
    "Pleiades": 100,
    "Orion Nebula": 10000
}

# -----------------------------
# 1. Print all celestial names
# -----------------------------
for name in celestial_objects:
    # dictionary loop gives ONLY keys (names)
    print(name)

# -----------------------------
# 2. Store all luminosities in a list
# -----------------------------
luminosities = []  # empty list to store values

for name, luminosity in celestial_objects.items():
    # .items() gives BOTH name and value

    luminosities.append(luminosity)
    # append() means:
    # "take this value and ADD it to the END of the list"

# -----------------------------
# 3. Print luminosities < 200 using while loop
# -----------------------------
index = 0  # start from first element in list

while index < len(luminosities):
    # check each value one by one

    if luminosities[index] < 200:
        # only print if condition is true
        print(luminosities[index])

    index += 1  # move to next element
    
 #Excersise: 5
 
mission_duration = 10  # Duration of the mission in hours
fuel_level = 1000  # Initial fuel level in gallons
distance_to_destination = 500000  # Distance to the destination in kilometers
mission_time = 0  # Initialize mission time
fuel_consumption_rate = 50  # gallons per hour 
distance_traveled_per_hour = 50000  # kilometers per hour

while mission_time < mission_duration:
    # Update mission parameters
    fuel_level -= fuel_consumption_rate
    distance_to_destination -= distance_traveled_per_hour

    # Display mission updates
    print("Mission Time:", mission_time, "hours")
    print("Remaining Fuel:", fuel_level, "gallons")
    print("Distance to Destination:", distance_to_destination, "kilometers\n")

    # Check mission status
    if fuel_level <= 0 or distance_to_destination <= 0:
        break

    # Increment mission time
    mission_time += 1
print("Mission Complete!")