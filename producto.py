# Clase base Producto 
class Producto:
    def __init__(self, nombre, precio):
        self._nombre = nombre
        self._precio = precio
        
    # Metodo para saber el precio 
    def ver_precio(self):
        return self._precio
    
    # Metodo para mosrar info del producto    
    def ver_info(self):
        return f"{self._nombre} - Precio: ${self._precio}"
        pass
    
# Clase Ropa hereda de Producto
class Ropa(Producto):
    def __init__(self, nombre, precio, tamanho, tela):
        super().__init__(nombre, precio)
        self._tamanho = tamanho
        self._tela = tela
        
    # Metodo sobreescrito para mostrar la informacion especifica de ropa
    def ver_info(self):
        return f"{self._nombre} - Tamanho: {self._tamanho}, Tela: {self._tela}, Precio: ${self._precio}"
    
# Clases derivadas de ropa, como Camisa, Pantalon, Zapato

class Camisa(Ropa):
    def __init__(self, nombre, precio, tamanho, tela, manga):
        super().__init__(nombre, precio, tamanho, tela)
        self._manga = manga
        
    def ver_info(self):
        return f"Camisa {self._nombre} - Tamanho: {self._tamanho}, Tela: {self._tela}, Manga: {self._manga}, Precio: ${self._precio:.2f}"
    
 
class Pantalon(Ropa):
    def __init__(self, nombre, precio, tamanho, tela, estilo):
        super().__init__(nombre, precio, tamanho, tela)
        self._estilo = estilo
        
        def ver_info(self):
            return f"Pantalon {self._nombre} - Tamanho: {self._tamanho}, Tela: {self._tela}, Estilo: {self._estilo}, Precio: ${self._precio:.2f}"   