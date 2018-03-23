
# Dictionaries Mission - Section 9
planet_names = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Neptune", "Uranus"]
short_names = []
long_names = []

for name in planet_names:
    if len(name) > 5:
        long_names.append(name)
    else:
        short_names.append(name)

# Dictionaries Mission
# 09 - Counting with Dictionaries
pantry = ["apple", "orange", "grape", "apple", "orange", "apple", "tomato", "potato", "grape"]
pantry_counts = {}

for item in pantry:
    if item in pantry_counts:
        pantry_counts[item] += 1
    else:
        pantry_counts[item] = 1

# Dictionaries Mission
# 11 - Counting the weather
# Needs to have a list containing climates for each day ( ['Sunny', 'Foggy',....'Storm'] )
weather_counts = {}

for climate in weather:
    if climate in weather_counts:
        weather_counts[climate] += 1
    else:
        weather_counts[climate] = 1
