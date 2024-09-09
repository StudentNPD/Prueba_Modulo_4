# Prueba Módulo 4

## Descripción del Proyecto

Este proyecto implementa una API para la gestión de campañas publicitarias, diseñada para ser consumida por diferentes interfaces de usuario, incluyendo aplicaciones web de escritorio, aplicaciones móviles y sistemas de terceros. La API está desarrollada en Python y forma parte de un desarrollo incremental con entregas parciales cada dos semanas.

## Estructura del Proyecto

El proyecto está estructurado en varios componentes clave:

1. **Clase Anuncio**: Clase base para los diferentes tipos de anuncios.
2. **Clases Video, Display, Social**: Clases derivadas de Anuncio para tipos específicos de anuncios.
3. **Clase Campana**: Gestiona una campaña publicitaria y sus anuncios asociados.
4. **Manejo de Errores**: Incluye excepciones personalizadas para manejar errores específicos.
5. **Interfaz de Usuario**: Un menú de consola para interactuar con el sistema (será reemplazado por la API en futuras iteraciones).

## Diagrama de Clases

A continuación se muestra el diagrama de clases del proyecto:

![Diagrama de Clases](/Diagrama_de_clases.png)

## Clases y Variables Importantes

### Clase Anuncio

- Atributos principales:
  - `_alto`: Altura del anuncio
  - `_ancho`: Ancho del anuncio
  - `_url_archivo`: URL del archivo del anuncio
  - `_url_click`: URL de destino al hacer clic
  - `_sub_tipo`: Subtipo específico del anuncio

### Clase Video (hereda de Anuncio)

- Atributo adicional:
  - `duracion`: Duración del video en segundos

### Clase Display (hereda de Anuncio)

- Sin atributos adicionales, utiliza los de la clase base

### Clase Social (hereda de Anuncio)

- Sin atributos adicionales, utiliza los de la clase base

### Clase Campana

- Atributos principales:

  - `_nombre`: Nombre de la campaña
  - `_fecha_inicio`: Fecha de inicio de la campaña
  - `_fecha_termino`: Fecha de término de la campaña
  - `_anuncios`: Lista de anuncios asociados a la campaña

- Constante importante:
  - `LARGO_NOMBRE_ANUNCIO`: Longitud máxima permitida para el nombre de la campaña (250 caracteres)

## Manejo de Errores

El proyecto implementa un sistema de manejo de errores personalizado:

### Clases de Excepciones

1. `Error`: Clase base para excepciones personalizadas.
2. `LargoExcedidoException`: Se lanza cuando se excede la longitud máxima permitida para el nombre de la campaña.
3. `SubTipoInvalidoException`: Se lanza cuando se intenta asignar un subtipo inválido a un anuncio.

### Registro de Errores

- Los errores se registran en un archivo de log (`archivolog.log`).
- Cada entrada de error incluye la fecha y hora del error, junto con una descripción del mismo.

## Funcionalidades Principales

- Creación y gestión de campañas publicitarias.
- Soporte para múltiples tipos de anuncios: Video, Display y Social.
- Modificación de propiedades de campañas y anuncios.
- Manejo de errores personalizado.
- Registro de errores en un archivo de log.

---

## Prerequisitos

- Sistema Operativos: Windows 10, 11, Linux, iOS
- Python 3.12

## Ejecución

**_Windows_**

`python demo.py`

**_Linux & iOS_**

`python3 demo.py`

---

## Colaboradores

- [Francisco Colomer](https://github.com/Cy5k0)
- [Francisco Monroy](https://github.com/fmonroy75)
- [Natalia Peña](https://github.com/StudentNPD)
