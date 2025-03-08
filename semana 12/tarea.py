class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.titulo_autor = (titulo, autor)
        self.categoria = categoria
        self.isbn = isbn

    def __str__(self):
        return f"{self.titulo_autor[0]} por {self.titulo_autor[1]}"

class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []

class Biblioteca:
    def __init__(self):
        self.libros_disponibles = {}
        self.usuarios = {}

    def añadir_libro(self, libro):
        if libro.isbn not in self.libros_disponibles:
            self.libros_disponibles[libro.isbn] = libro
            print(f"Libro '{libro.titulo_autor[0]}' añadido.")
        else:
            print(f"El libro con ISBN {libro.isbn} ya existe.")

    def quitar_libro(self, isbn):
        if isbn in self.libros_disponibles:
            del self.libros_disponibles[isbn]
            print(f"Libro con ISBN {isbn} eliminado.")
        else:
            print(f"El libro con ISBN {isbn} no existe.")

    def registrar_usuario(self, usuario):
        if usuario.id_usuario not in self.usuarios:
            self.usuarios[usuario.id_usuario] = usuario
            print(f"Usuario '{usuario.nombre}' registrado.")
        else:
            print(f"El ID {usuario.id_usuario} ya está registrado.")

    def dar_de_baja_usuario(self, id_usuario):
        if id_usuario in self.usuarios:
            del self.usuarios[id_usuario]
            print(f"Usuario con ID {id_usuario} dado de baja.")
        else:
            print(f"El ID {id_usuario} no está registrado.")

    def prestar_libro(self, id_usuario, isbn):
        if id_usuario in self.usuarios and isbn in self.libros_disponibles:
            self.usuarios[id_usuario].libros_prestados.append(self.libros_disponibles[isbn])
            del self.libros_disponibles[isbn]
            print(f"Libro prestado a {self.usuarios[id_usuario].nombre}.")
        else:
            print("Usuario o libro no encontrado.")

    def devolver_libro(self, id_usuario, isbn):
        if id_usuario in self.usuarios:
            for libro in self.usuarios[id_usuario].libros_prestados:
                if libro.isbn == isbn:
                    self.libros_disponibles[isbn] = libro
                    self.usuarios[id_usuario].libros_prestados.remove(libro)
                    print(f"Libro devuelto por {self.usuarios[id_usuario].nombre}.")
                    return
            print(f"El libro con ISBN {isbn} no fue prestado a este usuario.")
        else:
            print(f"El ID {id_usuario} no está registrado.")

    def buscar_libro(self, **kwargs):
        resultados = [libro for libro in self.libros_disponibles.values() if any(getattr(libro, k) == v for k, v in kwargs.items())]
        if resultados:
            print("Resultados de búsqueda:")
            for libro in resultados:
                print(libro)
        else:
            print("No se encontraron libros.")

    def listar_libros_prestados(self, id_usuario):
        if id_usuario in self.usuarios:
            if self.usuarios[id_usuario].libros_prestados:
                print(f"Libros prestados a {self.usuarios[id_usuario].nombre}:")
                for libro in self.usuarios[id_usuario].libros_prestados:
                    print(libro)
            else:
                print(f"{self.usuarios[id_usuario].nombre} no tiene libros prestados.")
        else:
            print(f"El ID {id_usuario} no está registrado.")

def mostrar_menu():
    print("\n--- Menú de la Biblioteca ---")
    print("1. Añadir libro")
    print("2. Quitar libro")
    print("3. Registrar usuario")
    print("4. Dar de baja usuario")
    print("5. Prestar libro")
    print("6. Devolver libro")
    print("7. Buscar libro")
    print("8. Listar libros prestados")
    print("9. Salir")

# Ejemplo de uso
biblioteca = Biblioteca()

while True:
    mostrar_menu()
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        titulo = input("Título del libro: ")
        autor = input("Autor del libro: ")
        categoria = input("Categoría del libro: ")
        isbn = input("ISBN del libro: ")
        biblioteca.añadir_libro(Libro(titulo, autor, categoria, isbn))

    elif opcion == "2":
        isbn = input("ISBN del libro a quitar: ")
        biblioteca.quitar_libro(isbn)

    elif opcion == "3":
        nombre = input("Nombre del usuario: ")
        id_usuario = input("ID del usuario: ")
        biblioteca.registrar_usuario(Usuario(nombre, id_usuario))

    elif opcion == "4":
        id_usuario = input("ID del usuario a dar de baja: ")
        biblioteca.dar_de_baja_usuario(id_usuario)

    elif opcion == "5":
        id_usuario = input("ID del usuario: ")
        isbn = input("ISBN del libro a prestar: ")
        biblioteca.prestar_libro(id_usuario, isbn)

    elif opcion == "6":
        id_usuario = input("ID del usuario: ")
        isbn = input("ISBN del libro a devolver: ")
        biblioteca.devolver_libro(id_usuario, isbn)

    elif opcion == "7":
        print("Buscar por: 1. Título, 2. Autor, 3. Categoría")
        sub_opcion = input("Seleccione una opción: ")
        if sub_opcion == "1":
            titulo = input("Título: ")
            biblioteca.buscar_libro(titulo_autor=(titulo, ""))
        elif sub_opcion == "2":
            autor = input("Autor: ")
            biblioteca.buscar_libro(titulo_autor=("", autor))
        elif sub_opcion == "3":
            categoria = input("Categoría: ")
            biblioteca.buscar_libro(categoria=categoria)

    elif opcion == "8":
        id_usuario = input("ID del usuario: ")
        biblioteca.listar_libros_prestados(id_usuario)

    elif opcion == "9":
        print("Saliendo del sistema...")
        break

    else:
        print("Opción no válida. Intente de nuevo.")