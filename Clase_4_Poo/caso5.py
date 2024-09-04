# Atributos
class Producto:
    def __init__(self, nombre, codigo, precio, cantidad):
        self.__nombre = nombre
        self.__codigo = codigo
        self.__precio = precio
        self.__cantidad = cantidad

# Getters y Setters

    def get_nombre(self):
        return self.__nombre

    def get_codigo(self):
        return self.__codigo

    def get_precio(self):
        return self.__precio

    def get_cantidad(self):
        return self.__cantidad

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_codigo(self, codigo):
        self.__codigo = codigo

    def set_precio(self, precio):
        self.__precio = precio

    def set_cantidad(self, cantidad):
        self.__cantidad = cantidad

# Métodos

    def actualizar_precio(self):
        return self.__precio * self.__cantidad
    
    def actualizar_cantidad(self, nueva_cantidad):
        self.__cantidad = nueva_cantidad


    def obtener_detalles(self):
        total_compra = self.actualizar_precio()
        return (f"Nombre: {self.get_nombre()}\n"
                f"codigo: {self.get_codigo()}\n"
                f"precio: {self.get_precio()}\n"
                f"EL TOTAL DE SU COMPRA ES: {total_compra}")
    
# creacion del objeto Compra

producto = Producto (nombre = "Celular", codigo = 12345, precio = 1.200, cantidad = 2)

# Actualizar cantidad

producto.actualizar_cantidad(2)

# Imprimir detalles de compra

print(producto.obtener_detalles())
