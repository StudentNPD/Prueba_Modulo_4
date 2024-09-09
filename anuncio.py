from abc import abstractmethod
from error import SubTipoInvalidoException  # agregado


class Anuncio:
    """
    Clase base para diferentes tipos de anuncios.

    Esta clase proporciona una estructura común para varios formatos de anuncios,
    incluyendo video, display y anuncios de redes sociales.

    Atributos:
        _alto (int): Altura del anuncio.
        _ancho (int): Ancho del anuncio.
        _url_archivo (str): URL del archivo del anuncio.
        _url_click (str): URL de clic para el anuncio.
        _sub_tipo (str): Subtipo del anuncio.
    """

    def __init__(self, alto, ancho, url_archivo, url_clic, sub_tipo):
        """
        Inicializa un objeto Anuncio.

        Args:
            alto (int): Altura del anuncio. Debe ser positivo.
            ancho (int): Ancho del anuncio. Debe ser positivo.
            url_archivo (str): URL del archivo del anuncio.
            url_clic (str): URL de clic para el anuncio.
            sub_tipo (str): Subtipo del anuncio.
        """
        self.__alto = alto if alto > 0 else 1
        self.__ancho = ancho if ancho > 0 else 1
        self.__url_archivo = url_archivo
        self.__url_click = url_clic
        self.__sub_tipo = sub_tipo

    @property
    def ancho(self):
        """int: Obtiene o establece el ancho del anuncio."""
        return self.__ancho

    @ancho.setter
    def ancho(self, valor: int):
        """Establece el ancho del anuncio. Debe ser positivo."""
        self.__ancho = valor if valor > 0 else 1

    @property
    def alto(self) -> int:
        """int: Obtiene o establece la altura del anuncio."""
        return self.__alto

    @alto.setter
    def alto(self, valor: int):
        """Establece la altura del anuncio. Debe ser positiva."""
        self.__alto = valor if valor > 0 else 1

    @property
    def url_archivo(self):
        """str: Obtiene o establece la URL del archivo del anuncio."""
        return self.__url_archivo

    @url_archivo.setter
    def url_archivo(self, valor: str):
        """Establece la URL del archivo del anuncio."""
        self.__url_archivo = valor

    @property
    def url_click(self):
        """str: Obtiene o establece la URL de clic para el anuncio."""
        return self.__url_click

    @url_click.setter
    def url_click(self, valor: str):
        """Establece la URL de clic para el anuncio."""
        self.__url_click = valor

    @property
    def sub_tipo(self):
        """str: Obtiene o establece el subtipo del anuncio."""
        return self.__sub_tipo

    @abstractmethod
    def comprimir_anuncio(self):
        """
        Método abstracto para comprimir el anuncio.

        Este método debe ser implementado por las subclases.
        """
        pass

    @abstractmethod
    def redimensionar_anuncio(self):
        """
        Método abstracto para redimensionar el anuncio.

        Este método debe ser implementado por las subclases.
        """
        pass

    @sub_tipo.setter
    def sub_tipo(self, valor: str):
        """
        Establece el subtipo del anuncio.

        Args:
            valor (str): El nuevo valor del subtipo.

        Raises:
            SubTipoInvalidoException: Si el subtipo no es válido.
        """
        if valor in self.SUB_TIPOS:
            self.__sub_tipo = valor
        else:
            raise SubTipoInvalidoException("El formato del archivo no es válido")

    @classmethod
    def mostrar_formatos(cls):
        """
        Método de clase para mostrar todos los formatos de anuncios disponibles y sus subtipos.
        """
        for formatos in [Video, Display, Social]:
            print(f"FORMATO {formatos.FORMATO}:")
            print("-----------------")
            for subtipo in formatos.SUB_TIPOS:
                print(f" {subtipo}")
            print()


