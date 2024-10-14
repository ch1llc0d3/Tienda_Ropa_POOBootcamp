## Sistema de Compras de Ropas con POO

# Descripción de la Tarea:

Los alumnos deberán desarrollar un programa de compra de ropas utilizando POO en Python. El sistema debe permitir al usuario seleccionar entre diferentes ítems de ropa (camisas, pantalones, zapatos, etc.) y procesar la compra. Para ello, implementarán clases que representen los productos, categorías y la tienda. Además, deberán demostrar el uso de los 4 pilares de POO, empleando herencia, encapsulación, polimorfismo y abstracción.

El proyecto será entregado a través de un repositorio en GitHub y evaluado en función de la correcta implementación de los conceptos de POO.
Objetivos de la Tarea:

    Aplicar los 4 pilares de la Programación Orientada a Objetos (POO): encapsulamiento, herencia, polimorfismo y abstracción.
    Practicar el uso de constructores, métodos, objetos y clases.
    Implementar un sistema básico de compra de ropa utilizando POO.
    Fomentar la reutilización de código y la escalabilidad en el desarrollo de software.
    Facilitar la comprensión de la relación entre clases padre e hijo, sobrescritura de métodos, y el uso de métodos para gestionar el flujo de un programa.

Requisitos de la Tarea:

    Repositorio en GitHub:
        Nombre del repositorio: Tienda_Ropa_POOBootcamp.
        Estructura clara del proyecto, siguiendo buenas prácticas (un archivo README.md explicando el funcionamiento y clases).

    Clases a Implementar:
        Producto: Clase base que representa un producto general.
        Ropa: Clase que hereda de Producto y añade características específicas de la ropa.
        Clases derivadas de Ropa: Clases específicas como Camisa, Pantalon, Zapato, que añaden atributos particulares (por ejemplo, talla, tipo de tela, etc.).
        Tienda: Clase que maneja los productos disponibles y las compras.

    Pilares de POO:
        Encapsulamiento: Deben encapsular los atributos de las clases, utilizando métodos getters y setters cuando sea necesario.
        Herencia: La clase Ropa debe heredar de Producto, y las clases específicas como Camisa o Pantalon deben heredar de Ropa.
        Polimorfismo: Implementar el método mostrar_info en cada clase hija, sobrescribiéndolo para mostrar información específica de cada producto.
        Abstracción: Ocultar los detalles internos del proceso de compra al usuario, centrándose en los aspectos esenciales (selección de productos, precios).

    Interacción con el Usuario:
        El programa debe permitir al usuario seleccionar uno o más productos de un menú.
        Se debe implementar una clase Carrito que almacene los productos seleccionados.
        Al finalizar la compra, se debe mostrar un resumen con los productos seleccionados y el total a pagar.

    Uso de Constructores y Métodos:
        Cada clase debe tener un constructor adecuado que inicialice sus atributos.
        Los métodos deben incluir la funcionalidad de agregar productos al carrito, calcular el precio total, y mostrar la información de la compra.

 
Guía de Corrección:

    Estructura del Repositorio (15%):
        Verificar que el proyecto tiene una estructura clara y bien documentada.
        Revisar que el archivo README.md explique el propósito del código y cómo ejecutarlo.

    Uso de POO (40%):
        Encapsulamiento: Asegurarse de que los atributos estén encapsulados utilizando _ para indicar privacidad.
        Herencia: Verificar que las clases Camisa y Pantalon heredan de Ropa, y que Ropa hereda de Producto.
        Polimorfismo: Comprobar que los métodos mostrar_info están sobrescritos en las clases derivadas.
        Abstracción: Revisar que el usuario no interactúe directamente con la lógica interna del sistema.

    Uso de Métodos y Constructores (20%):
        Confirmar que cada clase tiene un constructor correcto y que los métodos están bien implementados (por ejemplo, mostrar_info, obtener_precio).
        Revisar que el carrito de compras funcione correctamente.

    Interacción con el Usuario (15%):
        El programa debe permitir agregar productos al carrito y mostrar un resumen final.

    Correctitud del Código (10%):
        El programa debe ejecutarse sin errores y mostrar la información correcta de los productos y el total a pagar.

