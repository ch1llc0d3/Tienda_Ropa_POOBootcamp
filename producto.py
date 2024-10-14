# Clase base Producto 
class Producto:
    def __init__(self nombre, precio):
        self._nombre = nombre
        self._precio = precio
        
    # Metodo para saber el precio 
    def ver_precio(self):
        return self._precio
    
    # Metodo para mosrar info del producto    
    def ver_info(self):
        return f"Producto: {self._nombre} - Precio: ${self._precio:.2f}"