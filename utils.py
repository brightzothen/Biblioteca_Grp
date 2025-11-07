


import os
import biblioteca as m
# =====================================================
# CLASE LIBRO
# =====================================================
class Libro:
    def __init__(self, titulo, autor, genero, isbn, stock):
        self.titulo = titulo.strip()
        self.autor = autor.strip()
        self.genero = genero.strip().lower()
        self.isbn = isbn
        self.stock = stock

    def __str__(self):
        return f"{self.titulo} de {self.autor} ({self.genero}) - ID: {self.isbn}, disponibles: {self.stock}"


# Clase usuario. Atributos:
            # entero : id_user
            # cadena : nombre
            # cadena : email
            # lista (cadenas) : contiene los títulos en préstamo de dicho usuario.
class Usuario:
    def __init__(self, id_user, nombre, email):
        self.idUser = id_user
        self.nombre = nombre.strip()
        self.email = email.strip()
        self.libros_en_prestamo = []

    def __str__(self):
        return f"{self.idUser} de {self.nombre} ({self.email})"

# Clase Usuarios creada por Arnau. Personalmente (Alex) habría usado una lista y no habría creado una clase para este objeto, ya que
# simplemente se trata de una lista (usuario)

class Usuarios:
    def __init__(self, lista_de_users=None):
        
            if lista_de_users is None:
                self.users = []
            else:
                self.users = lista_de_users
            self.ui = m.Utiles() #Antiguo utiles

   # # Añadir un usuario
    def agregar_user(self, user):
        if self.en_usuarios(user['nombre']) == -1:
            self.users.append(user)
            print(f'Usuario "{user["nombre"]}" agregado a usuarios.')
        else:
            print(f'Error: el usuario "{user["nombre"]}" ya existe en usuarios.')

    def en_usuarios ( self, nombre ):
        # el título es una cadena y la lista_de_libros es una lista de diccionarios con clave 'título' que habrá que recorrer.
        # la función devuelve -1 si el libro no está en la lista de libros o el índice con su posición el la lista si está presente.
        pos = -1
        if not self.users:
            return pos

        i = 0
        for us in self.users:
            if ( us['nombre'].strip().lower() == nombre ) :
                pos = i
                break
            else:
                i += 1
        return pos

    def modificar_usuario (self, indice):
        # Función que tiene como parámetros un índice que marca una posición en la [lista_de_usuarios]
        # Le pide al usuario una serie de datos para modificar dicha entrada den la lista y, si el proceso se lleva a cabo bien,
        # devuelve True y modifica la entrada en la lista, en caso contrario devuelve False.

        modificado = False        

        self.ui.limpiar_pantalla()

        nombre_nuevo = input('\nIntroduzca el nuevo nombre: ').strip()
        if nombre_nuevo:
            self.users[indice]['nombre'] = nombre_nuevo
            modificado = True
        else:
            self.ui.error('no se puede asignar una cadena vacía.')
            return modificado
            
        email_nuevo = input('\nIntroduzca el nuevo email: ').strip()
        if email_nuevo:
            self.users[indice]['email'] = email_nuevo
            modificado = True
        else:
            self.ui.error('no se puede asignar una cadena vacía.')
            return modificado

        id_nuevo = self.ui.pedir_entero('Introduzca el nuevo id: ', 1, None)
        self.users[indice]['id_user'] = id_nuevo

        return modificado


    def hacer_prestamo( self, indice, biblioteca ):
        # Función que ejecuta el proceso de hacer un préstamo por parte de un usuario y retira un ejemplar de la biblioteca.
        # Los parámetros son un objeto de tipo Usuarios (self), el índice que marca el usuario que quiere retirar el libro 
        # y un objeto del tipo Biblioteca que le pasamos desde el objeto de tipo GestorBiblioteca de menu.py >> ahora denominado biblioteca.py
        # Devuelve True si puede llevarse a cabo el préstamo y modifica los objetos self y biblioteca, devuelve False en caso contrario.

        modificado = False

        if ( len(self.users[indice]['libros_en_prestamo']) ) > 2:
            self.ui.error('el usuario ya tiene 3 libros en préstamo, no puede tener más.')
        else:
            titulo = input('\nIntroduzca el título de la obra a prestar: ').strip().lower()
            if not titulo:
                self.ui.error('el título del libro no puede ser una cadena vacía.')
            else:
                ind = biblioteca.en_biblioteca(titulo)
                if ind < 0:
                    self.ui.error('el libro no se encuentra en la biblioteca.')
                else:
                    if ( biblioteca.libros[ind]['stock'] ) < 1:
                        self.ui.error('no quedan ejemplares del libro disponibles.')
                    else:
                        biblioteca.libros[ind]['stock'] -= 1  # restamos un ejemplar del stock de la biblioteca.
                        self.users[indice]['libros_en_prestamo'].append(biblioteca.libros[ind]['título'])
                        modificado = True
        return modificado

    def hacer_devolucion( self, indice, biblioteca ):
        # Función que ejecuta el proceso de hacer una devolución por parte de un usuario y añade un ejemplar en la biblioteca.
        # Los parámetros son un objeto de tipo Usuarios (self), el índice que marca el usuario que quiere retirar el libro 
        # y un objeto del tipo Biblioteca que le pasamos desde el objeto de tipo GestorBiblioteca de menu.py.
        # Devuelve True si puede llevarse a cabo el préstamo y modifica los objetos self y biblioteca, devuelve False en caso contrario.

        modificado = False

        if not self.users[indice]['libros_en_prestamo']:
            self.ui.error('el usuario no tiene libros en préstamo, no puede devolver nada.')
        else:
            print(f'\nLibros en préstamo de: {self.users[indice]['nombre']}')
            print(f'======================={'='*len(self.users[indice]['nombre'])}\n')
            for i, libro in enumerate(self.users[indice]['libros_en_prestamo']):
                print(f'{i+1} - {libro}')
            print('\n')
            libro_a_retornar = self.ui.pedir_entero('Introduzca el ejemplar a devolver: ',1,len(self.users[indice]['libros_en_prestamo']))
            titulo = self.users[indice]['libros_en_prestamo'][libro_a_retornar-1].strip().lower()
            ind = biblioteca.en_biblioteca(titulo)
            if ind < 0:
                self.ui.error('el libro no se encuentra en la biblioteca.')
            else:
                biblioteca.libros[ind]['stock'] += 1 # añadimos el ejemplar devuelto al stock de la biblioteca.
                del self.users[indice]['libros_en_prestamo'][libro_a_retornar-1] # borramos el libro de la lista de préstamos del usuario.
                modificado = True
    
        return modificado



