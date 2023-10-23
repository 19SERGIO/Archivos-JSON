import json

texto_json = """
        {
            "nombre": "Wuaky",
            "institucion":"SENA",
            "edad":18,
            "activo":true,
            "deportes":["Futbol","Tenis", "Natacion"],
            "direccion":{
                        "principal" :"av.a mi casa",
                        "numero": 7,
                        "ciudad":"Manizales",
                        "pais":"Colombia"
                        }
        }

       
"""
diccionario = json.loads(texto_json)
print (type(diccionario))
print ("Diccionario completo:\n", diccionario)
print ("Solo la institución: ", diccionario["institucion"])
print ("Solo la dirección: ", diccionario["direccion"])
print ("Su segundo deporte favorito: ", diccionario["deportes"][1])