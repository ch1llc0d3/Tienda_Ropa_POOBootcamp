class Carrito:
    def __init__(self):
        self._productos = []
    
    def add_producto(self, producto):
        self._productos.append(producto)
        print(f"{producto._nombre} ha sido add al carrito")
        
    def ver_carrito(self):
        if not self._productos:
            print("No hay productos")
        else:
            print("Productos en el carrito:")
            for producto in self._productos:
                print(producto.ver_info())
                
    def calcular_total(self):
        total = sum(producto.ver_precio() for producto in self._productos)
        print(f"EL total a pagar es: ${total}")
        return total 