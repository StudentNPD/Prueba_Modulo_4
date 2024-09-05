class Campaña:
    LARGO_NOMBRE_ANUNCIO=250

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
        if len(valor) <= LARGO_NOMBRE_ANUNCIO:
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


    def __str__(self) -> str:
        n_videos = 0
        n_display = 0
        n_social = 0
        
        for anuncio in self.listado_anuncios:
            if anuncio.__class__.__name__ == "Video":
                n_videos += 1
            elif anuncio.__class__.__name__ == "Display":
                n_display += 1
            else:
                n_social += 1
       
        return f"""
        Nombre de la campaña: {self.nombre}
        Anuncios: {n_videos} Video, {n_display} Display, {n_social} Social
        """
    

    def crear_anuncio(self):
        tipo_anuncio = input("Ingrese el tipo de anuncio que desea crear ('Video', 'Display' o 'Social'):\n")
        while tipo_anuncio not in  ["V", "D", "S"]:
            tipo_anuncio = input("Ingrese una de las opciones válidas('Video', 'Display' o 'Social'):\n")

