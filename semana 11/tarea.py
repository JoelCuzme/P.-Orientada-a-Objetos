class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio}"
class Inventario:
    def __init__(self):
        self.productos = {}  # Diccionario para almacenar productos por ID

    def añadir_producto(self, producto):
        if producto.id in self.productos:
            print("Error: El ID del producto ya existe.")
        else:
            self.productos[producto.id] = producto
            print("Producto añadido correctamente.")

    def eliminar_producto(self, id):
        if id in self.productos:
            del self.productos[id]
            print("Producto eliminado correctamente.")
        else:
            print("Error: Producto no encontrado.")

    def actualizar_producto(self, id, cantidad=None, precio=None):
        if id in self.productos:
            producto = self.productos[id]
            if cantidad is not None:
                producto.cantidad = cantidad
            if precio is not None:
                producto.precio = precio
            print("Producto actualizado correctamente.")
        else:
            print("Error: Producto no encontrado.")


    def guardar_a_archivo(self, archivo='inventario.txt'):
        with open(archivo, 'w') as f:
            for producto in self.productos.values():
                f.write(f"{producto.id},{producto.nombre},{producto.cantidad},{producto.precio}\n")
        print("Inventario guardado correctamente.")


    def mostrar_todos(self):
        if self.productos:
            for prod in self.productos.values():
                print(prod)
        else:
            print("El inventario está vacío.")

    def cargar_desde_archivo(self, archivo='inventario.txt'):
        try:
            with open(archivo, 'r') as f:
                for linea in f:
                    id, nombre, cantidad, precio = linea.strip().split(',')
                    producto = Producto(id, nombre, int(cantidad), float(precio))
                    self.productos[producto.id] = producto
            print("Inventario cargado correctamente.")
        except FileNotFoundError:
            print("Archivo no encontrado, empezando con un inventario vacío.")

def menu():
    inventario = Inventario()
    inventario.cargar_desde_archivo()  # Cargar el inventario al iniciar

    while True:
        print("\n--- Menú de Gestión de Inventario ---")
        print("1. Añadir Producto")
        print("2. Eliminar Producto")
        print("3. Mostrar   ")
        print("4. Actualizar Producto")
        print("5. Guardar y Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':  # Añadir producto
            id = input("ID del producto: ")
            nombre = input("Nombre del producto: ")
            cantidad = int(input("Cantidad del producto: "))
            precio = float(input("Precio del producto: "))
            inventario.añadir_producto(Producto(id, nombre, cantidad, precio))

        elif opcion == '2':  # Eliminar producto
            id = input("ID del producto a eliminar: ")
            inventario.eliminar_producto(id)

        elif opcion == '3':
            inventario.mostrar_todos()


        elif opcion == '4':  # Actualizar producto
            id = input("ID del producto a actualizar: ")
            cantidad = input("Nueva cantidad (dejar en blanco para no cambiar): ")
            precio = input("Nuevo precio (dejar en blanco para no cambiar): ")
            inventario.actualizar_producto(id, int(cantidad) if cantidad else None, float(precio) if precio else None)


        elif opcion == '5':  # Guardar y salir
            inventario.guardar_a_archivo()
            print("Saliendo del programa.")
            break

        else:  # Opción no válida
            print("Opción no válida. Intente de nuevo.")


menu()