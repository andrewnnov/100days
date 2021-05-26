travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]


def add_new_country(country, visits, cities):
    new_place = {}
    new_place["country"] = country
    new_place["visits"] = visits
    new_place["cities"] = cities

    travel_log.append(new_place)



add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
