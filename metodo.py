


import os
import json
import re
from pathlib import Path

class GArchivo_Usuario:
    
    def __init__(self, ruta_archivo = 'usuario.json'):
        self.ruta_archivo = Path(ruta_archivo)
        self.ui = Utiles()
        
    def leer_archivo (self):
        lista_de_users = []

        try:
            with self.ruta_archivo.open('r', encoding='utf-8') as f:
                lista_de_libros = json.load(f)
        except FileNotFoundError:
            self.ui.error('El archivo no existe.')
        except PermissionError:
            self.ui.error('No tienes permisos de acceso.')
        except json.JSONDecodeError:
            self.ui.error('El archivo contiene datos corruptos.')
        return lista_de_users

    def actualizar_archivo(self, lista_de_users):

        if not lista_de_users:
            val = 'w'
        else:
            val = 'a'

        try:
            with self.ruta_archivo.open(val, encoding='utf-8') as f:
                json.dump(lista_de_users, f, ensure_ascii=False, indent=2)
        except PermissionError:
            self.ui.error('No tienes permisos de acceso.')

class GestorArchivo:
    
    def __init__(self, ruta_archivo):
        if ruta_archivo == 'libros.json':
                self.ruta_archivo = Path(ruta_archivo)
        else:
            self.ruta_archivo = Path(ruta_archivo)

        self.ui = Utiles()
        
    def leer_archivo (self):
        lista_de_libros = []

        try:
            with self.ruta_archivo.open('r', encoding='utf-8') as f:
                lista_de_libros = json.load(f)
        except FileNotFoundError:
            self.ui.error('El archivo no existe.')
        except PermissionError:
            self.ui.error('No tienes permisos de acceso.')
        except json.JSONDecodeError:
            self.ui.error('El archivo contiene datos corruptos.')
        return lista_de_libros

    def actualizar_archivo(self, lista_de_libros):

        if not lista_de_libros:
            val = 'w'
        else:
            val = 'a'

        try:
            with self.ruta_archivo.open('w', encoding='utf-8') as f:
                json.dump(lista_de_libros, f, ensure_ascii=False, indent=2)
        except PermissionError:
            self.ui.error('No tienes permisos de acceso.')




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

    def hay_stock(self):
        return self.stock > 0

       
class Usuario:
    def __init__(self, id_user, nombre, email, prestados, cantidad):
        self.idUser = id_user
        self.nombre = nombre.strip()
        self.email = email.strip()
        self.libros_en_prestamo = prestados
        self.cant = cantidad

    def __str__(self):
        return f"{self.idUser} de {self.nombre} ({self.email}) {self.libros_en_prestamo} {self.cant}"

    #funcion que agrega el prestamo al usuario
    def agregar_prestamo(self, titulo):
        if len(self.libros_en_prestamo) >= 3:
            return False
        self.libros_en_prestamo.append(titulo)
        self.cant += 1
        return True



