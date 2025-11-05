


import os
import menu as m
# =====================================================
# CLASE LIBRO
# =====================================================
class Libro:
    def __init__(self, titulo, autor, genero, paginas, leido=False):
        self.titulo = titulo.strip()
        self.autor = autor.strip()
        self.genero = genero.strip().lower()
        self.paginas = paginas
        self.leido = leido

    def __str__(self):
        estado = "leído" if self.leido else "no leído"
        return f"{self.titulo} de {self.autor} ({self.genero}) - {self.paginas} págs., {estado}"

    def alternar_estado(self):
        self.leido = not self.leido

class Libro_user:
    def __init__(self, ISBN, titulo, autor, genero, paginas, stock, leido=False):
        self.idLib = ISBN.strip()
        self.titulo = titulo.strip()
        self.autor = autor.strip()
        self.genero = genero.strip().lower()
        self.paginas = paginas
        self.stock = stock
        self.leido = leido

    def __str__(self):
        estado = "leído" if self.leido else "no leído"
        return f"{self.titulo} de {self.autor} ({self.genero}) - {self.paginas} págs., {estado} (ID: {self.id_libro}, Stock: {self.stock})"


    def alternar_estado(self):
        self.leido = not self.leido
  
    def hay_stock(self):
        return self.stock > 0

    def reservar(self):
        if self.hay_stock():
            self.stock -= 1
            return True
        return False


class Usuarios:
    def __init__(self, id_user, nombre, email, Biblioteca=None):
        self.idUser = id_user
        self.nombre = nombre.strip()
        self.email = email.strip()
        

        if Biblioteca is None:
                self.libros = []
        else:
                self.libros = Biblioteca
                self.ui = m.Utiles() #Antiguo utiles
    
    # Añadir un usuario
    def agregar_user(self, user):
        if self.en_biblioteca(user['nombre']) == -1:
            self.libros.append(user)
            print(f'Libro "{user["nombre"]}" agregado a usuarios.')
        else:
            print(f'Error: el usuario "{user["nombre"]}" ya existe en usuarios.')


    def en_usuarios ( self, nombre ):
        # el título es una cadena y la lista_de_libros es una lista de diccionarios con clave 'título' que habrá que recorrer.
        # la función devuelve -1 si el libro no está en la lista de libros o el índice con su posición el la lista si está presente.
        pos = -1
        if not self.libros:
            return pos

        i = 0
        for libro in self.libros:
            if ( libro['título'].strip().lower() == titulo ) :
                pos = i
                break
            else:
                i += 1
        return pos


# 
#                                           Lista de funciones programadas en este módulo:
#                                           ==============================================
# 
#                           Return                        Call                               Parameters
# 
#                       (int posicion)                en_biblioteca         ( str titulo, lista_diccionarios biblioteca )
#                       ([libros diccionarios])       libros_por_autor      ( str autor, lista_diccionarios biblioteca )
#                       ([libros diccionarios])       libros_por_genero     ( str genero, lista_diccionarios biblioteca )
#                       (int posicion)                eliminar_libro        ( lista_diccionarios biblioteca )
#                       (None)                        menu_editar_libro     ( str titulo )
#                       (boll modificado)             modificar_libro       ( int indice, lista_diccionarios biblioteca )
#                       ([str generos])               buscar_generos        ( lista_diccionarios biblioteca )
#                       (None)                        menu_buscar_libro     ( None )
#                       (None)                        buscar_libro          ( lista_diccionarios biblioteca )
#                       (None)                        mostrar_estadisticas  ( lista_diccionarios biblioteca )


class Biblioteca:
    def __init__(self, lista_de_libros=None):

            if lista_de_libros is None:
                self.libros = []
            else:
                self.libros = lista_de_libros
            self.ui = m.Utiles() #Antiguo utiles

    # Añadir un libro
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
        if not self.libros:
            return pos

        i = 0
        for libro in self.libros:
            if ( libro['título'].strip().lower() == titulo ) :
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

        # Función que le pregunta al usuario el título o el autor de una obra dentro de [lista_de_libros]
        # y retorna la posición del libro a buscar dentro de la lista o -1 en caso que no lo encuentre por los parámetros de búsqueda.
        posicion = -1
        op = self.ui.pedir_entero('\n¿Cómo quiere buscar la obra? 1- por título, 2- por autor. ',1,2)

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
        4.- Modificar el número de páginas.
        5.- Modificar el estado de lectura.
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
                    paginas = self.ui.pedir_entero('\nIntroduzca el número de páginas del libro: ',1,None)
                    self.libros[indice]['páginas'] = paginas
                    modificado = True
                case 5:
                    if self.libros[indice]['leído']:
                        print('\nModificando el estado del libro de "leído" a "no leído".' )
                        self.libros[indice]['leído'] = False
                        modificado = True
                    else:
                        print('\nModificando el estado del libro de "no leído" a "leído".' )
                        self.libros[indice]['leído'] = True
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
            opcion = self.ui.pedir_entero('Escoja opción [1-4]: ',1,4)
            match opcion:

                case 1:
                    titulo = input('\nIntroduzca el título a buscar: ').strip().lower()
                    if titulo:
                        pos = self.en_biblioteca(titulo)
                        if pos < 0:
                            self.ui.error('título no encontrado en la biblioteca.')
                        else:
                            if self.libros[pos]['leído']:
                                leido = 'leído'
                            else:
                                leido = 'no leído'
                            print(f'\n{self.libros[pos]['título']}, escrito por {self.libros[pos]['autor']}: {leido}.')
                    else:
                        self.ui.error('no se puede asignar una cadena vacía.')
                case 2:
                    autor = input('\nIntroduzca el nombre del autor cuyos libros quieres buscar: ').strip().lower()
                    if autor:
                        libros = self.libros_por_autor(autor)
                        print(f'\nLos libros encontrados en la biblioteca de {autor} son:')
                        print(f'============================================{'='*len(autor)}====\n')
                        for i, libro in enumerate(libros):
                            if libro['leído']:
                                leido = 'leído'
                            else:
                                leido = 'no leído'
                            print(f'{i+1} - {libro['título']}, {leido}.')    
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
                            if libro['leído']:
                                leido = 'leído'
                            else:
                                leido = 'no leído'
                            print(f'{i+1} - {libro['título']} de {libro['autor']}, {leido}.')
                    else:
                        self.ui.error('no se puede asignar una cadena vacía.')
                case 4:
                    salir = True

            if opcion in [1,2,3]:
                self.ui.esperar_input()


    def generos_disponibles(self):
        return set(libro.genero for libro in self.libros)

    def estadisticas_biblioteca(self):

        # Función que tiene como entrada una biblioteca, esto es, una [lista_de_libros], donde cada libro es un diccionario con
        # las llaves: título, autor, género, páginas y leído.
        # Y muestra por pantalla los siguientes datos:
        # Total de libros en la biblioteca, promedio de páginas y porcentaje de libros leídos/total_de_libros en la biblioteca.

        if self.libros:
            total_libros = len(self.libros)
            promedio_paginas = 0
            leidos = 0
            for libro in self.libros:
                promedio_paginas += libro['páginas']
                if libro['leído']:
                    leidos += 1
            promedio_paginas /= total_libros
            porcentaje = leidos * 100 / total_libros

            print(f'\nLa biblioteca contiene {total_libros} libros, de los cuales has léido un {porcentaje:.2f}% y el promedio de páginas de todos los libros es de: {round(promedio_paginas)}')
        else:
            self.ui.error('no se pueden mostrar estadísticas, no hay biblioteca.')


