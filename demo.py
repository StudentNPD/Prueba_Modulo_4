from campana import Campana
from error import Error, LargoExcedidoException, SubTipoInvalidoException, SubTipoInvalidoError
from datetime import datetime

NOMBRE_LOG = "archivolog.log"

def mostrar_menu():
    """
    Muestra el menú principal de opciones para la gestión de la campaña.
    """
    print("\nMenú de Gestión de Campaña:")
    print("1. Modificar Nombre")
    print("2. Modificar Subtipo")
    print("3. Mostrar Información de la Campaña")
    print("4. Salir")

def main():
    """
    Función principal que ejecuta el programa de gestión de campaña.

    Esta función crea una nueva campaña, la inicializa y entra en un bucle
    que permite al usuario interactuar con la campaña a través de un menú.
    Maneja las excepciones y registra los errores en un archivo de log.
    """
    nueva_campana = Campana("Nueva Campana", "27/10/2024", "27/10/2024")
    nueva_campana.inicializar()

    while True:
        try:
            print(f"\nCampaña actual: {nueva_campana.nombre}")
            print(f"Subtipo actual: {nueva_campana.anuncios[0].sub_tipo}")
            
            mostrar_menu()
            opcion = int(input("Seleccione una opción (1-4): "))
            
            if opcion == 1:
                nuevo_nombre = input("Ingrese el nuevo nombre de su campaña: ")
                nueva_campana.nombre = nuevo_nombre
                print(f"Nombre de la campaña actualizado a: {nueva_campana.nombre}")
            
            elif opcion == 2:
                mi_anuncio = nueva_campana.anuncios[0]
                print(f"Subtipo actual: {mi_anuncio.sub_tipo}")
                print("Subtipos disponibles:", mi_anuncio.mostrar_subtipos)
                mi_subtipo = input("Escoja un nuevo subtipo: ")
                mi_anuncio.sub_tipo = mi_subtipo
                print(f"Subtipo actualizado a: {mi_anuncio.sub_tipo}")
            
            elif opcion == 3:
                print(nueva_campana)
            
            elif opcion == 4:
                print("Gracias por usar el programa. ¡Hasta luego!")
                break
            
            else:
                print("Opción no válida. Por favor, intenta de nuevo.")

        except (LargoExcedidoException, SubTipoInvalidoException, SubTipoInvalidoError, Error) as e:
            fecha_actual = datetime.now()
            print(f"Error: {e}")
            with open(NOMBRE_LOG, 'a') as log:
                log.write(f'{fecha_actual} - [ERROR]: {e}\n')
        except ValueError:
            print("Por favor, ingrese un número válido.")

        input("\nPresione Enter para continuar...")

if __name__ == "__main__":
    main()
