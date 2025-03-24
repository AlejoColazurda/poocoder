from clientes.cliente import Cliente, ClientePremium

def obtener_dato(mensaje, tipo=str, validador=None):
    while True:
        try:
            dato = input(mensaje).strip()
            if not dato:
                raise ValueError("❌ Este campo es obligatorio")
            if validador:
                dato = validador(dato)
            return dato
        except ValueError as e:
            print(f"⚠️ Error: {e}")

def validar_email(email):
    if "@" not in email:
        raise ValueError("❌ Debe contener @")
    return email

def seleccionar_cliente(clientes):
    if not clientes:
        print("\n⚠️ No hay clientes registrados.")
        return None
    
    print("\n📋 Clientes disponibles:")
    for cliente in clientes:
        print(f"  🆔 {cliente.id}: {cliente.nombre}")
    
    while True:
        try:
            cliente_id = int(obtener_dato("\n👉 Ingrese el ID del cliente: ", int))
            for cliente in clientes:
                if cliente.id == cliente_id:
                    return cliente
            print("❌ ID no encontrado. Intente de nuevo.")
        except ValueError:
            print("⚠️ ¡Debe ser un número!")

def menu_carrito(cliente):
    while True:
        print("\n" + "=" * 30)
        print(f"🛒 GESTIÓN DE CARRITO - {cliente.nombre}")
        print("=" * 30)
        print("1. Agregar producto al carrito")
        print("2. Ver carrito")
        print("3. Realizar compra")
        print("4. Volver al menú principal")
        
        try:
            opcion = int(obtener_dato("\n👉 Seleccione una opción: ", int))
            
            if opcion == 1:
                producto = obtener_dato("Nombre del producto: ")
                print(cliente.agregar_al_carrito(producto))
                
            elif opcion == 2:
                print("\n📦 Contenido del carrito:")
                if not cliente.carrito_compras:
                    print("  🛒 El carrito está vacío.")
                else:
                    for i, producto in enumerate(cliente.carrito_compras, 1):
                        print(f"  {i}. {producto}")
                        
            elif opcion == 3:
                print(f"\n{cliente.realizar_compra()}")
                
            elif opcion == 4:
                break
                
            else:
                print("❌ ¡Opción inválida!")
                
        except Exception as e:
            print(f"\n🚨 Error: {e}")

def menu_principal():
    clientes = []
    
    while True:
        print("\n" + "=" * 40)
        print("🛍️  TIENDA VIRTUAL - MENÚ PRINCIPAL")
        print("=" * 40)
        print("1. Crear cliente regular")
        print("2. Crear cliente premium")
        print("3. Ver todos los clientes")
        print("4. Gestionar carrito de un cliente")
        print("5. Salir")
        
        try:
            opcion = int(obtener_dato("\n👉 Seleccione una opción: ", int))
            
            if opcion == 1:
                nombre = obtener_dato("Nombre del cliente: ", validador=lambda x: x)
                email = obtener_dato("Email: ", validador=validar_email)
                nuevo_cliente = Cliente(nombre, email)
                clientes.append(nuevo_cliente)
                print(f"\n✅ Cliente creado:\n{nuevo_cliente}")
                
            elif opcion == 2:
                nombre = obtener_dato("Nombre del cliente premium: ", validador=lambda x: x)
                email = obtener_dato("Email: ", validador=validar_email)
                nuevo_premium = ClientePremium(nombre, email)
                clientes.append(nuevo_premium)
                print(f"\n💎 Cliente premium creado:\n{nuevo_premium}")
                
            elif opcion == 3:
                print("\n📋 LISTA DE CLIENTES:")
                for cliente in clientes:
                    print("\n" + "-" * 30)
                    print(cliente)
                    
            elif opcion == 4:
                cliente = seleccionar_cliente(clientes)
                if cliente:
                    menu_carrito(cliente)
                    
            elif opcion == 5:
                print("\n👋 ¡Hasta pronto!")
                break
                
            else:
                print("❌ ¡Opción inválida!")
                
        except Exception as e:
            print(f"\n🚨 Error inesperado: {e}")

if __name__ == "__main__":
    menu_principal()