class Usuarios:

    def __init__(self, archivo="usuarios.json"):
        self.archivo = archivo
        self.users = []
        self.ui = Utiles()
        self.biblioteca = Biblioteca()
        self.val = validate()
        self.cargar_usuarios()  # 🔹 Carga los usuarios existentes al iniciar

    def agregar_user(self, user_obj):
        self.users.append(user_obj)

    def en_usuarios(self, nombre):
        nombre = nombre.strip().lower()
        for i, u in enumerate(self.users):
            if u.nombre.lower() == nombre:
                return i
        return -1


    def guardar_usuarios(self):
        data = []
        for u in self.users:
            user_dict = {
                "id_user": u.idUser,
                "nombre": u.nombre,
                "email": u.email,
                "libros_en_prestamo": u.libros_en_prestamo,
                "cantidad_prestados": u.cant
            }
            data.append(user_dict)

        try:
            # Crea la carpeta si no existe
            carpeta = os.path.dirname(self.archivo)
            if carpeta and not os.path.exists(carpeta):
                os.makedirs(carpeta)

            with open(self.archivo, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)

            print(f"✅ Archivo '{self.archivo}' actualizado correctamente.")

        except Exception as e:
            print(f"⚠️ Error al guardar los usuarios: {e}")

    def cargar_usuarios(self):
        if not os.path.exists(self.archivo):
            self.users = []
            return

        try:
            with open(self.archivo, 'r', encoding='utf-8') as f:
                data = json.load(f)

            self.users = [
                Usuario(
                    id_user=u["id_user"],
                    nombre=u["nombre"],
                    email=u["email"],
                    prestados=u.get("libros_en_prestamo", []),
                    cantidad=u.get("cantidad_prestados", 0)
                ) for u in data
            ]

            print(f"📂 {len(self.users)} usuarios cargados desde '{self.archivo}'.")

        except Exception as e:
            print(f"⚠️ Error al cargar los usuarios: {e}")
            self.users = []

    def modificar_usuario(self, indice):
        user = self.users[indice]
        cant_m = 0
        modificado = False
        self.ui.limpiar_pantalla()
    
        nombre_nuevo = input(f'\nIntroduzca el nuevo nombre de {user.nombre}: ').strip()
        if nombre_nuevo.isalpha():
            cant_m += 1
        else:
            self.ui.error('no se puede asignar una cadena vacía.')

        email_nuevo = input(f'\nIntroduzca el nuevo email  {user.email}: ').strip()
        if validate.validar_email(email_nuevo):
            cant_m += 1
        else:
            self.ui.error('no se puede asignar una cadena vacía.')

        id_nuevo = self.ui.pedir_entero('Introduzca el nuevo id: ', 1, None)
        if id_nuevo:
            cant_m += 1
        else:
            self.ui.error('no se puede asignar una cadena vacía.')


        if cant_m == 3:
            # Modificar los datos
            user.nombre = nombre_nuevo
            user.email = email_nuevo
            user.idUser = id_nuevo

            # Guardar la lista actualizada
            self.guardar_usuarios()

            print(f"✅ Usuario '{user.nombre}' modificado correctamente.")
            return True
        else:
            self.ui.error('Alguno de los datos no se introdujo y no se modifica el usuario')
            
            
    def hacer_prestamo(self, indice):
        usuario = self.users[indice]

        if len(usuario.libros_en_prestamo) >= 3:
            self.ui.error('El usuario ya tiene 3 libros en préstamo.')
            return

        titulo = input('\nIntroduzca el título de la obra a prestar: ').strip().lower()
        if not titulo:
            self.ui.error('El título del libro no puede ser una cadena vacía.')
            return

        ind = self.biblioteca.en_biblioteca(titulo)
        if ind < 0:
            self.ui.error('El libro no se encuentra en la biblioteca.')
            return

        libro = self.biblioteca.libros[ind]
        if libro['stock'] < 1:
            self.ui.error('No quedan ejemplares disponibles.')
            return

        # ✅ Hacer el préstamo
        libro['stock'] -= 1
        usuario.libros_en_prestamo.append(libro['título'])
        usuario.cant += 1

        # ✅ Guardar los usuarios y libros actualizados
        self.guardar_usuarios()
        self.biblioteca.guardar_libros()

        print(f"✅ El libro '{libro['título']}' ha sido prestado a {usuario.nombre}.")
 
    def hacer_devolucion(self, indice):
        usuario = self.users[indice]

        if not usuario.libros_en_prestamo:
            self.ui.error('El usuario no tiene libros en préstamo.')
            return

        print(f"\nLibros en préstamo de {usuario.nombre}:")
        for i, titulo in enumerate(usuario.libros_en_prestamo, start=1):
            print(f"{i}. {titulo}")

        titulo = input('\nIntroduzca el título del libro que desea devolver: ').strip().lower()
        if not titulo:
            self.ui.error('El título no puede ser una cadena vacía.')
            return

        titulos_norm = [t.lower() for t in usuario.libros_en_prestamo]
        if titulo not in titulos_norm:
            self.ui.error('Ese libro no figura entre los préstamos del usuario.')
            return

        ind_libro = self.biblioteca.en_biblioteca(titulo)
        if ind_libro < 0:
            self.ui.error('El libro no se encuentra en la biblioteca.')
            return

        # Actualizar datos
        libro = self.biblioteca.libros[ind_libro]
        libro['stock'] += 1
        index_en_usuario = titulos_norm.index(titulo)
        usuario.libros_en_prestamo.pop(index_en_usuario)
        usuario.cant -= 1

        # 🔹 Guardar cambios en archivos
        self.biblioteca.guardar_libros()
        self.guardar_usuarios()

        print(f"✅ El libro '{libro['título']}' ha sido devuelto por {usuario.nombre}.")

