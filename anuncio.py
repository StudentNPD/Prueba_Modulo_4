from abc import ABC, abstractmethod
from error import SubTipoInvalidoException #agregado

class Anuncio:

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

    @abstractmethod
    def comprimir_anuncio(self):
        pass

    @abstractmethod
    def redimensionar_anuncio(self):
        pass

    @sub_tipo.setter
    def sub_tipo(self, valor: str):
        if valor in self.SUB_TIPOS:
            self.__sub_tipo = valor
        else:
            raise SubTipoInvalidoException("El formato del archivo no es válido")

    def mostrar_formatos():
        for formatos in [Video, Display, Social]:
            print(f"FORMATO {formatos.FORMATO}:")
            print("-----------------")
            for subtipo in formatos.SUB_TIPOS:
                print(f" {subtipo}")
            print()


class Video(Anuncio):

    FORMATO = "Video"
    SUB_TIPOS = ("instream", "outstream")

    def __init__(self, url_archivo, url_clic, sub_tipo, duracion):
        if sub_tipo not in self.SUB_TIPOS:
            raise SubTipoInvalidoError(f"Subtipo {sub_tipo} no es válido para Video")
        super().__init__(1, 1, url_archivo, url_clic, sub_tipo)
        self.duracion = duracion

    def comprimir_anuncio():
        print("COMPRESIÓN DE ANUNCIOS DISPLAY NO IMPLEMENTADA AÚN")

    def redimensionar_anuncio():
        print("REDIMENSIONAMIENTO DE ANUNCIOS DISPLAY NO IMPLEMENTADO AÚN")


class Display(Anuncio):
    FORMATO = "Display"
    SUB_TIPOS = (" adicional", "native")

    def __init__(self, ancho, alto, url_archivo, url_clic, sub_tipo):
        if sub_tipo not in self.SUB_TIPOS:
            raise SubTipoInvalidoError(f"Subtipo {sub_tipo} no es valido para Display")
        super().__init__(ancho, alto, url_archivo, url_clic, sub_tipo)

    def comprimir_anuncio():
        print("COMPRESIÓN DE ANUNCIOS DISPLAY NO IMPLEMENTADA AÚN")

    def redimensionar_anuncio():
        print("REDIMENSIONAMIENTO DE ANUNCIOS DISPLAY NO IMPLEMENTADO AÚN")


class Social(Anuncio):
    FORMATO = "Social"
    SUB_TIPOS = ("facebook", "linkedin")

    def __init__(self, ancho, alto, url_archivo, url_clic, sub_tipo):
        if sub_tipo not in self.SUB_TIPOS:
            raise SubTipoInvalidoError(f"Subtipo {sub_tipo} no es válido para Social")
        super().__init__(ancho, alto, url_archivo, url_clic, sub_tipo)

    def comprimir_anuncio():
        print("COMPRESIÓN DE ANUNCIOS DE REDES SOCIALES NO IMPLEMENTADA AÚN")

    def redimensionar_anuncio():
        print("REDIMENSIONAMIENTO DE ANUNCIOS DE REDES SOCIALES NO IMPLEMENTADO AÚN")
