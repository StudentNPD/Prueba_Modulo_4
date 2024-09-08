from campana import Campana
from error import Error, LargoExcedidoException, SubTipoInvalidoException
from datetime import datetime

NOMBRE_LOG="archivolog.log"


#crear campana
nueva_campana = Campana("Nueva Campana", "27/10/2024", "27/10/2024")


log = None
consultar = True

while consultar:

    try:
        #modificar campana
        print("Creemos una campaña! :D")
        
        nuevo_nombre = input("Ingrese el nuevo nombre de la campana:\n")
        print(nuevo_nombre)
        nueva_campana.nombre = nuevo_nombre
        nueva_campana.crear_anuncio()
        consultar = False
    except LargoExcedidoException as e:
        fecha_actual = datetime.now()
        # Imprime solo el mensaje
        print(e)
        with open(NOMBRE_LOG, 'a') as log:
            log.write(f'{fecha_actual} : [ERROR]: {e}\n')

    except SubTipoInvalidoException as e:
        fecha_actual = datetime.now()
        # Imprime solo el mensaje
        print(e)
        with open(NOMBRE_LOG, 'a') as log:
            log.write(f'{fecha_actual} - [ERROR]: {e}\n')

    except Error as e:
        fecha_actual = datetime.now()
        # Imprime solo el mensaje
        print(e)
        with open(NOMBRE_LOG, 'a') as log:
            log.write(f'{fecha_actual} : [ERROR]: {e}\n')

    finally:
        if log is not None:
            log.close()
