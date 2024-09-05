   

class Anuncio():
    
    def __init__(self, alto, ancho, url_archivo, url_clic, sub_tipo):
        self._alto = alto if alto > 0 else 1
        self._ancho = ancho if ancho > 0 else 1
        self._url_archivo = url_archivo
        self._url_clic = url_clic
        self._sub_tipo = sub_tipo


    @property
    def ancho(self):
        return self.__ancho

    @ancho.setter
    def ancho(self, valor: int):
        self.__ancho = valor if valor > 0 else 1

    @property
    def alto(self) -> int:
        return self.__alto

    @alto.setter
    def alto(self, valor: int):
        self.__alto = valor if valor > 0 else 1

    @property
    def url_archivo(self):
        return self.__url_archivo

    @url_archivo.setter
    def url_archivo(self, valor: str):
        self.__url_archivo = valor

    @property
    def url_click(self):
        return self.__url_click

    @url_click.setter
    def url_click(self, valor: str):
        self.__url_click = valor

    @property
    def sub_tipo(self):
        return self.__sub_tipo

    @sub_tipo.setter
    def sub_tipo(self, valor: str):
        if valor in self.SUB_TIPOS:
            self.__sub_tipo = valor
        else:
            raise SubTipoInvalidoException("El formato del archivo no es válido")



class Video(Anuncio):
    
    FORMATO = "Video"
    SUB_TIPOS = ("instream", "outstream")

    def __init__(self, url_archivo, url_clic, sub_tipo, duracion):
            self.duracion = duracion

class Display(Anuncio):
    FORMATO = "Display"
    SUB_TIPOS = ("tradicional", "native")

class Social(Anuncio):
    FORMATO = "Social"
    SUB_TIPOS = ("facebook", "linkedin")
