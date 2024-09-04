class Perro:
    def __init__(self, raza, ano_nacimiento, peso, nombre):
        self.__en_adopcion = False
        self.__raza = raza
        self.__ano_nacimiento = ano_nacimiento
        self.__peso = peso
        self.__tiene_chip = False
        self.__esta_lastimado = False
        self.__nombre = nombre

    # Getters y Setters
    def is_en_adopcion(self):
        return self.__en_adopcion

    def set_en_adopcion(self, en_adopcion):
        self.__en_adopcion = en_adopcion

    def get_raza(self):
        return self.__raza

    def set_raza(self, raza):
        self.__raza = raza

    def get_ano_nacimiento(self):
        return self.__ano_nacimiento

    def set_ano_nacimiento(self, ano_nacimiento):
        self.__ano_nacimiento = ano_nacimiento

    def get_peso(self):
        return self.__peso

    def set_peso(self, peso):
        self.__peso = peso

    def is_tiene_chip(self):
        return self.__tiene_chip

    def set_tiene_chip(self, tiene_chip):
        self.__tiene_chip = tiene_chip

    def is_esta_lastimado(self):
        return self.__esta_lastimado

    def set_esta_lastimado(self, esta_lastimado):
        self.__esta_lastimado = esta_lastimado

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def calcular_edad(self):
        from datetime import datetime
        return datetime.now().year - self.__ano_nacimiento

    def es_perro_perdible(self):
        return not self.__tiene_chip

    def enviar_adopcion(self):
        if not self.__esta_lastimado and self.__peso > 5.0:
            self.__en_adopcion = True
            return True
        return False

    def obtener_detalles(self):
        return (f"Nombre: {self.get_nombre()}\n"
                f"Raza: {self.get_raza()}\n"
                f"Año de Nacimiento: {self.get_ano_nacimiento()}\n"
                f"Peso: {self.get_peso()}\n"
                f"Tiene Chip: {self.is_tiene_chip()}\n"
                f"Está Lastimado: {self.is_esta_lastimado()}\n"
                f"En Adopción: {self.is_en_adopcion()}")


perro = Perro(raza="Pastor Alemán", ano_nacimiento=2024, peso=6.0, nombre="Comando")

# Imprimir detalles del perro

print(perro.obtener_detalles())

