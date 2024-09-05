from campaña import Campaña
from error import Error, LargoExcedidoError, SubTipoInvalidoError
from datetime import datetime

NOMBRE_LOG="archivolog.log"

#crear campaña
nueva_campaña = Campaña("Nueva Campaña", "27/10/2024", "27/10/2024")


log = None

try:
    #modificar campaña
    nuevo_nombre = input("Ingrese el nuevo nombre de la campaña:\n")
    nueva_campaña.nombre = nuevo_nombre

except LargoExcedidoException as e:
    fecha_actual = datetime.now()
    with open(NOMBRE_LOG, 'a') as log:
        log.write(f'{fecha_actual} : [ERROR]: {e}\n')

except SubTipoInvalidoException as e:
    fecha_actual = datetime.now()
    with open(NOMBRE_LOG, 'a') as log:
        log.write(f'{fecha_actual} - [ERROR]: {e}\n')

except Error as e:
    fecha_actual = datetime.now()
    with open(NOMBRE_LOG, 'a') as log:
        log.write(f'{fecha_actual} : [ERROR]: {e}\n')

finally:
    if log is not None:
        log.close()
