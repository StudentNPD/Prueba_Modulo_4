from error import LargoExcedidoException, SubTipoInvalidoException # agregado
from anuncio import Display, Video, Social # agregado


class Campana:
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
        if len(valor) <= 250: # LARGO_NOMBRE_ANUNCIO: No lo toma 
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
        tipo_anuncio = input("Ingrese el tipo de anuncio que desea crear ('Video', 'Display' o 'Social'):\n").strip().upper
        while tipo_anuncio not in  ["V", "D", "S"]:
        #if tipo_anuncio not in  ["V", "D", "S"]: # No es necesario que sea un ciclo
            tipo_anuncio = input("Ingrese una de las opciones válidas('Video', 'Display' o 'Social'):\n")
         #   raise SubTipoInvalidoException("Ingrese en mayuscula solo la primera letra de la opción")

        url_archivo = input("Ingrese la url del archivo:\n")
        url_click = input("Ingrese la url del click:\n")
        sub_tipo = input("Ingrese el subtipo del anuncio:\n")

        if tipo_anuncio == "V":
            duracion = int(input("Ingrese la duración del video:\n"))
            nuevo_anuncio = Video(url_archivo, url_click, sub_tipo, duracion)
        elif tipo_anuncio == "D":
            ancho = int(input("Ingrese el ancho del anuncio:\n"))
            alto = int(input("Ingrese el alto del archivo:\n"))
            nuevo_anuncio = Display(ancho, alto, url_archivo, url_click, sub_tipo)
        else:
            ancho = int(input("Ingrese el ancho del anuncio:\n"))
            alto = int(input("Ingrese el alto del archivo:\n"))
            nuevo_anuncio = Social(ancho, alto, url_archivo, url_click, sub_tipo)

        self.anuncios.append(nuevo_anuncio)
        return nuevo_anuncio

    def __str__(self) -> str:
        num_videos = 0
        num_display = 0
        num_social = 0
        
        for anuncio in self.anuncios:
            if anuncio.__class__.__name__ == "V":
                num_videos += 1
            elif anuncio.__class__.__name__ == "D":
                num_display += 1
            else:
                num_social += 1
        
        
        desc=f"Nombre de la campaña: {self.nombre}"
        desc=desc + f"Anuncios: {num_videos} Video, {num_display} Display, {num_social} Social"
                
        return desc

    def __str__(self) -> str:
        num_videos = 0
        num_display = 0
        num_social = 0
        
        for anuncio in self.anuncios:
            if anuncio.__class__.__name__ == "V":
                num_videos += 1
            elif anuncio.__class__.__name__ == "D":
                num_display += 1
            else:
                num_social += 1
        
        
        desc=f"Nombre de la campaña: {self.nombre}"
        desc=desc + f"Anuncios: {num_videos} Video, {num_display} Display, {num_social} Social"
                
        return desc
