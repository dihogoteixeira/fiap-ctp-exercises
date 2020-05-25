import json

dicionario = {
  "chaves" : ["Chaves do 8", "14/04/2016", "Recep_01"],
  "quico"  : ["Quico das Flores", "24/12/2017", "Raiox_03"],
  "florinda"  : ["Dona Florinda", "18/12/2017", "Raiox_02"]
}

with open("db1.json", "w") as json_file:
 json.dump(dicionario, json_file)