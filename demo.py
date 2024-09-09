from campana import Campana
from error import Error, LargoExcedidoException, SubTipoInvalidoException
from datetime import datetime

NOMBRE_LOG = "archivolog.log"


# crear campana
nueva_campana = Campana("Nueva Campana", "27/10/2024", "27/10/2024")


log = None
consultar = True

while consultar:

    try:
        print("Creemos una campaña! :D")
        # Ingrese el nombre de su campaña
        # Preguntar por el tipo de anuncio que desea agregar con sus especificaciones
        # Preguntar si desea agregar otro anuncio
        # Mostrar:
        #          Nombre de la campaña: Campaña 1
        #          Anuncios: 1 Video, 2 Display, 0 Social
        # Preguntar si desea cambiar nombre campaña, agregar anuncio o salir

        nuevo_nombre = input("Ingrese el nuevo nombre de la campana:\n")
        print(f"Se ha creado la campaña: {nuevo_nombre}")
        nueva_campana.nombre = nuevo_nombre
        nueva_campana.crear_anuncio()
        consultar = False
    except LargoExcedidoException as e:
        fecha_actual = datetime.now()
        # Imprime solo el mensaje
        print(e)
        with open(NOMBRE_LOG, "a") as log:
            log.write(f"{fecha_actual} : [ERROR]: {e}\n")

    except SubTipoInvalidoException as e:
        fecha_actual = datetime.now()
        # Imprime solo el mensaje
        print(e)
        with open(NOMBRE_LOG, "a") as log:
            log.write(f"{fecha_actual} - [ERROR]: {e}\n")

    except Error as e:
        fecha_actual = datetime.now()
        # Imprime solo el mensaje
        print(e)
        with open(NOMBRE_LOG, "a") as log:
            log.write(f"{fecha_actual} : [ERROR]: {e}\n")

    finally:
        if log is not None:
            log.close()
