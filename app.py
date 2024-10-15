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
            tienda.ver_productos()
        elif opcion == "2":
            tienda.ver_productos()
            try:
                seleccion = input(input("Seleccione el numero del producto para add al carrito:"))
                producto = tienda.select_producto(seleccion)
                carrito.add_producto(producto)
            except (ValueError, IndexError):
                print("Opcion no valida")
        elif opcion == "3":
            carrito.ver_carrito()
        elif opcion == "4":
            carrito.ver_carrito()
            carrito.calcular_total()
            print("Gracias por tu compra")
            break
        else:
            print("Opcion no valida. Por favor, selecciona de nuevo")        
            
if __name__ == "__main__":
    menu()
        