from carrito import Carrito
from producto import Producto
from tienda import Tienda

def menu():
    tienda = Tienda("Tienda de Ropas")
    
    # Add productos a la tienda
    tienda.add_producto(Camisa("Camisa Amarilla", 29.99, "S", "Lino", True))
    tienda.add_producto(Pantalon("Jeans Azul", 59.12, "M", "Denim", "champion"))    
    
    carrito = Carrito()
    
    while True:
        print("\n--- Menu de Compras ---")
        print("1. Ver productos")
        print("2. Add producto al carrito")
        print("3. Ver carrito")
        print("4. Pagar y salir")
        opcion = input("Selecciona una opcion:")
        
        if opcion == "1":
            
        elif opcion == "2":
            
        elif opcion == "3":
            
        else opcion == "4":
        
        
        