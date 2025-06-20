def generar_factura(cliente, productos, delivery=1.5):
    print("\n" + "="*40)
    print("         🧾 BURGERSOFT - FACTURA")
    print("="*40)

    # Datos del cliente
    print(f"Nombre del cliente: {cliente['nombre']}")
    print(f"Dirección: {cliente['direccion']}")
    print(f"Teléfono: {cliente['telefono']}")
    print("-" * 40)

    # Productos seleccionados
    total_productos = 0
    print("Productos seleccionados:")
    for producto in productos:
        print(f"  - {producto['nombre']} .... ${producto['precio']:.2f}")
        total_productos += producto['precio']
    
    print("-" * 40)

    # Costo del delivery
    print(f"Costo de delivery:        ${delivery:.2f}")

    # Total
    total_pagar = total_productos + delivery
    print(f"TOTAL A PAGAR:            ${total_pagar:.2f}")
    print("-" * 40)

    # Tiempo estimado
    print("⏱ Tiempo estimado de entrega: 20–25 minutos")
    print("="*40 + "\n")


# Recolectar datos del cliente
cliente = {}
print("👤 Ingrese sus datos:")
cliente["nombre"] = input("Nombre: ")
cliente["direccion"] = input("Dirección: ")
cliente["telefono"] = input("Teléfono: ")

# Ingresar productos
productos = []
print("\n🛒 Ingrese productos al pedido (escriba 'fin' para terminar):")
while True:
    nombre_producto = input("Nombre del producto: ")
    if nombre_producto.lower() == "fin":
        break
    try:
        precio = float(input("Precio del producto: $"))
        productos.append({"nombre": nombre_producto, "precio": precio})
    except ValueError:
        print("⚠️ Precio inválido. Intente de nuevo.")

# Generar factura
if productos:
    generar_factura(cliente, productos)
else:
    print("No se ingresaron productos. No se puede generar la factura.")
