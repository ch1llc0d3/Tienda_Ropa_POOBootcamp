class Tienda:
    def __init__(self, nombre):
        self._hombre = nombre
        self._productos = []
        
    def add_producto(self, producto):
        self._productos.append(producto)
        
    def ver_productos(self):
        for i, producto in enumerate(self._productos, 1):
            print(f"{1}. {producto.ver_info()}")
    
    def select_producto(self, indice):
        return self._productos[indice - 1]
    