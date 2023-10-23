import json

class Aprendiz:
    def __init__(self, nombre, edad, sexo):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo

aprendiz1 = Aprendiz ("Karen", 18, "F")
aprendiz2 = Aprendiz ("Sergio",23,"M")

#Serializacion de los objetos
print(aprendiz1.__dict__)
serializacion1= json.dumps(aprendiz1.__dict__, indent=4)#convierte el objeto 
serializacion2 =json.dumps(aprendiz2.__dict__,indent=4)#y se pasan a una funcion dumps
print ("objeto 1 serializacion\n", serializacion1)
print ("objeto 2 serializacion\n", serializacion2)