class Video(Anuncio):
    """
    Clase que representa anuncios de video.

    Esta clase hereda de Anuncio y añade funcionalidad específica
    para anuncios de video.

    Atributos:
        FORMATO (str): El tipo de formato, establecido como "Video".
        SUB_TIPOS (tuple): Subtipos válidos para anuncios de video.
        duracion (int): Duración del anuncio de video en segundos.
    """

    FORMATO = "Video"
    SUB_TIPOS = ("instream", "outstream")

    def __init__(self, url_archivo, url_clic, sub_tipo, duracion):
        """
        Inicializa un objeto Video.

        Args:
            url_archivo (str): URL del archivo de video.
            url_clic (str): URL de clic para el anuncio.
            sub_tipo (str): Subtipo del anuncio de video.
            duracion (int): Duración del video en segundos.

        Raises:
            SubTipoInvalidoException: Si el subtipo no es válido para Video.
        """
        if sub_tipo not in self.SUB_TIPOS:
            raise SubTipoInvalidoException(
                f"Subtipo {sub_tipo} no es válido para Video"
            )
        super().__init__(1, 1, url_archivo, url_clic, sub_tipo)
        self.duracion = duracion if duracion > 0 else 5

    @property
    def nombre(self):
        """str: Obtiene el subtipo del anuncio de video."""
        return self.__sub_tipo

    @property
    def mostrar_subtipos(self):
        """tuple: Obtiene los subtipos válidos para anuncios de video."""
        return self.SUB_TIPOS

    def comprimir_anuncio(self):
        """Método para comprimir el anuncio de video (no implementado)."""
        print("COMPRESIÓN DE ANUNCIOS DISPLAY NO IMPLEMENTADA AÚN")

    def redimensionar_anuncio(self):
        """Método para redimensionar el anuncio de video (no implementado)."""
        print("REDIMENSIONAMIENTO DE ANUNCIOS DISPLAY NO IMPLEMENTADO AÚN")


class Display(Anuncio):
    """
    Clase que representa anuncios de display.

    Esta clase hereda de Anuncio y añade funcionalidad específica
    para anuncios de display.

    Atributos:
        FORMATO (str): El tipo de formato, establecido como "Display".
        SUB_TIPOS (tuple): Subtipos válidos para anuncios de display.
    """

    FORMATO = "Display"
    SUB_TIPOS = ("adicional", "native")

    def __init__(self, ancho, alto, url_archivo, url_clic, sub_tipo):
        """
        Inicializa un objeto Display.

        Args:
            ancho (int): Ancho del anuncio de display.
            alto (int): Altura del anuncio de display.
            url_archivo (str): URL del archivo del anuncio de display.
            url_clic (str): URL de clic para el anuncio.
            sub_tipo (str): Subtipo del anuncio de display.

        Raises:
            SubTipoInvalidoException: Si el subtipo no es válido para Display.
        """
        if sub_tipo not in self.SUB_TIPOS:
            raise SubTipoInvalidoException(
                f"Subtipo {sub_tipo} no es valido para Display"
            )
        super().__init__(ancho, alto, url_archivo, url_clic, sub_tipo)

    def comprimir_anuncio(self):
        """Método para comprimir el anuncio de display (no implementado)."""
        print("COMPRESIÓN DE ANUNCIOS DISPLAY NO IMPLEMENTADA AÚN")

    def redimensionar_anuncio(self):
        """Método para redimensionar el anuncio de display (no implementado)."""
        print("REDIMENSIONAMIENTO DE ANUNCIOS DISPLAY NO IMPLEMENTADO AÚN")


class Social(Anuncio):
    """
    Clase que representa anuncios de redes sociales.

    Esta clase hereda de Anuncio y añade funcionalidad específica
    para anuncios de redes sociales.

    Atributos:
        FORMATO (str): El tipo de formato, establecido como "Social".
        SUB_TIPOS (tuple): Subtipos válidos para anuncios de redes sociales.
    """

    FORMATO = "Social"
    SUB_TIPOS = ("facebook", "linkedin")

    def __init__(self, ancho, alto, url_archivo, url_clic, sub_tipo):
        """
        Inicializa un objeto Social.

        Args:
            ancho (int): Ancho del anuncio de redes sociales.
            alto (int): Altura del anuncio de redes sociales.
            url_archivo (str): URL del archivo del anuncio de redes sociales.
            url_clic (str): URL de clic para el anuncio.
            sub_tipo (str): Subtipo del anuncio de redes sociales.

        Raises:
            SubTipoInvalidoException: Si el subtipo no es válido para Social.
        """
        if sub_tipo not in self.SUB_TIPOS:
            raise SubTipoInvalidoException(
                f"Subtipo {sub_tipo} no es válido para Social"
            )
        super().__init__(ancho, alto, url_archivo, url_clic, sub_tipo)

    def comprimir_anuncio(self):
        """Método para comprimir el anuncio de redes sociales (no implementado)."""
        print("COMPRESIÓN DE ANUNCIOS DE REDES SOCIALES NO IMPLEMENTADA AÚN")

    def redimensionar_anuncio(self):
        """Método para redimensionar el anuncio de redes sociales (no implementado)."""
        print("REDIMENSIONAMIENTO DE ANUNCIOS DE REDES SOCIALES NO IMPLEMENTADO AÚN")
