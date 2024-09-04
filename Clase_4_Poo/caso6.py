# Atributos
class Vehiculo:
    def __init__(self, marca, modelo, año, cantidad_combustible):
        self.__marca = marca
        self.__modelo = modelo
        self.__año = año
        self.__cantidad_combustible = cantidad_combustible

# Getters y Setters

    def get_marca(self):
        return self.__marca

    def get_modelo(self):
        return self.__modelo

    def get_año(self):
        return self.__año

    def get_cantidad_combustible(self):
        return self.__cantidad_combustible

    def set_marca(self, marca):
        self.__marca = marca

    def set_modelo(self, modelo):
        self.__modelo = modelo

    def set_año(self, año):
        self.__año = año

    def set_cantidad_combustible(self, cantidad_combustible):
        self.__cantidad_combustible = cantidad_combustible

    # Métodos

    def llenar_combustible(self, cantidad):
        self.__cantidad_combustible += cantidad

    
    def usar_combustible(self, cantidad):
        if self.__cantidad_combustible >= cantidad:
            self.__cantidad_combustible -= cantidad
            return True
        else:
            return False
        
    def obtener_detalles(self):
        return (f"Marca: {self.get_marca()}\n"
                f"Modelo: {self.get_modelo()}\n"
                f"Año: {self.get_año()}\n"
                f"Cantidad de Combustible: {self.get_cantidad_combustible()}")


vehiculo = Vehiculo(marca = "Ford", modelo = "Raptor", año = 2024, cantidad_combustible = 40)

# Llenar combustible

vehiculo.llenar_combustible(50)

# Usar combustible

if vehiculo.usar_combustible(50):
    print("Combustible usado correctamente.")
else:
    print("No hay suficiente combustible.")

# Imprimir detalles del vehículo

print(vehiculo.obtener_detalles())




