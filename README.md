# Curso de Scrapy
Scrapy es una de las herramientas de web scraping más poderosas, utilizando python podremos generar un script capaz de hacer scraping hacia los gobiernos 🐞

## Instalación
- Creamos una carpeta raíz del proyecto
- Inicializamos el repositorio con `git init` en git bash
- Generamos un virtual environment con `python -m venv venv`
- Generamos el archivo `.gitignore` y agregamos al directorio **venv/**
- Una vez terminada la generación de nuestro entorno lo inicializamos con `venv/scripts/activate`
- Instalamos los requerimientos del proyecto con `pip install autopep8 scrapy`
- **Opcional:** Generamos requirements.txt con `pip freeze > requirements.txt`
- Hacemos nuestro commit inicial con `git add .` y `git commit -m "message"`

## El framework asíncrono
Scrapy nos permite hacer **webscraping** y **webcrawiling**
Scrapy es un framework asíncrono, lo que nos permite generar requests de forma independiente de las anteriores
- Herramientas
-- Procesador Xpath interno
-- Interactive Shell interna
-- Exportación múltiple [JSON, CSV, etc]
-- Seguimiento de reglas robots.txt automática 🤖

## Comenzando

Una vez abierta la carpeta raíz del proyecto en VSCode con `code .` inicializamos un proyecto de Scrapy
- El código para ello es: `scrapy startproject <project_name>`
- Luego de esto nos pedirá cambiar de directorio a `cd <project_name>`
- Se generará una nueva carpeta, en la cual vamos a hacer un nuevo archivo **.py** dentro de `<project_name>/<project_name>/file.py`

Dentro de nuestro archivo haremos la importación de la librería con `import scrapy`, lógicamente no hablaremos de la construcción del archivo pero si sobre algunas especificaciones, Scrapy es orientado a objetos por lo que nuestro proyecto se generará basado en este paradigma.

La ejecución de un archivo se da a través de `scrapy crawl ClassName>name` (Refiriéndose a que el nombre a utilizar es el que está dentro de la clase y dentro de la variable name)

## Generadores e Iteradores
*Recordamos el uso de estos.*
- *Un Iterador* dentro de Python es un elemento que pueda ser iterado, tales como los string, list, etc. Python posee una forma sencilla de iterar entre estos elementos, el ciclo **for**, pero este no es más que _suggar syntax_ para facilitar la tarea original, el proceso sería el siguiente:
-- Python toma el elemento y lo convierte en un objeto iterable
-- Utiliza la función built-in `next()` para poder seleccionar el elemento inicial o siguiente de acuerdo a las peticiones del usuario.
-- Al llegar al final de la iteración arroja un error de tipo `StopIteration`
- Un Generador es una forma práctica que tiene Python de retornar un elemento en una función sin tener que terminar con esta, esto se logra al reemplazar el uso de **return** por **yield** y utilizando next() para la el paso al siguiente iterable. Python llega hasta la declaración `yield` y deja marcado el estado de la misma, una vez empezado nuevamente un ciclo y a través de next(), `yield` se encargará de devolver el valor correspondiente a la siguiente iteración, cosa que no ocurriría dentro de `return`, ya que este se toma este como punto final de la función.

## Scrapy shell
¡Nos va a permitir hacer consultas de XPath de manera mejorada y eficaz!
A través de esta shell interactiva podemos hacer request de páginas para obtener todo tipo de información útil a través de:
- `scrapy shell 'url'` para hacer la llamada inicial

Y luego, abierta la shell, múltiples funciones como:

-- `response.xpath('xpath-path').get() -/- .getall()` para obtener uno o múltiples elementos xpath
-- `request.encoding` para obtener el encoding dado por la request
-- `request.status`, para saber el estado de la llamada
-- `request.headers` para obtener los headers del sitio y su información
-- `request.body` para obtener el cuerpo de la llamada, osea el html

## Estructura de carpetas
Luego de creado nuestro directorio a través de `scrapy startproject <project_name>` nos encontraremos con varios archivos dentro de los directorios del proyecto, tales como:
- scrapy.cfg: Settings
- pipelines.py: Modificar desde la entrada en Spiders hasta su salida
- middlewares.py: Controlador de eventos durante la ejecución de la request
- settings.py: Archivo de configuraciones, tales como tiempos, nombres, cookies, headers y otras funciones

## Spiders 🕷
*Una clase de python en la que decidimos qué información queremos, cuál no y cómo guardarla*

`parse()`: Analiza un archivo (response) para extraer información valiosa del mismo

## Guardado como archivo
Para guardar un archivo con Scrapy se debe fijar el output desde la consola (Al menos por ahora) utilizando el flag -o y el nombre del output:
`scrapy crawl <file> -o <file_output>`