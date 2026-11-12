
import json
pokedex = open("./pokedex.json", encoding="utf8")
data = json.load(pokedex)
def lang():
    language = input("what language would you like to choose?")
    for pokemon in range(len(data)):
        if language == ("english"):
            print(data[pokemon]['name']['english'])
        if language == ("japanese"):
            print(data[pokemon]['name']['japanese'])
        if language == ("chinese"):
            print(data[pokemon]['name']['chinese'])
        if language == ("french"):
            print(data[pokemon]['name']['french'])
lang()
     
