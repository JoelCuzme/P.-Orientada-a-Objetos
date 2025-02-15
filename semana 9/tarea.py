class Producto:
    def __init__(self, codigo, nombre, cantidad, precio):
        self.codigo = codigo
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio



class Inventario:
    def __init__(self):
        self.productos = []

    # Añadir un nuevo producto
    def añadir_producto(self, producto):
        if any(i.codigo == producto.codigo for i in self.productos):
            print("Error: Ya existe un producto con ese ID.")
        else:
            self.productos.append(producto)
            print("Producto añadido con éxito.")

    # Eliminar un producto por ID
    def eliminar_producto(self, codigo):
        producto = self.buscar_por_codigo(codigo)
        if producto:
            self.productos.remove(producto)
            print("Producto eliminado con éxito.")
        else:
            print("Error: No se encontró un producto con ese ID.")

    # Actualizar cantidad o precio de un producto por ID
    def actualizar_producto(self, codigo, cantidad=None, precio=None):
        producto = self.buscar_por_codigo(codigo)
        if producto:
            if cantidad is not None:
                producto.cantidad = cantidad
            if precio is not None:
                producto.precio = precio
            print("Producto actualizado con éxito.")
        else:
            print("Error: No se encontró un producto con ese ID.")

    # Buscar producto(s) por nombre (puede haber nombres similares)
    def buscar_por_nombre(self, nombre):
        resultados = [p for p in self.productos if nombre.lower() in p.nombre.lower()]
        if resultados:
            for producto in resultados:
                print(producto)
        else:
            print("No se encontraron productos con ese nombre.")

    # Buscar producto por ID
    def buscar_por_codigo(self, codigo):
        for producto in self.productos:
            if producto.codigo == codigo:
                return producto
        return None

    # Mostrar todos los productos en el inventario
    def mostrar_inventario(self):
        if self.productos:
            for producto in self.productos:
                print(producto)
        else:
            print("El inventario está vacío.")

def mostrar_menu():
    print("Menú de Inventario ")
    print("1. Añadir producto")
    print("2. Eliminar producto")
    print("3. Actualizar producto")
    print("4. Buscar producto por nombre")
    print("5. Mostrar inventario")
    print("6. Salir")


def menu():
    inventario = Inventario()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":  # Añadir producto
            codigo = int(input("Ingrese el codigo del producto: "))
            nombre = input("Ingrese el nombre del producto: ")
            cantidad = int(input("Ingrese la cantidad: "))
            precio = float(input("Ingrese el precio: "))
            producto = Producto(codigo, nombre, cantidad, precio)
            inventario.añadir_producto(producto)

        elif opcion == "2":  # Eliminar producto
            codigo = int(input("Ingrese el codigo del producto a eliminar: "))
            inventario.eliminar_producto(codigo)

        elif opcion == "3":  # Actualizar producto
            codigo = int(input("Ingrese el codigo del producto a actualizar: "))
            cantidad = input("Ingrese la nueva cantidad (deje en blanco para no cambiar): ")
            precio = input("Ingrese el nuevo precio (deje en blanco para no cambiar): ")
            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None
            inventario.actualizar_producto(codigo, cantidad, precio)

        elif opcion == "4":  # Buscar producto por nombre
            nombre = input("Ingrese el nombre del producto a buscar: ")
            inventario.buscar_por_nombre(nombre)

        elif opcion == "5":  # Mostrar inventario
            inventario.mostrar_inventario()

        elif opcion == "6":  # Salir
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida. Intente de nuevo.")


menu()