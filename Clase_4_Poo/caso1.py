class UsuarioJuego:
    def __init__(self, nombre, clave):
        self.__nombre = nombre
        self.__clave = clave
        self.__puntaje = 0
        self.__nivel = 0

    # Getters y Setters

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_clave(self):
        return self.__clave

    def set_clave(self, clave):
        self.__clave = clave

    def get_puntaje(self):
        return self.__puntaje

    def set_puntaje(self, puntaje):
        self.__puntaje = puntaje

    def get_nivel(self):
        return self.__nivel

    def set_nivel(self, nivel):
        self.__nivel = nivel

    # Métodos

    def aumentar_puntaje(self):
        self.__puntaje += 1

    def aumentar_nivel(self):
        self.__nivel += 1

    def recibir_bonus(self, bonus):
        self.__puntaje += bonus

    def datos_jugador(self):
        return f"{self.__nombre} {self.__clave} {self.__puntaje} {self.__nivel}"


usuario = UsuarioJuego(nombre="CRISTIAN CARPETA", clave="109202930239")

# Aumentar puntaje

usuario.aumentar_puntaje()

# Aumentar nivel

usuario.aumentar_nivel()

# Recibir bonus

usuario.recibir_bonus(10)

# Imprimir datos del jugador

print(usuario.datos_jugador())
