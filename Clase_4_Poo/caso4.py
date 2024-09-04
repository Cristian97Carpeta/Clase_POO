# Atributos
class Estudiante:
    def __init__(self, nombre, edad, grado):
        self.__nombre = nombre
        self.__edad = edad
        self.__grado = grado
        self.__asignaturas = {}

    # Getters y Setters

    def get_nombre(self):
        return self.__nombre

    def get_edad(self):
        return self.__edad

    def get_grado(self):
        return self.__grado

    def get_asignaturas(self):
        return self.__asignaturas

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_edad(self, edad):
        self.__edad = edad

    def set_grado(self, grado):
        self.__grado = grado

    def set_asignaturas(self, asignaturas):
        self.__asignaturas = asignaturas
        
    # Métodos

    def agregar_asignatura(self, asignatura, calificacion):
        self.__asignaturas[asignatura] = calificacion

    def calcular_promedio(self):
        if self.__asignaturas:
            total_calificaciones = sum(self.__asignaturas.values())
            return total_calificaciones / len(self.__asignaturas)
        return 0

    def obtener_detalles(self):
        promedio = self.calcular_promedio()
        return (f"Nombre: {self.get_nombre()}\n"
                f"Edad: {self.get_edad()}\n"
                f"Grado: {self.get_grado()}\n"
                f"Promedio de calificaciones: {promedio}\n")

# Creación del objeto Estudiante
estudiante = Estudiante(nombre="Cristian Carpeta", edad=27, grado=10)
estudiante.agregar_asignatura("sociales", 90)
estudiante.agregar_asignatura("ingles", 94)

# Imprimir detalles del estudiante
print(estudiante.obtener_detalles())


