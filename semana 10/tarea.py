class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio}"


class Inventario:
    def __init__(self, archivo='inventario.txt'):
        self.archivo=archivo
        self.productos = self.cargar_inventario()

    def cargar_inventario(self):
        try:
            with open(self.archivo, 'r') as f:
                productos = {}  # Diccionario para almacenar los productos
                for linea in f:
                    datos= linea.split(',')
                    id_producto, nombre, cantidad, precio = datos

                    id_producto = int(id_producto)
                    cantidad = int(cantidad)
                    precio = float(precio)
                    productos[id_producto] = Producto(id_producto, nombre, cantidad, precio)

                return productos
        except FileNotFoundError:
            print("Archivo no encontrado. Se creará uno nuevo.")
            return {}

    def guardar_inventario(self):
        with open(self.archivo, 'w') as f:
            f.writelines(f"{p.id},{p.nombre},{p.cantidad},{p.precio}\n" for p in self.productos.values())

    def añadir_producto(self, producto):
        self.productos[producto.id] = producto
        self.guardar_inventario()
        print(f"Producto '{producto.nombre}' añadido.")

    def actualizar_producto(self, id, cantidad=None, precio=None):
        if id in self.productos:
            p = self.productos[id]
            if cantidad: p.cantidad = cantidad
            if precio: p.precio = precio
            self.guardar_inventario()
            print(f"Producto '{p.nombre}' actualizado.")
        else:
            print("ID no encontrado.")

    def eliminar_producto(self, id):
        if id in self.productos:
            print(f"Producto '{self.productos.pop(id).nombre}' eliminado.")
            self.guardar_inventario()
        else:
            print("ID no encontrado.")

    def listar_productos(self):
        if not self.productos:
            print("Inventario vacío.")
        else:
            for p in self.productos.values():
                print(p)

def menu():
    inventario = Inventario()
    while True:
        opcion = input("\n1. Añadir\n2. Actualizar\n3. Eliminar\n4. Listar\n5. Salir\nOpción: ")
        if opcion == '1':
            inventario.añadir_producto(Producto(int(input("ID: ")), input("Nombre: "), int(input("Cantidad: ")), float(input("Precio: "))))
        elif opcion == '2':
            inventario.actualizar_producto(int(input("ID: ")), int(input("Nueva cantidad: ")) if input("¿Cambiar cantidad? (s/n): ") == 's' else None, float(input("Nuevo precio: ")) if input("¿Cambiar precio? (s/n): ") == 's' else None)
        elif opcion == '3':
            inventario.eliminar_producto(int(input("ID: ")))
        elif opcion == '4':
            inventario.listar_productos()
        elif opcion == '5':
            print("Saliendo...")
            break
        else:
            print("Opción no válida.")

menu()