class validate:
    
    def validar_email(email):
        patron = r'^[^\s@]+@[^\s@]+\.[^\s@]+$'
        return re.match(patron, email) is not None

    # # Ejemplo:
    # emails = ["usuario@dominio.com", "mal@correo", "otro@dominio.co"]
    # for e in emails:
    #     print(e, "✅ Válido" if validar_email(e) else "❌ Inválido")





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
#                       (int posición)                isbn_en_biblioteca    ( lista_diccionarios biblioteca )

# class Biblioteca:
    # def __init__(self, libros):
    #     self.libros = libros  # lista de diccionarios
    #     self.archivo = 'libros.json'


class Biblioteca:

    def __init__(self, lista_de_libros=None, archivo="libros.json"):
        self.archivo = archivo
        if not lista_de_libros:
            self.libros = self._cargar_desde_archivo()
        else:
            self.libros = lista_de_libros
        self.ui = Utiles() #Antiguo utiles

    def guardar_libros(self):
        try:
            with open(self.archivo, 'w', encoding='utf-8') as f:
                json.dump(self.libros, f, ensure_ascii=False, indent=4)
            print("✅ Biblioteca guardada correctamente.")
        except Exception as e:
            print(f"⚠️ Error al guardar la biblioteca: {e}")

    def _cargar_desde_archivo(self):
        import json, os
        if os.path.exists(self.archivo):
            try:
                with open(self.archivo, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    print(f"📚 Biblioteca cargada ({len(data)} libros).")
                    return data
            except Exception as e:
                print(f"⚠️ Error al cargar biblioteca: {e}")
                return []
        else:
            print(f"ℹ️ No se encontró {self.archivo}, se creará vacío.")
            return []


    # Añadir un libro
    def agregar_libro(self, libro):
        if self.en_biblioteca(libro['título']) == -1:
            self.libros.append(libro)
            print(f'Libro "{libro["título"]}" agregado a la biblioteca.')
        else:
            print(f'Error: el libro "{libro["título"]}" ya existe en la biblioteca.')

    def guardar_libros(self):
        import json
        try:
            with open(self.archivo, "w", encoding="utf-8") as f:  # 🔹 modo 'w', no 'a'
                json.dump(self.libros, f, indent=2, ensure_ascii=False)
            print(f"✅ Biblioteca guardada ({len(self.libros)} libros).")
        except Exception as e:
            print(f"⚠️ Error al guardar biblioteca: {e}")

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

class Utiles:

    @staticmethod
    def error(cadena):
        print(f'\nError: {cadena}')

    @staticmethod
    def esperar_input():
        input('\nPresione la tecla [ENTER]')

    @staticmethod
    def limpiar_pantalla():
        os.system('cls' if os.name == 'nt' else 'clear')

    @staticmethod
    def mostrar_menu_principal():
        print('''
Gestor de Biblioteca Personal:
=============================

1.- Añadir Libro.
2.- Eliminar Libro.
3.- Editar/Modificar Libro.
4.- Buscar Libro.
5.- Introducir Usuario.
6.- Modificar Usuario.
7.- Devolución de Libro.
8.- Préstamo de Libro.
9.- Salir del Gestor.
          ''')   
    
    @staticmethod     
    def menu_buscar_libro ():
    # Función para mostrar la interfaz de búsqueda de entradas en la biblioteca personal.
        print('''
    Búsquedas de libro:
    ==================

    1.- Por título.
    2.- Por autor.
    3.- Por género.
    4.- Por ISBN.
    5.- Salir del menú de búsquedas.
            ''')


    @staticmethod
    def pedir_entero(mensaje, valor_minimo=None, valor_maximo=None):
        while True:
            try:
                valor = int(input(mensaje))
                if valor_minimo is not None and valor < valor_minimo:
                    continue
                if valor_maximo is not None and valor > valor_maximo:
                    continue
                return valor
            except ValueError:
                print('Introduce un número válido.')

    @staticmethod
    def validar_datos(titulo, autor, genero, isbn, stock):
        print('\nConfirme que quiere introducir la siguiente entrada a la Biblioteca personal:')
        print(f'Título: {titulo}, autor: {autor}, género: {genero}, ISBN: {isbn}, unidades disponibles: {stock}.\n')
        respuesta = input('Confirme (y/n): ').strip().lower()
        return respuesta == 'y'
   

    @staticmethod
    def validar_datos_user(nombre, email):
        print('\nConfirme que quiere introducir la siguiente entrada a la Biblioteca personal:')
        print(f'Nombre: {nombre}, E-mail: {email}.\n')
        respuesta = input('Confirme (y/n): ').strip().lower()
        return respuesta == 'y'




