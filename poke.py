import json
pokedex = open("./pokedex.json", encoding="utf8")
data = json.load(pokedex)
language = input("what language would you like to choose?")
for i in range (len(data)):
    print ("name")
