def carrito_compras():
    carrito = []

    while True:
        print("\n--- Carrito de Compras ---")
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Mostrar carrito")
        print("4. Calcular total")
        print("5. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            producto = input("Nombre del producto: ")
            precio = float(input("Precio: "))
            carrito.append((producto, precio))
        elif opcion == "2":
            producto = input("Producto a eliminar: ")
            carrito = [p for p in carrito if p[0] != producto]
        elif opcion == "3":
            print("Carrito:", carrito)
        elif opcion == "4":
            total = sum(precio for _, precio in carrito)
            print("Total:", total)
        elif opcion == "5":
            break
        else:
            print("Opción inválida.")


