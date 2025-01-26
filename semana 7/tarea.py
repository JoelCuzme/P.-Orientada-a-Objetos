class Personaje:
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = vida

class Arquero(Personaje):
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        informacion=[self.nombre, self.fuerza, self.inteligencia, self.defensa, self.vida]
        print(informacion)

    def __del__(self):
        print(f"El personaje {self.nombre} ha sido eliminado")

class Guerrero(Personaje):
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, Espada):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.espada = Espada
        informacion=[self.nombre, self.fuerza, self.inteligencia, self.defensa, self.vida, self.espada]
        print(informacion)

    def __del__(self):
        print(f"El personaje {self.nombre} ha sido eliminado")

personaje1= Arquero("Jhin",100,40,20,500,)
personaje2= Guerrero("Garen",200,40,20,500,15)