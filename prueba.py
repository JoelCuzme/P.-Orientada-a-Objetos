class Usuario:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
    def __str__(self):
        return f'{self.nombre} {self.apellido} {self.edad}'

class Recoletor:
    def __init__(self):
        self.usuarios = {}

    def agregar_usuario(self,id, usuario):
        self.usuarios[id] = usuario
        print("Se añadio correctamente")

    def mostrar_usuarios(self):
        for lista in self.usuarios.values():
            print(lista)
    def guardar (self, archivo="prueba.txt"):
        with open(archivo,"w") as a:
            for usuario in self.usuarios.values():
                a.write(f"{usuario.nombre},{usuario.apellido},{usuario.edad}\n")
        print("Guardado exitosamente")


recoletor = Recoletor()

usuario1 = Usuario("<NAME>", "<NAME>", "23")

recoletor.agregar_usuario(1, usuario1)

mostrar = recoletor.mostrar_usuarios()
Guardar= recoletor.guardar("prueba.txt")

print(mostrar)



