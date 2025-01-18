class Vehiculo:
    def __init__(self, marca, modelo, color, velocidad):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self._velocidad = velocidad

    def __str__(self):
        informacion=[self.modelo,self.marca,self.color]
        print (informacion)

    def encender(self):
        print(f"El {self.modelo} está encendido.")
        return True

    def apagar(self):
        print(f"El {self.modelo} está apagado.")
        return False

    def calculo_avance(self, estado):
        if estado:
            try:
                distancia = float(input("Ingrese la distancia a recorrer (en km): "))
                tiempo = distancia / self._velocidad
                print(f"El {self.modelo} tardaría {tiempo:.2f} horas en recorrer {distancia} km.")
            except ValueError:
                print("Por favor, ingrese un número válido para la distancia.")
        else:
            print(f"El {self.modelo} está apagado y no puede avanzar.")


# Clase derivada Auto
class Auto(Vehiculo):
    def __init__(self, marca, modelo, color, velocidad, tipo_motor):
        super().__init__(marca, modelo, color, velocidad)
        self.tipo_motor = tipo_motor



    def calculo_avance(self, estado):
        if estado:
            try:
                distancia = float(input("Ingrese la distancia a recorrer (en km): "))
                tiempo = distancia / self._velocidad
                print(f"El auto {self.modelo} con motor {self.tipo_motor} tardaría {tiempo:.2f} horas en recorrer {distancia} km.")
            except ValueError:
                print("Por favor, ingrese un número válido para la distancia.")
        else:
            print(f"El auto {self.modelo} está apagado y no puede avanzar.")



class Bicicleta(Vehiculo):
    def __init__(self, marca, modelo, color, velocidad, tipo):
        super().__init__(marca, modelo, color, velocidad)
        self.tipo = tipo

    def calculo_avance(self):
        distancia = float(input("Ingrese la distancia a recorrer (en km): "))
        tiempo = distancia / self._velocidad
        print(f"El {self.modelo} tardaría {tiempo:.2f} horas en recorrer {distancia} km.")






#Auto
auto = Auto("Mazda", "Corolla", "Blanco", 120, "Híbrido")
auto.__str__()
estado_auto = auto.encender()
auto.calculo_avance(estado_auto)
auto.apagar()


#Bicicleta
bicicleta = Bicicleta("Trek", "FX 3", "Negro", 25, "Montaña")
bicicleta.__str__()
bicicleta.calculo_avance()
