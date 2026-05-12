from pandas import Series
import numpy as np
import pandas as pd


# -----------------------
# Series from NumPy array
# -----------------------
data = np.array([10, 20, 30, 40, 50])
series = Series(data)

print("\nSeries from NumPy array:")
print(series)


# -----------------------
# Exercise 01
# -----------------------
planet_distances_dict = {
    'Mercury': 57.9,
    'Venus': 108.2,
    'Earth': 149.6,
    'Mars': 227.9,
    'Jupiter': 778.6,
    'Saturn': 1433.5,
    'Uranus': 2872.5,
    'Neptune': 4495.1,
    'Pluto': 5906.4
}

moon_data = {
    'Planet': ['Jupiter', 'Jupiter', 'Saturn', 'Saturn', 'Uranus', 'Neptune'],
    'Moon': ['Io', 'Ganymede', 'Titan', 'Rhea', 'Titania', 'Triton'],
    'Diameter (km)': [3642, 5262, 5150, 1528, 1578, 2707],
    'Orbital Period (days)': [1.77, 7.15, 15.95, 4.52, 8.71, 5.88]
}

# Create structures
planet_distances = pd.Series(planet_distances_dict)
moon_characteristics = pd.DataFrame(moon_data)

# Analysis
print("\nAverage distance of planets from the Sun:")
print(planet_distances.mean())


print("\nNumber of moons for each outer planet:")
outer_planets = ['Jupiter', 'Saturn', 'Uranus', 'Neptune']

for planet in outer_planets:
    filtered = moon_characteristics[moon_characteristics['Planet'] == planet]
    num_moons = filtered.shape[0]
    print(f"{planet}: {num_moons}")


print("\nLargest moon of each outer planet:")
for planet in outer_planets:
    filtered = moon_characteristics[moon_characteristics['Planet'] == planet]
    sorted_data = filtered.sort_values(by='Diameter (km)', ascending=False)
    largest_moon = sorted_data.iloc[0]

    print(f"{planet}: {largest_moon['Moon']} ({largest_moon['Diameter (km)']} km)")


# -----------------------
# Exercise 02
# -----------------------
space_x_missions_csv = "https://raw.githubusercontent.com/BriantOliveira/SpaceX-Dataset/master/dataset/SpaceX-Missions.csv"

launches_dataset = pd.read_csv(space_x_missions_csv)

print("\nFirst 5 rows:")
print(launches_dataset.head())

print("\nCustomer Country column:")
print(launches_dataset["Customer Country"])

print("\nUnique countries:")
print(pd.unique(launches_dataset["Customer Country"]))

print("\nGrouped by country (first rows of each group):")
launches_by_country = launches_dataset.groupby("Customer Country")
print(launches_by_country.head())

print("\nPayload < 4000 kg:")
print(launches_dataset[launches_dataset["Payload Mass (kg)"] < 4000])

print("\nMedian payload for United States:")
usa_median = launches_dataset[
    launches_dataset["Customer Country"] == "United States"
]["Payload Mass (kg)"].median()

print(usa_median)