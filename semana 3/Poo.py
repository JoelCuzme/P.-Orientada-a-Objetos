class TemperaturaSemanal:
    def __init__(self):
        self.dias = []

    def pedir_datos(self):
        for i in range(1, 8):
            dia = int(input(f"Día {i}: "))
            self.dias.append(dia)

    def calcular_promedio(self):
        suma = sum(self.dias)
        promedio = suma / len(self.dias)
        print(f"El promedio semanal es de {promedio:.2f} grados")



temperatura_semanal = TemperaturaSemanal()
temperatura_semanal.pedir_datos()
temperatura_semanal.calcular_promedio()

