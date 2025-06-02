import os

### Variables globales
arr_products = []
option = ""

### Ejemplo de producto para pruebas
# product = {
#     "nombre": "Nombre del producto ejemplo",
#     "categoria": "Categoria del producto ejemplo",
#     "precio": 2     
# }
# arr_products.append(product)


### Inicio del programa
print("Bienvenido al sistema de gestión de productos")

while option != "5":
    # Menú principal
    option = input("#######################\n" \
    "Seleccione una opción:\n" \
    "1. Agregar un producto\n" \
    "2. Mostrar un producto\n" \
    "3. Buscar un producto\n" \
    "4. Eliminar un producto\n" \
    "5. Salir\n"
    "#######################\n")

    match option:
        case "1":
            print("Agregar un producto")
            # Validación de entrada para evitar errores
            continue_input = "s"
            while continue_input == "s":
                try:
                    productName = str(input("Ingrese el nombre del producto: "))
                    productCategory = str(input("Ingrese la categoria del producto: "))
                    productPrice = input("Ingrese el precio del producto (número entero): ")
                    
                    # Validación de campos vacíos
                    if productName == "":
                        raise ValueError("El nombre no puede estar vacío.")
                    if productCategory == "":
                        raise ValueError("La categoría no puede estar vacía.")
                    if not productPrice.isnumeric() :
                        raise ValueError("El precio debe ser un número entero positivo.")
                    else:
                        productPrice = int(productPrice)
                    
                    product = {
                        "nombre": productName,
                        "categoria": productCategory,
                        "precio": productPrice
                    }
                    arr_products.append(product)
                    continue_input = input("¿Desea agregar otro producto? (s/n): ").lower()
                except ValueError as e:
                    print(e, "Intente de nuevo. \n")
            os.system('cls||clear')
        case "2":
            print("Mostrar un producto")
            for product in arr_products:
                print(f" \
                    Producto {arr_products.index(product) + 1}: \n \
                    - Nombre: {product['nombre']}\n \
                    - Categoría: {product['categoria']}\n \
                    - Precio: {product['precio']} \n \
                    #######################\n"
                )
            if (arr_products == []):
                print("No hay productos para mostrar.")
            input("Presione Enter para continuar...")
            os.system('cls||clear')
        case "3":
            print("Buscar un producto")
            string_search = input("Ingrese el nombre del producto a buscar: ")
            for product in arr_products:
                if string_search.lower() in product['nombre'].lower():
                    print(f" \
                        Producto encontrado #{arr_products.index(product) + 1}: \n \
                        - Nombre: {product['nombre']}\n \
                        - Categoría: {product['categoria']}\n \
                        - Precio: {product['precio']} \n \
                        #######################\n"
                    )
                else:
                    print("Producto no encontrado.")
            input("Presione Enter para continuar...")
            os.system('cls||clear')
        case "4":
            print("Eliminar un producto")
            try:
                string_search = int(input("Ingrese el nro. del producto a eliminar (número): "))
                # for product in arr_products:
                if arr_products.index(product) == (string_search - 1):
                    print(f" \
                        Producto encontrado: \n \
                        - Nombre: {product['nombre']}\n \
                        - Categoría: {product['categoria']}\n \
                        - Precio: {product['precio']} \n \
                        #######################\n"
                    )
                    confirm = input("¿Está seguro de que desea eliminar este producto? (s/n): ").lower()
                    if confirm == 's':
                        # arr_products.pop(string_search - 1)
                        arr_products.remove(product)
                        print("Producto eliminado exitosamente.")
                else:
                    print("Producto no encontrado.")
            except:
                print("Ingreso inválido. Verifique el tipo de dato ingresado. Intente de nuevo. \n")
            input("Presione Enter para continuar...")
            os.system('cls||clear')
        case "5":
            print("Saliendo del sistema. ¡Hasta luego!")
            break
        case _:
            print("Opción no válida. Intente de nuevo.")