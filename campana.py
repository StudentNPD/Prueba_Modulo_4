from error import LargoExcedidoException, SubTipoInvalidoException # agregado
from anuncio import Display, Video, Social # agregado

class Campana:
    """
    Clase que representa una campaña publicitaria.

    Esta clase gestiona una campaña que puede contener varios tipos de anuncios,
    incluyendo video, display y anuncios de redes sociales.

    Atributos:
        LARGO_NOMBRE_ANUNCIO (int): Longitud máxima permitida para el nombre de la campaña.
    """

    LARGO_NOMBRE_ANUNCIO = 250

    def __init__(self, nombre: str, fecha_inicio: str, fecha_termino: str) -> None:
        """
        Inicializa una instancia de Campana.

        Args:
            nombre (str): Nombre de la campaña.
            fecha_inicio (str): Fecha de inicio de la campaña.
            fecha_termino (str): Fecha de término de la campaña.
        """
        self.__nombre = nombre
        self.__fecha_inicio = fecha_inicio
        self.__fecha_termino = fecha_termino
        self.__anuncios = []

    @property
    def nombre(self):
        """str: Obtiene o establece el nombre de la campaña."""
        return self.__nombre

    @nombre.setter
    def nombre(self, valor: str):
        """
        Establece el nombre de la campaña.

        Args:
            valor (str): El nuevo nombre de la campaña.

        Raises:
            LargoExcedidoException: Si la longitud del nombre excede LARGO_NOMBRE_ANUNCIO.
        """
        if len(valor) <= self.LARGO_NOMBRE_ANUNCIO:
            self.__nombre = valor
        else:
            raise LargoExcedidoException("El número de caracteres excede lo permitido")

    @property
    def fecha_inicio(self):
        """str: Obtiene o establece la fecha de inicio de la campaña."""
        return self.__fecha_inicio

    @fecha_inicio.setter
    def fecha_inicio(self, valor: str):
        """Establece la fecha de inicio de la campaña."""
        self.__fecha_inicio = valor

    @property
    def fecha_termino(self):
        """str: Obtiene o establece la fecha de término de la campaña."""
        return self.__fecha_termino

    @fecha_termino.setter
    def fecha_termino(self, valor: str):
        """Establece la fecha de término de la campaña."""
        self.__fecha_termino = valor

    @property
    def anuncios(self):
        """list: Obtiene la lista de anuncios de la campaña."""
        return self.__anuncios

    def inicializar(self):
        """
        Inicializa la campaña con un anuncio de video por defecto.
        """
        self.__anuncios.append(Video("gato.url", "2gato.url", "instream", 23))

    def crear_anuncio(self):
        """
        Crea un nuevo anuncio y lo añade a la campaña.

        Este método interactúa con el usuario para obtener los detalles del anuncio.

        Returns:
            object: El nuevo anuncio creado (instancia de Video, Display o Social).
        """
        tipo_anuncio = input("Ingrese el tipo de anuncio que desea crear ('Video', 'Display' o 'Social (V , D o S)'):\n")
        tipo_anuncio = tipo_anuncio.upper()
        while tipo_anuncio not in ["V", "D", "S"]:
            tipo_anuncio = input("Ingrese una de las opciones válidas('Video', 'Display' o 'Social'):\n")

        url_archivo = input("Ingrese la url del archivo:\n")
        url_click = input("Ingrese la url del click:\n")

        if tipo_anuncio == "V":
            duracion = int(input("Ingrese la duración del video:\n"))
            sub_tipo = input("Ingrese el subtipo del anuncio: 'instream' o 'outstream'\n").lower()
            nuevo_anuncio = Video(url_archivo, url_click, sub_tipo, duracion)
        elif tipo_anuncio == "D":
            ancho = int(input("Ingrese el ancho del anuncio:\n"))
            alto = int(input("Ingrese el alto del archivo:\n"))
            sub_tipo = input("Ingrese el subtipo del anuncio: 'adicional' o 'native'\n").lower()
            nuevo_anuncio = Display(ancho, alto, url_archivo, url_click, sub_tipo)
        elif tipo_anuncio == "S":
            ancho = int(input("Ingrese el ancho del anuncio:\n"))
            alto = int(input("Ingrese el alto del archivo:\n"))
            sub_tipo = input("Ingrese el subtipo del anuncio: 'facebook' o 'linkedin'\n").lower()
            nuevo_anuncio = Social(ancho, alto, url_archivo, url_click, sub_tipo)

        self.anuncios.append(nuevo_anuncio)
        return nuevo_anuncio

    def __str__(self) -> str:
        """
        Genera una representación en cadena de la campaña.

        Returns:
            str: Una descripción de la campaña, incluyendo su nombre y el número de cada tipo de anuncio.
        """
        num_videos = 0
        num_display = 0
        num_social = 0

        for anuncio in self.anuncios:
            if anuncio.__class__.__name__ == "Video":
                num_videos += 1
            elif anuncio.__class__.__name__ == "Display":
                num_display += 1
            elif anuncio.__class__.__name__ == "Social":
                num_social += 1

        desc = f"Nombre de la campaña: {self.nombre}"
        desc = desc + f"\nAnuncios: {num_videos} Video, {num_display} Display, {num_social} Social"

        return desc 
