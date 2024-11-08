"""
This program defines 2 classes (Table and TableDB) to operate and manipulate data from CSV files
"""
import csv


class Table:
    """This class represent a table imported from a CSV file"""
    def __init__(self, table_name, table_data):
        """Initialize the Table with name & data"""
        self.table_name = table_name
        self.table_data = table_data  # List of dict from CSV

    @classmethod
    def open_csv(cls, table_name):
        """Open a CSV file and import the data into a Table instance"""
        table_data = []
        with open(table_name) as f:
            rows = csv.DictReader(f)
            for r in rows:
                table_data.append(dict(r))  # Convert each row to a dictionary
        return cls(table_name, table_data)

    def filter(self, condition):
        """Filter rows based on an input condition"""
        return [row for row in self.table_data if condition(row)]

    def aggregate(self, aggregation_function, aggregation_key):
        """Aggregate data based on an input function and key (e.g. AVG, MIN, MAX)"""
        values_set = [float(row[aggregation_key]) for row in self.table_data]
        return aggregation_function(values_set)

    def __str__(self):
        return f"Table Name: {self.table_name} ({len(self.table_data)} Rows)"


class TableDB:
    """This class is provided in order to manage Table instances"""
    def __init__(self):
        """Initialize the TableDB with an empty set"""
        self.table_db = []

    def insert(self, table):
        """Insert a table into the self.tableDB()"""
        self.table_db.append(table)

    def search(self, table_name_input):
        """Search for a table by an input name"""
        for table in self.table_db:
            if table.table_name == table_name_input:
                return table
        return None


# ------------------------------- MAIN PART ------------------------------- #
db = TableDB()  # Create an instance of TableDB

table_cities = Table.open_csv('Cities.csv')
table_countries = Table.open_csv('Countries.csv')
# Import tables from CSV files

db.insert(table_cities)
db.insert(table_countries)
# Insert tables into db


# PRINT section
table_searched = db.search('Cities.csv')  # Search for a table by a name input

print("The average temperature of all the cities:")
temp_avg = table_searched.aggregate(lambda temps: sum(temps) / len(temps), 'temperature')
print(f"{temp_avg:.4f}")

italy_cities = table_searched.filter(lambda x: x['country'] == 'Italy')
print("\nAll the cities in Italy:")
cities_set = [city['city'] for city in italy_cities]
print(cities_set)

print("\nThe average temperature of all the cities in Italy :")
avg_temp_italy = table_searched.aggregate(lambda temps: sum(temps) / len(temps), 'temperature')
print(f"{avg_temp_italy:.4f}")

print("\nThe max temperature of all the cities in Italy :")
max_temp_italy = table_searched.aggregate(max, 'temperature')
print(f"{max_temp_italy:.4f}")

print("\nThe min temperature of all the cities in Italy :")
min_temp_italy = table_searched.aggregate(min, 'temperature')
print(f"{min_temp_italy:.4f}\n")

# Print cities with latitude >= 60.0
filtered_cities = table_searched.filter(lambda _city: float(_city['latitude']) >= 60.0)
for _city in filtered_cities:
    print(_city)

# Print AVG, MIN, and MAX temp for Italy and Sweden
for country in ['Italy', 'Sweden']:
    cities_inside = table_searched.filter(lambda _city: _city['country'] == country)

    temp_avg = table_searched.aggregate(lambda n: round(sum(n)/len(n), 4), 'temperature')
    temp_min = table_searched.aggregate(min, 'temperature')
    temp_max = table_searched.aggregate(max, 'temperature')

    print(f"\nTemperature in {country}")
    print(f"Average: {temp_avg}")
    print(f"Minimum: {temp_min}")
    print(f"Maximum: {temp_max}")
