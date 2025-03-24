class Cliente:
    siguiente_id = 1000
    
    def __init__(self, nombre, email):
        self.id = Cliente.siguiente_id
        self.nombre = nombre
        self.email = self.validar_email(email)
        self.activo = True
        self.carrito_compras = []
        Cliente.siguiente_id += 1
    
    def __str__(self):
        return (
            f"🏷️ ID: {self.id}\n"
            f"👤 Nombre: {self.nombre}\n"
            f"📧 Email: {self.email}\n"
            f"🛒 Productos en carrito: {len(self.carrito_compras)}\n"
            f"🚦 Estado: {'🟢 Activo' if self.activo else '🔴 Inactivo'}"
        )
    
    @staticmethod
    def validar_email(email):
        if "@" not in email:
            raise ValueError("❌ ¡Email inválido! Debe contener @")
        return email
    
    def agregar_al_carrito(self, producto):
        if not producto:
            raise ValueError("❌ ¡El producto no puede estar vacío!")
        self.carrito_compras.append(producto)
        return f"✅ ¡{producto} agregado al carrito!"
    
    def realizar_compra(self):
        if not self.carrito_compras:
            raise Exception("❌ ¡No puedes comprar con el carrito vacío!")
        
        total = len(self.carrito_compras)
        self.carrito_compras = []
        return f"🎉 ¡Compra exitosa! {total} productos adquiridos."

class ClientePremium(Cliente):
    def __init__(self, nombre, email):
        super().__init__(nombre, email)
        self.descuento = 0.10
    
    def __str__(self):
        info_base = super().__str__()
        return (
            f"🌟 CLIENTE PREMIUM 🌟\n"
            f"{info_base}\n"
            f"🎁 Descuento: {self.descuento * 100}%"
        )