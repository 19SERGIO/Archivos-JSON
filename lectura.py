import json
with open ("auditorias.json") as archivo_json:
    audit= json.load(archivo_json)

print(audit)