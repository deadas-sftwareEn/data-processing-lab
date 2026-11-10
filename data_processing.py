import csv, os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

cities = []
with open(os.path.join(__location__, 'Cities.csv')) as f:
    rows = csv.DictReader(f)
    for r in rows:
        cities.append(dict(r))

# Print first 5 cities only
for city in cities[:5]:
    print(city)

# Print the average temperature of all the cities
print("The average temperature of all the cities:")
temps = []
for city in cities:
    temps.append(float(city['temperature']))
print(sum(temps)/len(temps))
print()

# Print the average temperature of all the cities
print("The average temperature of all the cities:")
temps = [float(city['temperature']) for city in cities]
print(sum(temps)/len(temps))
print()

# Print all cities in Germany

print("All cities in Germany:")
for city in cities:
    if city["country"] == "Germany":
        print(city["city"])
print()

# Print all cities in Spain with a temperature above 12°C

print("All cities in Spain with a temperature above 12°C:")
for city in cities:
    if city["country"] == "Spain" and float(city["temperature"]) > 12:
        print(city["city"])
print()

# Count the number of unique countries

print("Number of unique countries:")
counted = []
for city in cities:
    if city["country"] not in counted:
        counted.append(city["country"])
print(len(counted))
print()

# Print the average temperature for all the cities in Germany

print("the average temperature for all the cities in Germany")
germany_temps = []
for city in cities:
    if city["country"] == "Germany":
        germany_temps.append(float(city["temperature"]))
avg_germany = sum(germany_temps)/len(germany_temps)
print(avg_germany)
print()

# Print the max temperature for all the cities in Italy

print("the max temperature for all the cities in Italy:")
italy_temps = []
for city in cities:
    if city["country"] == "Italy":
        italy_temps.append(float(city["temperature"]))
print(max(italy_temps))