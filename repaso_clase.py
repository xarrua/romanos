import datetime

class Persona:
    #self seria una referencia a las variables y funciones de la clase
    def __init__(self,nombre,email):
        self.nombre=nombre 
        self.email=email
        self.fecha = datetime.datetime.now()

    #metodo magico para mostrar los datos de un objeto en string
    def __str__(self):
        return f"Nombre: {self.nombre}, Email: {self.email}, Fecha: {self.fecha}"
    #metodo magico para mostrar la representacion de un objeto en string
    def __repr__(self):
        return f"Nombre: {self.nombre}, Email: {self.email}, Fecha: {self.fecha}"
    #metodo magico para sumar atributos de objetos
    def __add__(self,valor):
        return f"La suma de valores: { 10 + valor.valor_inicial}"

class Numero():
    def __init__(self,valor):
        self.valor_inicial=valor

objetoPersona= Persona("Jose","jose@email.com")
objetoNumero=Numero(25)

resultado = objetoPersona + objetoNumero
print(resultado)
#print("aqui",objetoPersona)
#print("metodo str:",str( datetime.datetime.now() ))
#print("metodo repr", repr( datetime.datetime.now() ) )         
