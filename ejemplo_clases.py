class Persona:
   apellido=""
   dni=""
   direccion=""
   nacionalidad=""

class Heroe(Persona):#Heroe hereda los atributos de la clase padre Persona
   #nombre,poder,apodo son variables de la clase Heroe
   #nombre,poder,apodo son atributos de la clase Hereo
   nombre = ""
   poder  = ""
   apodo  = ""
   edad   = 20
    #funcion especial de python que se ejecuta al crear un objeto de clase
    #funcion inicial o constructor
   def __init__(self,nombre,poder,apodo):
      self.nombre = nombre
      self.poder = poder
      self.apodo = apodo  

   def saludar(self):
      print(f"Hola {self.nombre} tu edad es: {self.edad}")


    #metodo magico para representar una cadena de devolucion final
   def __repr__(self):
     return f"Nombre:{self.nombre}, Poder:{self.poder}, Apodo:{self.apodo},Edad:{self.edad}"   
    
   def __str__(self):
       return f"Nombre:{self.nombre}, Poder:{self.poder}, Apodo:{self.apodo},Edad:{self.edad}"  

#spiderman es un objeto de la clase Heroe
#spiderman es una instancia de la clase Heroe
spiderman = Heroe("Peter Parker","Super fuerza","Hombre Araña")
ironman = Heroe("Tony Stark","Millonario","Hombre de acero")
ironman.edad=40
hulk = Heroe("Bruce Banner","Verde","Increible")
hulk.edad= 40

print(spiderman) 
ironman.apellido="stark"
ironman.dni="322323"
ironman.direccion="EEUU"
ironman.nacionalidad="EEUU" 
hulk 





