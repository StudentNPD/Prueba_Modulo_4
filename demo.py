# from campana import Campana
# from error import Error, LargoExcedidoException, SubTipoInvalidoException
# from datetime import datetime

# NOMBRE_LOG = "archivolog.log"


# # crear campana
# nueva_campana = Campana("Nueva Campana", "27/10/2024", "27/10/2024")


# log = None
# consultar = True

# while consultar:

#     try:
#         print("Creemos una campaña! :D")
#         # Ingrese el nombre de su campaña
#         # Preguntar por el tipo de anuncio que desea agregar con sus especificaciones
#         # Preguntar si desea agregar otro anuncio
#         # Mostrar:
#         #          Nombre de la campaña: Campaña 1
#         #          Anuncios: 1 Video, 2 Display, 0 Social
#         # Preguntar si desea cambiar nombre campaña, agregar anuncio o salir

#         nuevo_nombre = input("Ingrese el nuevo nombre de la campana:\n")
#         print(f"Se ha creado la campaña: {nuevo_nombre}")
#         nueva_campana.nombre = nuevo_nombre
#         nueva_campana.crear_anuncio()
#         # consultar = False
#         consultar = input("¿Desea agregar otro anuncio? (s/n)\n").lower() == "s"
#         if not consultar:
#             print(nueva_campana)

#     except LargoExcedidoException as e:
#         fecha_actual = datetime.now()
#         # Imprime solo el mensaje
#         print(e)
#         with open(NOMBRE_LOG, "a") as log:
#             log.write(f"{fecha_actual} : [ERROR]: {e}\n")

#     except SubTipoInvalidoException as e:
#         fecha_actual = datetime.now()
#         # Imprime solo el mensaje
#         print(e)
#         with open(NOMBRE_LOG, "a") as log:
#             log.write(f"{fecha_actual} - [ERROR]: {e}\n")

#     except Error as e:
#         fecha_actual = datetime.now()
#         # Imprime solo el mensaje
#         print(e)
#         with open(NOMBRE_LOG, "a") as log:
#             log.write(f"{fecha_actual} : [ERROR]: {e}\n")

#     finally:
#         if log is not None:
#             log.close()

from campana import Campana
from error import LargoExcedidoException, SubTipoInvalidoException
from datetime import datetime

NOMBRE_LOG = "archivolog.log"

nueva_campana = None
consultar = True

while consultar:
    try:
        if nueva_campana is None:
            nombre_campana = input("Ingrese el nombre de la nueva campaña: ")
            fecha_inicio = input("Ingrese la fecha de inicio (dd/mm/aaaa): ")
            fecha_fin = input("Ingrese la fecha de término (dd/mm/aaaa): ")
            nueva_campana = Campana(nombre_campana, fecha_inicio, fecha_fin)
            print(f"Se ha creado la campaña: {nueva_campana.nombre}")

        nueva_campana.crear_anuncio()

        agregar_otro = input("¿Desea agregar otro anuncio? (s/n) ")
        consultar = agregar_otro.lower() == "s"

        if not consultar:
            print(nueva_campana)
            break

    except LargoExcedidoException as e:
        fecha_actual = datetime.now()
        print(e)
        with open(NOMBRE_LOG, "a") as f:
            f.write(f"{fecha_actual} : [ERROR]: {e}\n")

    except SubTipoInvalidoException as e:
        fecha_actual = datetime.now()
        print(e)
        with open(NOMBRE_LOG, "a") as f:
            f.write(f"{fecha_actual} - [ERROR]: {e}\n")
