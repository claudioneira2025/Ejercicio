class Persona:
    def __init__(self, nombre, apellido, telefono):
        self.__nombre=nombre
        self.__apellido=apellido
        self.__telefono=telefono

    def getNombreCompleto(self):
        return f"{self.__nombre} {self.__apellido}"
