# Biblioteca_Grp
Archivo README de la versión de Álex.

Con los minutos que quedaron del martes, tras la creación del grupo, propuse a Arnau utilizar el código que tenía para el proyecto
del gestor de una biblioteca personal (PAC anterior) como punto de inicio para el desarrollo de este nuevo proyecto.
Arnau aceptó la propuesta.
Creamos en mi GitHub el repositorio con las 3 ramas: main, alex y arnau.

Al inicio de la clase el miércoles, Arnau trajó el código base (del gestor de la Biblioteca Personal) refactorizado con las clases añadidas.

El código funciona, pero no tengo ningún control sobre las clases creadas. Después de ver los atributos asignados por Arnau, acepto
la definición de las clases hechas por él. De otro modo tendríamos que empezar de 0.

A partir de este momento trabajamos con el código modificado por ChatGPT que trae Arnau.
El nuevo proyecto ha visto reducido los 3 módulos del proyecto base original a 2, metodos.py y menu.py

Trabajamos en la clase Usuario y en los métodos de dicha clase: agregar_usuario y modificar_usuario.
Trabajamos en conjunto. Al estar mezcladas las clases en dos únicos módulos, se hace difícil trabajar por separado.
Intentamos hacer un merge. Hay tantos conflictos que sólo podemos resolverlos manualmente.
Creamos la branch "prueba" para trabajar sin machacar partes que funcionan.

Acabamos el miércoles repartiéndonos el trabajo que queda: Arnau se encargará de las devoluciones de libros y Álex de los préstamos.

El jueves empezamos trabajando cada uno en nuestras ramas, pero después de crear "prueba", trabajo mayormente en "prueba".

Después del jueves decidimos trabajar con dos versiones distintas del proyecto.
La solución de Arnau pasa por promptear a ChatGPT los errores, y ChatGPT devuelve código que modifica todos los archivos.

No puedo trabajar (Álex) en un único código si las clases cambian cada vez que surge un error de ejecución.

Al principio del viernes codifico mi parte de préstamos tal y como habíamos acordado.
Arnau trae codificada (con cambios en el resto del código) ambas partes, la suya (devoluciones) y la mía (préstamos).
No quiero conflictos.
Decido acabar el código entero con mi versión.
El viernes trabajo por entero en la rama "prueba"

Para evitar conflictos en el repositorio o en la distinción de versiones, cambio de nombre mis archivos:
menu.py >> biblioteca.py (módulo principal, contiene las clases: GestorArchivos, GestorBiblioteca)
metodos.py >> utils.py (módulo que contiene las clases Libro, Biblioteca, Usuario, Usuarios)

También cambio los archivos de guardado de datos:
libros.json >> biblioteca.json
usuarios.json >> usuaris.json

Pusheado el trabajo hecho en la rama "prueba" a GitHub y de GitHub movido a la rama "alex" 

Commits:
========
Algunos commits los comentó Arnau. De nuevo no quise entrar en conflicto sobre el uso de mi ordenador local y dejé que los enviara él.
Estoy en contra de enviar commits comentados como "retocar" o "retocar2" o "grabar" pero no vengo a discutir ni a pelearme al centro.

Uso de la IA generativa:
========================

(Álex) no uso ni Copilot ni ChatGPT ni ninguna otra. A veces recurro al Gemini del buscador de Google, pero no para generar código, sino para resolver dudas 
cómo pasar parámetros o cómo llamar ciertas funciones.

No obstante la aplicación contiene parte de código generado por IA generativa ya que Arnau pasó el proyecto de la Biblioteca Personal por el Chat GPT.
Desconozco los prompts utilizados.

Módulos usados de Python:
=========================
Personalmente uso el módulo os y el Path de Python.

URL del repositorio de GitHub:
==============================
https://github.com/brightzothen/Biblioteca_Grp.git

