import json

with open("auditorias.json") as archivo_json:
  audit = json.load(archivo_json)

print ("No autenticados")
for registro in audit:
  if registro["autenticado"] == False:
      print ("ip:",registro["ip"])
      print ("fecha:",registro["fecha"])
      print ("hora:",registro["hora"])
      print ("operacion:",registro["operacion"])
      print ("autenticado:",registro["autenticado"])