import requests

# len is automatically in python

url = "https://pokeapi.co/api/v2/pokemon/lugia"
response = requests.get(url)
print(response)
# print(response.text["abilities"][0]["ability"]["name"])
# "turn it into a dictionary!"
data = response.json()
# print(data)
print(data.keys())

# You get:
# dict_keys(['abilities', 'base_experience', 'forms', 'game_indices', 'height', 'held_items', 'id', 'is_default', 'location_area_encounters', 'moves', 'name', 'order', 'past_types', 'species', 'sprites', 'stats', 'types', 'weight'])

# print(data["forms"])
print(data["moves"])

for move in data["moves"]:
    print("------")
    print(move)
