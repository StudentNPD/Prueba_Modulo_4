class Campaña:


    def __init__(self, nombre: str, fecha_inicio: str, fecha_termino: str) -> None:
        self.__nombre = nombre
        self.__fecha_inicio = fecha_inicio
        self.__fecha_termino = fecha_termino
        self.__anuncios = []
        #self.anuncios_disponibles = ["Video", "Display", "Social"]

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor: str):
        if len(valor) <= 250:
            self.__nombre = valor
        else:
            raise LargoExcedidoException("El número de carácteres excede lo permitido")


    @property
    def fecha_inicio(self):
        return self.__fecha_inicio

    @fecha_inicio.setter
    def fecha_inicio(self, valor: str):
        self.__fecha_inicio = valor

    @property
    def fecha_termino(self):
        return self.__fecha_termino

    @fecha_termino.setter
    def fecha_termino(self, valor: str):
        self.__fecha_termino = valor

    @property
    def anuncios(self):
        return self.__anuncios


    def crear_anuncio(self):
        tipo_anuncio = input("Ingrese el tipo de anuncio que desea crear ('Video', 'Display' o 'Social'):\n")
    
