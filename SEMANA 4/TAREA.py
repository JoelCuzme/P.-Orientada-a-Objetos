
class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def __str__(self):
        return f"{self.nombre} - ${self.precio}"

class Canasta:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)
        print(f"Producto {producto.nombre} agregado a la canasta")

    def calcular_total(self):
        total = sum([producto.precio for producto in self.productos])
        return total

    def vaciar_carrito(self):
        self.productos = []
        print("Carrito vaciado.")

# Clase Tienda
class Tienda:
    def __init__(self):
        self.productos_disponibles = []

    def agregar_producto(self, producto):
        self.productos_disponibles.append(producto)

    def mostrar_productos(self):
        print("Productos disponibles:")
        for producto in self.productos_disponibles:
            print(f"- {producto}")

    def realizar_compra(self, Canasta):
        total = Canasta.calcular_total()
        if total > 0:
            print(f"Compra realizada. Total: ${total:.2f}")
            Canasta.vaciar_carrito()
        else:
            print("La Canasta está vacía. No se puede realizar la compra.")

Primero= Producto("Pelota", 100)
Segundo= Producto("Cama", 1000)
Tercero= Producto("Peluche", 80)

Tienda= Tienda()
Tienda.agregar_producto(Primero)
Tienda.agregar_producto(Segundo)
Tienda.agregar_producto(Tercero)

Canasta= Canasta()
Canasta.agregar_producto(Primero)
Canasta.agregar_producto(Segundo)

Tienda.realizar_compra(Canasta)






