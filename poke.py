
import json
pokedex = open("./pokedex.json", encoding="utf8")
data = json.load(pokedex)

def name():
    poke = int(input("what pokemon do you want to see"))
    poke = ["id"]
name()



def lang():
    language = input("what language would you like to choose?")
    for pokemon in range(len(data)):
        if language == ("english"):
            print(data[pokemon]['name']['english'])
        elif language == ("japanese"):
            print(data[pokemon]['name']['japanese'])
        elif language == ("chinese"):
            print(data[pokemon]['name']['chinese'])
        elif language == ("french"):
            print(data[pokemon]['name']['french'])
        else:
            print ("langauge not avalible")
lang()


