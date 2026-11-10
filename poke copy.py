import json
pokedex = open("./pokedex.json", encoding="utf8")
data = json.load(pokedex)
language = input("what language would you like to choose?")
for pokemon in range (len(data)):
    count = 0
    if language == ("english"):
        print(data[pokemon]['name']['english'])
    if language == ("japanese"):
        print(data[pokemon]['name']['japanese'])
    if language == ("chinese"):
        print(data[pokemon]['name']['chinese'])
    if language == ("french"):
        print(data[pokemon]['name']['french'])
    else:
        count += 1
if count == 1:
    print("not a valid language")    
        
