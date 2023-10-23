import json

class Aprendiz:
  def __init__(self, nombre, edad, sexo):
    self.nombre = nombre
    self.edad = edad
    self.sexo = sexo
    
serializacion1="""
{
    "nombre":"Wuakypandy",
    "edad":18,
    "sexo":"F"
}
"""
serializacion2 = """
{
    "nombre":"Drago",
    "edad":23,
    "sexo":"M"
}
"""


#Deserializacion de los objetos
dic1 = json.loads(serializacion1)
aprendiz1 = Aprendiz(dic1["nombre"], dic1["edad"], dic1["sexo"])

dic2 = json.loads(serializacion1)
aprendiz2 = Aprendiz(dic2["nombre"], dic2["edad"], dic2["sexo"])

print (f"Datos del aprendiz1:\nnombre:{aprendiz1.nombre} edad: {aprendiz1.edad} sexo: {aprendiz1.sexo}")
print (f"Datos del aprendiz2:\nnombre:{aprendiz2.nombre} edad: {aprendiz2.edad} sexo: {aprendiz2.sexo}")
