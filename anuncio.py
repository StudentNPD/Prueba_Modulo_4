   

class Anuncio():
    
    def __init__(self, alto, ancho, url_archivo, url_clic, sub_tipo):
        self._alto = alto
        self._ancho = ancho
        self._url_archivo = url_archivo
        self._url_clic = url_clic
        self._sub_tipo = sub_tipo

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