# 
#                                           Lista de funciones programadas en este módulo:
#                                           ==============================================
# 
#                           Return                        Call                               Parameters
# 
#                       (int posicion)                en_biblioteca         ( self, str titulo ) *método de la clase Biblioteca
#                       (None)                        agregar_libro         ( self, Libro libro ) *método de la clase Biblioteca
#                       ([libros diccionarios])       libros_por_autor      ( str autor, lista_diccionarios biblioteca )
#                       ([libros diccionarios])       libros_por_genero     ( str genero, lista_diccionarios biblioteca )
#                       (int posicion)                eliminar_libro        ( lista_diccionarios biblioteca )
#                       (None)                        menu_editar_libro     ( str titulo )
#                       (boll modificado)             modificar_libro       ( int indice, lista_diccionarios biblioteca )
#                       ([str generos])               buscar_generos        ( lista_diccionarios biblioteca )
#                       (None)                        menu_buscar_libro     ( None )
#                       (None)                        buscar_libro          ( lista_diccionarios biblioteca )
#                       (int posición)                isbn_en_biblioteca    ( lista_diccionarios biblioteca )


# Clase creada por Arnau. De nuevo, personalmente (Alex) habría usado una lista ya que se trata de una colección del tipo de objeto (Libro).
class Biblioteca:
    def __init__(self, lista_de_libros=None):

            if lista_de_libros is None:
                self.libros = []
            else:
                self.libros = lista_de_libros
            self.ui = m.Utiles() #Antiguo utiles

    # Añadir un libro (del tipo Libro) a un objeto del tipo Biblioteca.
    def agregar_libro(self, libro):
        if self.en_biblioteca(libro['título']) == -1:
            self.libros.append(libro)
            print(f'Libro "{libro["título"]}" agregado a la biblioteca.')
        else:
            print(f'Error: el libro "{libro["título"]}" ya existe en la biblioteca.')


    def en_biblioteca ( self, titulo ):
        # el título es una cadena y la lista_de_libros es una lista de diccionarios con clave 'título' que habrá que recorrer.
        # la función devuelve -1 si el libro no está en la lista de libros o el índice con su posición el la lista si está presente.
        pos = -1
        if self.libros:
            i = 0
            for libro in self.libros:
                if ( libro['título'].strip().lower() == titulo ) :
                    pos = i
                    break
                else:
                    i += 1
        return pos
    
    def isbn_en_biblioteca ( self, isbn ):
        # el isbn es un entero y la lista_de_libros es una lista de diccionarios con clave 'ISBN' que habrá que recorrer.
        # la función devuelve -1 si el libro no está en la lista de libros o el índice con su posición el la lista si está presente.
        pos = -1
        if self.libros:
            i = 0
            for libro in self.libros:
                if ( libro['ISBN'] == isbn ) :
                    pos = i
                    break
                else:
                    i += 1
        return pos


    def libros_por_autor (self, autor):

    # Función que tiene como parámetros de entrada un nombre de autor 'autor' y una lista de disccionarios con las obras del sistema
    # [lista_de_libros]. Si el autor no es la cadena vacía, devuelve la lista de libros dentro de la biblioteca cuyo autor sea el mismo
    # que el marcado por 'autor'.

        if not autor:
            self.ui.error('el nombre del autor no puede ser una cadena vacía.')
            return []
        else:
            return [ libro for libro in self.libros if libro['autor'].strip().lower() == autor]

    def libros_por_genero ( self, genero ):
        # Función que opera parecida a libros_por_autor, pero la lista que devuelve corresponde a la de los libros en [lista_de_libros]
        # cuyo género es el mismo que el del parámetro 'genero'.

        if not genero:
            self.ui.error('el nombre del género no puede ser una cadena vacía.')
            return []
        else:
            return [ libro for libro in self.libros if libro['género'].strip().lower() == genero]


    def buscar_por_titulo(self, titulo):
        titulo = titulo.strip().lower()
        for i, libro in enumerate(self.libros):
            if libro.titulo.lower() == titulo:
                return i
        return -1

    def eliminar_libro(self):

        # Función que le pregunta al usuario el título o el autor o el ISBN de una obra dentro de [lista_de_libros]
        # y retorna la posición del libro a buscar dentro de la lista o -1 en caso que no lo encuentre por los parámetros de búsqueda.
        posicion = -1
        op = self.ui.pedir_entero('\n¿Cómo quiere buscar la obra?\n\n1- Por título\n2- Por autor\n3.- Por ISBN\n',1,3)

        match op:
            case 1:
                titulo = input('\nIntroduzca el título de la obra... ').strip().lower()
                if not titulo:
                    self.ui.error('el nombre de la obra no puede ser una cadena vacía.')
                else:
                    posicion = self.en_biblioteca(titulo)
            case 2:
                autor = input('\nIntroduzca el autor de la obra... ').strip().lower()
                if not autor:
                    self.ui.error('el nombre del autor no puede ser una cadena vacía.')
                else:
                    # libros_del_autor = [ libro for libro in lista_de_libros if libro['autor'] == autor]
                    libros_del_autor = self.libros_por_autor(autor)
                    if not libros_del_autor:
                        self.ui.error('el autor no dispone de ninguna obra catalogada en la biblioteca.')
                    else:
                        print(f'\nLibros de {autor.capitalize()} en la Biblioteca personal:\n')
                        for indice, libro_del_autor in enumerate(libros_del_autor):
                            print(f'{indice+1} - {libro_del_autor['título']}')
                        print()
                        i = self.ui.pedir_entero('Escoja número de la obra (0 para cancelar): ',0,len(libros_del_autor))
                        if i > 0:
                            titulo_standard = libros_del_autor[i-1]['título'].strip().lower()
                            posicion = self.en_biblioteca( titulo_standard)
                        else:
                            self.ui.error('cancelación del borrado.')
            case 3:
                isbn = self.ui.pedir_entero('Introduzca el ISBN de la obra a eliminar del catálogo: ',1,None)
                posicion = self.isbn_en_biblioteca(isbn)
            case _:
                self.ui.error('inesperado borrando libro.')

        return posicion


    def menu_editar_libro (self, titulo):
        # Función para mostrar la interfaz de edición de entradas en la biblioteca personal.
            print(f'''
        Edición del libro: {titulo}
        ==================={'='*len(titulo)}

        1.- Modificar el título.
        2.- Modificar el autor.
        3.- Modificar el género.
        4.- Modificar el número de ISBN.
        5.- Modificar el stock.
        6.- Salir de la modificación del libro.
                ''')

    def modificar_libro (self, indice ):
        # Función que tiene como parámetros un índice que marca una posición en la [lista_de_libros]
        # Le pide al usuario una serie de datos para modificar dicha entrada den la lista y, si el proceso se lleva a cabo bien,
        # devuelve True y modifica la entrada en la lista, en caso contrario devuelve False.

        modificado = False
        salir = False

        while not salir:
            self.ui.limpiar_pantalla()
            self.menu_editar_libro(self.libros[indice]['título'].strip())

            opcion = self.ui.pedir_entero('Escoja opción [1-6]: ',1,6)

            match opcion:

                case 1:
                    titulo_nuevo = input('\nIntroduzca el nuevo título: ').strip()
                    if titulo_nuevo:
                        self.libros[indice]['título'] = titulo_nuevo
                        modificado = True
                    else:
                        self.ui.error('no se puede asignar una cadena vacía.')
                case 2:
                    autor_nuevo = input('\nIntroduzca el nuevo autor: ').strip()
                    if autor_nuevo:
                        self.libros[indice]['autor'] = autor_nuevo
                        modificado = True
                    else:
                        self.ui.error('no se puede asignar una cadena vacía.')
                case 3:
                    genero_nuevo = input('\nIntroduzca el nuevo género: ').strip().lower()
                    if genero_nuevo:
                        self.libros[indice]['género'] = genero_nuevo
                        modificado = True
                    else:
                        self.ui.error('no se puede asignar una cadena vacía.')
                case 4:
                    isbn = self.ui.pedir_entero('\nIntroduzca el código ISBN del libro: ',1,None)
                    self.libros[indice]['ISBN'] = isbn
                    modificado = True
                case 5:
                    stock = self.ui.pedir_entero('\nIntroduzca cuántas copias nuevas del libro han llegado: ',1,None)
                    self.libros[indice]['stock'] += stock
                    modificado = True
                case 6:
                    salir = True

            if opcion in [1,2,3,4,5]:
                self.ui.esperar_input()

        return modificado

    def buscar_generos (self):
        # Función que devuelve un set con los distintos géneros existentes en la biblioteca [lista_de_libros]
        lista_de_generos = set([])
        if not self.libros:
            return []
        else:
            for libro in self.libros:
                lista_de_generos.add(libro['género'])
            return lista_de_generos


    def buscar_libro ( self ):
        # Función que tiene como parámetros una [lista_de_libros]
        # Dependiendo de la entrada del usuario le ofrece una información u otra de la biblioteca [lista_de_libros]

        salir = False

        while not salir:
            self.ui.limpiar_pantalla()
            self.ui.menu_buscar_libro()
            opcion = self.ui.pedir_entero('Escoja opción [1-5]: ',1,5)
            match opcion:

                case 1:
                    titulo = input('\nIntroduzca el título a buscar: ').strip().lower()
                    if titulo:
                        pos = self.en_biblioteca(titulo)
                        if pos < 0:
                            self.ui.error('título no encontrado en la biblioteca.')
                        else:
                            print(f'\n{self.libros[pos]['título']}, escrito por {self.libros[pos]['autor']}, ISBN: {self.libros[pos]['ISBN']} stock: {self.libros[pos]['stock']}.')
                    else:
                        self.ui.error('no se puede asignar una cadena vacía.')
                case 2:
                    autor = input('\nIntroduzca el nombre del autor cuyos libros quieres buscar: ').strip().lower()
                    if autor:
                        libros = self.libros_por_autor(autor)
                        print(f'\nLos libros encontrados en la biblioteca de {autor} son:')
                        print(f'============================================{'='*len(autor)}====\n')
                        for i, libro in enumerate(libros):
                            print(f'{i+1} - {libro['título']}, ISBN: {libro['ISBN']}, stock: {libro['stock']}.')    
                    else:
                        self.ui.error('no se puede asignar una cadena vacía.')
                case 3:
                    generos = self.buscar_generos()
                    self.ui.limpiar_pantalla()
                    print(f'\nLa lista de géneros encontrados en la biblioteca es:')
                    print('====================================================')
                    print(generos)
                    genero = input('\nIntroduzca el género de las obras a buscar: ').strip().lower()
                    if genero:
                        libros = self.libros_por_genero(genero)
                        print(f'\nLos libros encontrados en la biblioteca del género {genero} son:')
                        print(f'===================================================={'='*len(genero)}====\n')
                        for i, libro in enumerate(libros):
                            print(f'{i+1} - {libro['título']} de {libro['autor']}, ISBN: {libro['ISBN']} disponibles: {libro['stock']}.')
                    else:
                        self.ui.error('no se puede asignar una cadena vacía.')
                case 4:
                    isbn = self.ui.pedir_entero('Introduzca el ISBN del libro a buscar: ',1,None)
                    pos = self.isbn_en_biblioteca(isbn)
                    if pos < 0:
                        self.ui.error('ISBN no presente en el catálogo de libros.')
                    else:
                        print(f'\n{self.libros[pos]['título']}, escrito por {self.libros[pos]['autor']}, stock: {self.libros[pos]['stock']}.')
                case 5:
                    salir = True

            if opcion in [1,2,3,4]:
                self.ui.esperar_input()


    def generos_disponibles(self):
        return set(libro.genero for libro in self.libros)



