import json

diccionario ={
    "marca":"mazda",
    "modelo":2023,
    "accesorios":["ABS","vidrios","sensores"]
}

texto_json =json.dumps(diccionario)
print (type( texto_json))
print (texto_json)