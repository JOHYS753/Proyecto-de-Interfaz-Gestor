##Gestor de Contenido Digital para Cursos
Este es un proyecto de aplicación de escritorio desarrollado en Python con PySide6 que funciona como un sistema de gestión de contenido (CMS) para cursos. Permite a los usuarios registrar, consultar, editar y eliminar diferentes tipos de materiales de estudio, como videos, documentos y enlaces web, utilizando una interfaz gráfica intuitiva y una base de datos SQL Server para la persistencia de los datos.

#🚀 Características Principales
Gestión CRUD completa:

Crear: Añadir nuevos contenidos (videos, documentos, enlaces web) a través de un formulario de registro.

Leer: Visualizar todos los contenidos en una tabla y buscarlos por título.

Actualizar: Seleccionar y editar la información de un contenido existente.

Eliminar: Borrar contenidos de la base de datos de forma segura con confirmación.

Interfaz de Pestañas: La aplicación se divide en dos pestañas principales para una mejor experiencia de usuario: "Registro / Edición" y "Consulta / Eliminación".

Formularios Dinámicos: El formulario de registro se adapta automáticamente para mostrar solo los campos relevantes según el tipo de contenido seleccionado (video, documento o enlace web).

Herencia y Polimorfismo: El código utiliza programación orientada a objetos para modelar los diferentes tipos de contenido, con una clase base Contenido y clases derivadas Video, Documento y EnlaceWeb.

Arquitectura en Capas: El proyecto está estructurado siguiendo una arquitectura de software que separa la presentación (UI), la lógica de negocio (servicio) y el acceso a datos (DAO).

#🛠️ Tecnologías Utilizadas
Lenguaje: Python

Interfaz Gráfica (GUI): PySide6

Base de Datos: Microsoft SQL Server

Conector de Base de Datos: pyodbc

#⚙️ Arquitectura del Proyecto
El proyecto sigue un diseño en capas para separar responsabilidades, facilitar el mantenimiento y mejorar la escalabilidad:

Capa de Presentación (UI):

main.py: Punto de entrada de la aplicación.

vtnGestor.py: Estructura de la interfaz gráfica (generada desde Qt Designer).

contenidoP.py: Controla la lógica de la interfaz, maneja los eventos y la interacción del usuario.

Capa de Dominio (Modelo):

contenido.py: Clase base que define los atributos comunes a todo el contenido.

video.py, documento.py, enlaceweb.py: Clases que heredan de Contenido y añaden atributos específicos.

Capa de Acceso a Datos (DAO):

contenidoDao.py: Gestiona todas las operaciones (CRUD) con la base de datos.

conexion.py: Administra la conexión con la base de datos SQL Server.

Base de Datos:

scripGestor.slq.sql: Script SQL para la creación de las tablas necesarias en la base de datos.

#📋 Requisitos Previos
Antes de ejecutar el proyecto, asegúrate de tener instalado lo siguiente:

Python 3.x

Microsoft SQL Server (cualquier edición, incluyendo Express).

Microsoft ODBC Driver for SQL Server.

#🚀 Instalación y Configuración
Sigue estos pasos para poner en marcha el proyecto:

#1. Instalar Dependencias de Python
Abre una terminal y ejecuta el siguiente comando para instalar las librerías necesarias:

Bash

pip install PySide6 pyodbc
#2. Configurar la Base de Datos
Abre SQL Server Management Studio (SSMS) o una herramienta similar.

Crea una nueva base de datos. En los archivos, se usa el nombre GestionContenidoDB.

Crea un usuario con permisos de lectura y escritura sobre esa base de datos (por ejemplo, usuario: Johana, pass: 0123456789).

Ejecuta el script scripGestor.slq.sql en tu base de datos para crear las tablas Contenidos, Videos, Documentos y EnlacesWeb.

#3. Actualizar la Cadena de Conexión
Abre el archivo src/datos/conexion.py y modifica las siguientes variables con tus propias credenciales de SQL Server:

Python

#class Conexion:
    _SERVIDOR = 'NOMBRE_DE_TU_SERVIDOR'  # Ej: 'DESKTOP-12345' o 'localhost'
    _BBDD = 'GestionContenidoDB'         # El nombre de tu base de datos
    _USUARIO = 'TuUsuarioSQL'            # El usuario que creaste
    _PASSWORD = 'TuContraseña'           # La contraseña del usuario
    # ...
#▶️ Ejecutar la Aplicación
Una vez configurado todo, ejecuta el archivo principal desde la raíz del proyecto para iniciar la aplicación:

Bash

python main.py
Aparecerá la ventana del "Gestor de Contenido Digital" y podrás empezar a utilizarla.
<img width="800" height="630" alt="image" src="https://github.com/user-attachments/assets/bf8995c4-107d-4063-8ef9-421e5937d4ff" />



