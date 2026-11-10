import csv, os

class DataLoader:
    @staticmethod
    def load_csv(file_path):
        """Reads a CSV file and returns a Table object initialized with the rows."""
        rows = []
        with open(file_path, mode='r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                rows.append(dict(row))
        return Table(file_path, rows)
    
class Table:
    def __init__(self, name, rows):
        self.name = name
        self.rows = rows

    def filter(self, condition):
        """Returns a new Table instance containing filtered rows."""
        filtered_rows = [row for row in self.rows if condition(row)]
        return Table(f"{self.name}_filtered", filtered_rows)

    def aggregate(self, key, func):
        """Aggregates values of a specific key across rows."""
        values = []
        for row in self.rows:
            val = row[key]
            try:
                values.append(float(val))
            except (ValueError, TypeError):
                values.append(val)
        return func(values)

    def select(self, key):
        """Returns a list of values for a given column key."""
        return [row[key] for row in self.rows]


# Determine absolute path to Cities.csv
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__))
)

# Load the dataset
cities_table = DataLoader.load_csv(os.path.join(__location__, 'Cities.csv'))

# Print first 5 cities only
for city in cities_table.rows[:5]:
    print(city)
print()

# Print the average temperature of all the cities
print("The average temperature of all the cities:")
avg_temp_all = cities_table.aggregate(
    "temperature",
    lambda temps: sum(temps) / len(temps)
)
print(avg_temp_all)
print()

# Print all cities in Germany
print("All cities in Germany:")
germany_table = cities_table.filter(lambda c: c["country"] == "Germany")
for city_name in germany_table.select("city"):
    print(city_name)
print()

# Print all cities in Spain with a temperature above 12°C
print("All cities in Spain with a temperature above 12°C:")
spain_warm_table = cities_table.filter(
    lambda c: c["country"] == "Spain" and float(c["temperature"]) > 12
)
for city_name in spain_warm_table.select("city"):
    print(city_name)
print()

# Count the number of unique countries
print("Number of unique countries:")
num_countries = cities_table.aggregate(
    "country",
    lambda countries: len(set(countries))
)
print(num_countries)
print()

# Print the average temperature for all the cities in Germany
print("The average temperature for all the cities in Germany:")
avg_germany = germany_table.aggregate(
    "temperature",
    lambda temps: sum(temps) / len(temps)
)
print(avg_germany)
print()

# Print the max temperature for all the cities in Italy
print("The max temperature for all the cities in Italy:")
italy_table = cities_table.filter(lambda c: c["country"] == "Italy")
max_italy_temp = italy_table.aggregate("temperature", max)
print(max_italy_temp)