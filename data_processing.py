import csv
import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

cities = []
with open(os.path.join(__location__, 'Cities.csv')) as f:
    rows = csv.DictReader(f)
    for r in rows:
        cities.append(dict(r))

countries = []
with open(os.path.join(__location__, 'Countries.csv')) as f:
    rows = csv.DictReader(f)
    for r in rows:
        countries.append(dict(r))

# Print the average temperature of all the cities
print("The average temperature of all the cities:")
temps = []
for city in cities:
    temps.append(float(city['temperature']))
print(sum(temps) / len(temps))
print()

# Print all cities in Italy
cities_temp = []
my_country = 'Italy'
for city in cities:
    if city['country'] == my_country:
        cities_temp.append(city['city'])
print("All the cities in", my_country, ":")
print(cities_temp)
print()

# Print the average temperature for all the cities in Italy
# Write code for me
temps = []
my_country = 'Italy'
for city in cities:
    if city['country'] == my_country:
        temps.append(float(city['temperature']))
print("The average temperature of all the cities in", my_country, ":")
print(sum(temps) / len(temps))
print()

# Print the max temperature for all the cities in Italy
# Write code for me
temps = []
my_country = 'Italy'
for city in cities:
    if city['country'] == my_country:
        temps.append(float(city['temperature']))
print("The max temperature of all the cities in", my_country, ":")
print(max(temps))
print()

# Print the min temperature for all the cities in Italy
# Write code for me
temps = []
my_country = 'Italy'
for city in cities:
    if city['country'] == my_country:
        temps.append(float(city['temperature']))
print("The min temperature of all the cities in", my_country, ":")
print(min(temps))
print()


# Let's write a function to filter out only items that meet the condition
# Hint: condition will be associated with an anonymous function, e.x., lamdbda x: max(x)
def filter(condition, dict_list):
    filtered_list = []
    for item in dict_list:
        if condition(item):
            filtered_list.append(item)
    return filtered_list


x = filter(lambda x: float(x['latitude']) >= 60.0, cities)
for item in x:
    print(item)


# Let's write a function to do aggregation given an aggregation function and an aggregation key
def aggregate(aggregation_key, aggregation_function, dict_list):
    set_of_values = [float(value[aggregation_key]) for value in dict_list]
    return aggregation_function(set_of_values)


# Let's write code to
# - print the average temperature for all the cities in Italy
# - print the average temperature for all the cities in Sweden
# - print the min temperature for all the cities in Italy
# - print the max temperature for all the cities in Sweden
focused_countries = ["Italy", "Sweden"]

for country in focused_countries:
    cities_inside = filter(lambda city: city['country'] == country, cities)

    temp_avg = aggregate('temperature', lambda n: round(sum(n) / len(n), 4), cities_inside)
    temp_min = aggregate('temperature', min, cities_inside)
    temp_max = aggregate('temperature', max, cities_inside)

    print("______________")
    print(f"Temperature in {country}")
    print(f"Average: {temp_avg}")
    print(f"Minimum: {temp_min}")
    print(f"Maximum: {temp_max}")

print("______________")


