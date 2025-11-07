# Biblioteca_Grp
https://github.com/brightzothen/Biblioteca_Grp.git

mi branca inicial, fue arnau peto y esta rota, la aplicacion final esta en la branca pepito

Mi contribucion general fue convertir la aplicacion de proyecto del Alex entera a Clases, apartir de este hecho

hemos comenzado los retoque.

Archivo menu.py

===========

Cargo todas las clases del archivo metodo en el propio archivo.

En este archivo hay una Clase ·GestorBiblioteca" que gestiona la biblioteca

Cargara la impresion de pantalla del menu ubicada en la clase utiles si no es de 1 a 9 no entrara

opcion 1: agregar_libro()

    la funcion original de alex

opcion 2: eliminar_libro()

    la funcion original de alex

opcion 3: modificar_libro()

    la funcion original de alex

opcion 4: buscar_libro()

    la funcion original de alex

opcion 5: agregar_user()

- Se entran cada dato, si el dato nombre introducido no es una cadena alfanumerica, no entra a pedir
  el email. Pide el email, y llama a la funcion validar_email de la clase validate, encontrada en chat GPT al pedirle, una funcion de validar email basada en javascript. Si es valido el email pide el id del usuario, si la
  posicion del id de ese nombre no lo encuentra , se llama a una funcion de añadir usario dentro de la clase usuario

opcion 6: modificar_usuario()

- Se entran el dato nombre introducido no es una cadena alfanumerica no sigue dando un error, si sigue pide el id si no lo encuentra no sigue, y si fuera que si pide la funcion en la clase usuarios de modificacion de usuarios, si devuelve un valor verdadero actualiza los cambios en el archivo ussarios
- Funcion modificar_usuario de la clase Usuarios:

  - Pide el nombre nuevo y comprueba si es una cadena alfanumerica, pide el nuevo email y lo valida, y si es correcto pide el nuevo id , si es correcto en cada validacion ira sumando +1 a cant_m, si es 3 añadira el usuario si no no.

opcion 7: hacer_devolucion()

- Se valida el dato nombre y si es correcto se hace la funcion de modificar usuario en la clase usuarios, y de la guardar_users en la misma clase.

opcion 8: hacer_prestamo()

- mismo desarrollo que hacer devolucion, con funcion hacer_prestamo en la clase usuarios.

opcion 9: salida del programa con actualizacion de la tabla libros

Archivo metodo.py

============

- Clase GArchivo_Uusario: carga el archivo usuarios.json
- Clase GestorArchivo: carga el archivo libros.json
- Clase Libro: inicializacion del objeto clase Libro
- Clase Usuario: inicializacion del objeto clase Usuario
- Clase Usuarios:
  - Cargamos las otras clses necesarias para usar las funciones en esta clase.
  - Guardar_usuarios: actualizar la tabla auxiliar con los datos del diccionario como si fuera una tabla objeto.
  - las funciones de prestamo y devolucion estan hechas en parte por el chat
