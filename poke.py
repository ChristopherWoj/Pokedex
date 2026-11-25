
import json
pokedex = open("./pokedex.json", encoding="utf8")
data = json.load(pokedex)

language = input("what language would you like to choose?  ")

def pokemon_search():
    type = input("what type do you want to see").capitalize()
    for pokemon in data:
        if type in pokemon["type"]:
             print (pokemon["name"][language])
        elif type in pokemon != ["type"]:
            print ("not avalible")
pokemon_search()





