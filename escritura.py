import json

aprendices =  [
              {"nombre": "Karen",
               "grupo": "25091",
               "competencias": {"etica": "A","Ingles":"A"}
              },
              {"nombre": "Juan",
               "grupo": "25093",
               "competencias": {"etica": "A","Ingles":"D", "fisica": "A"}
              },
              {"nombre": "Sergio",
               "grupo": "25091",
               "competencias": {"etica": "D","Ingles":"A"}
              }
             ]
with open ("aprendices.json", "w")as acrchivo_json:
    json.dump(aprendices,acrchivo_json,indent=4)