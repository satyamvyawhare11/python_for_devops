info = {
    "apple" : "red",
    "banana" : "yellow",
    "graps_green" : True,
    "onion_in_basket": 100,
    "fav": "mango"
}

print(info)
print(f"My fav fruit is {info["fav"]}")
print(f"color of mango is {info.get("mango", "% not found %")}")

info.update({"king_of_jungle":"lion"})

print(info)
print(info.items())
print(info.keys())

for key,value in info.items():
    print(key,value)

