class Error(Exception):
    """
    Clase base para excepciones personalizadas en este módulo.

    Esta clase hereda de la clase Exception incorporada en Python y
    sirve como base para otras excepciones más específicas.
    """
    pass

class LargoExcedidoException(Error):
    """
    Excepción levantada cuando se excede la longitud máxima permitida.

    Esta excepción se utiliza típicamente cuando un campo o entrada
    supera el número máximo de caracteres permitidos.
    """
    pass

class SubTipoInvalidoException(Error):
    """
    Excepción levantada cuando se proporciona un subtipo inválido.

    Esta excepción se utiliza cuando se intenta asignar un subtipo
    que no está en la lista de subtipos válidos para un anuncio.
    """
    pass
