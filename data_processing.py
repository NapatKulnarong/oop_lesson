import csv
import os


class City:
    def __init__(self, city, country, latitude, longitude, temperature):
        self.city = city
        self.country = country
        self.latitude = latitude
        self.longitude = longitude
        self.temperature = temperature


class WeatherData:
    def __init__(self, cities, countries):
        self.cities = cities
        self.countries = countries

    @classmethod
    def open_csv(cls, cities_csv, countries_csv):
        cities = []
        with open(cities_csv) as f:
            rows = csv.DictReader(f)
            for r in rows:
                cities.append(dict(r))

        countries = []
        with open(countries_csv) as f:
            rows = csv.DictReader(f)
            for r in rows:
                countries.append(dict(r))

        return cls(cities, countries)

    def filter(self, condition_function, dict_list):
        return [item for item in dict_list if condition_function(item)]
        # return: a list of dict that's matched with the condition

    def aggregate(self, aggregation_key, aggregation_function, dict_list):
        values_set = [float(_dict[aggregation_key]) for _dict in dict_list]
        return aggregation_function(values_set)

    def get_cities_in_country(self, input_country):
        return [_city for _city in self.cities if _city['country'] == input_country]

    def print_avg_temp(self, cities):
        avg_temp = self.aggregate('temperature', lambda temps_set: sum(temps_set) / len(temps_set), cities)
        print(f"{avg_temp:.4f}")

    def print_min_temp(self, cities):
        min_temp = self.aggregate('temperature', lambda temps_set: min(temps_set), cities)
        print(f"{min_temp:.4f}")

    def print_max_temp(self, cities):
        max_temp = self.aggregate('temperature', lambda temps_set: max(temps_set), cities)
        print(f"{max_temp:.4f}")


__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
cities_import = os.path.join(__location__, 'Cities.csv')
countries_import = os.path.join(__location__, 'Countries.csv')

weather_data = WeatherData.open_csv(cities_import, countries_import)
# import cities and countries data from CSV files
# weather_data is an instance of the WeatherData class, it has 2 attributes
# 1. cities: a list of dictionaries showing city data
# 2. countries: a list of dictionaries showing country data


# PRINT
print("The average temperature of all the cities:")
weather_data.print_avg_temp(weather_data.cities)

italy_cities = weather_data.get_cities_in_country('Italy')

print("\nAll the cities in Italy:")
cities_set = []
for _dict in italy_cities:
    cities_set.append(_dict['city'])
print(cities_set)

print("\nThe average temperature of all the cities in Italy :")
weather_data.print_avg_temp(italy_cities)

print("\nThe max temperature of all the cities in Italy :")
weather_data.print_max_temp(italy_cities)

print("\nThe min temperature of all the cities in Italy :")
weather_data.print_min_temp(italy_cities)

# Cities with latitude >= 60.0
print()
filtered_cities = weather_data.filter(lambda _city: float(_city['latitude']) >= 60.0, weather_data.cities)
for _city in filtered_cities:
    print(_city)

# AVG, MIN, and MAX temp for Italy and Sweden
for country in ['Italy', 'Sweden']:
    cities_inside = list(filter(lambda _city: _city['country'] == country, weather_data.cities))

    temp_avg = weather_data.aggregate('temperature', lambda n: round(sum(n)/len(n), 4), cities_inside)
    temp_min = weather_data.aggregate('temperature', min, cities_inside)
    temp_max = weather_data.aggregate('temperature', max, cities_inside)

    print(f"\nTemperature in {country}")
    print(f"Average: {temp_avg}")
    print(f"Minimum: {temp_min}")
    print(f"Maximum: {temp_max}")




