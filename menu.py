import os 
import metodo as met
from pathlib import Path


import json


class GestorArchivo:
    
    # def __init__(self, ruta_archivo='libros.json'):
    def __init__(self, ruta_archivo):
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
        try:
            with self.ruta_archivo.open('w', encoding='utf-8') as f:
                json.dump(lista_de_libros, f, ensure_ascii=False, indent=2)
        except PermissionError:
            self.ui.error('No tienes permisos de acceso.')



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
5.- Mostrar Estadísticas.
6.- Salir del Gestor.
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
    4.- Salir del menú de búsquedas.
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
    def validar_datos(titulo, autor, genero, paginas):
        print('\nConfirme que quiere introducir la siguiente entrada a la Biblioteca personal:')
        print(f'Título: {titulo}, autor: {autor}, género: {genero}, # de páginas: {paginas}.\n')
        respuesta = input('Confirme (y/n): ').strip().lower()
        return respuesta == 'y'

    @staticmethod
    def validar_datos_lib(titulo, autor, genero, paginas, stock):
        print('\nConfirme que quiere introducir la siguiente entrada a la Biblioteca personal:')
        print(f'Título: {titulo}, autor: {autor}, género: {genero}, # de páginas: {paginas}.\n')
        respuesta = input('Confirme (y/n): ').strip().lower()
        return respuesta == 'y'

    @staticmethod
    def validar_datos_user(nombre, email):
        print('\nConfirme que quiere introducir la siguiente entrada a la Biblioteca personal:')
        print(f'Título: {titulo}, autor: {autor}, género: {genero}, # de páginas: {paginas}.\n')
        respuesta = input('Confirme (y/n): ').strip().lower()
        return respuesta == 'y'



# =====================================================
# EJECUCIÓN PRINCIPAL
# =====================================================


# from libros import Libro, Biblioteca
# from archivos import Archivo as a


class GestorBiblioteca:
    def __init__(self):
        self.a = GestorArchivo('libros.json')
        self.biblioteca = met.Biblioteca(self.a.leer_archivo()) #mecoge la clase biblioteca con la lectura del archivo
        self.ui = Utiles() #Antiguo utiles
        self.us = GestorArchivo('usuarios.json')
        self.usuario = met.Usuarios(self.us.leer_archivo()) #mecoge la clase usuarios con la lectura del archivo
        

    def menu_principal(self):
        salir = False
        while not salir:
            self.ui.limpiar_pantalla()
            self.ui.mostrar_menu_principal()
            opcion = self.ui.pedir_entero('Escoja opción [1-6]: ', 1, 6)


            match opcion:
                case 1:
                    self.agregar_libro()
                case 2:
                    self.eliminar_libro()
                case 3:
                    self.modificar_libro()
                case 4:
                    self.biblioteca.buscar_libro()

                case 5:
                    self.biblioteca.estadisticas_biblioteca()
                case 6:
                    print('\nGracias por usar el Gestor de Biblioteca Personal. Guardando el archivo. ¡Hasta la próxima!\n')
                    self.a.actualizar_archivo(self.biblioteca.libros)
                    salir = True
                case _:
                    self.ui.error('opción no contemplada en el menú.')
                    self.ui.esperar_input()


            if opcion in [1, 2, 3, 5]:
                self.ui.esperar_input()



    def agregar_libro(self):
        titulo = input('\nIntroduzca el título de la obra: ')
        autor = input('Introduzca el autor de la obra: ')
        genero = input('Introduzca el género de la obra: ').strip().lower()
        paginas = self.ui.pedir_entero('Introduzca el número de páginas de la obra: ',1,None)
        stock = self.ui.pedir_entero('Introduzca el número de copias de la obra: ',1,None)
        leido = False


        if not titulo or not autor or not genero:
            self.ui.error("Datos de entrada erróneos.")
            return
        else:
            if self.biblioteca.en_biblioteca ( titulo ) == -1: # comprobamos que el libro no esté en nuestra biblioteca ya.
                if self.ui.validar_datos(titulo, autor, genero, stock, paginas): #ideas
                    print(f'Añadiendo {titulo} a la biblioteca personal.')

                    libro = {
                        'título': titulo,
                        'autor': autor,
                        'género': genero,
                        'páginas': paginas,
                        'stock': stock,
                        'leído': leido
                    }
                    nom = input('\nIntroduzca el nombre del usuario: ')
                    email = input('Introduzca el email del usuario: ')
                    if self.usuario.en_usuarios ( nom ) == -1: # comprobamos que el libro no esté en nuestra biblioteca ya.
                        if self.ui.validar_datos(nom, email): #ideas



                    self.biblioteca.agregar_libro(libro)
                    self.a.actualizar_archivo(self.biblioteca.libros)
                else:
                    print('Entrada descartada.')
            else:
                self.ui.error(' el libro ya está en la biblioteca, no se puede añadir otra instancia nueva.')
        self.ui.esperar_input()

             
   
    def eliminar_libro(self):
        indice = self.biblioteca.eliminar_libro()
        if indice < 0:
            self.ui.error('el libro no se puede eliminar, no está en la biblioteca.')
        else:
            print(f'\nEliminando {self.biblioteca.libros[indice]['título']} de la biblioteca.')
            del(self.biblioteca.libros[indice])
            self.a.actualizar_archivo(self.biblioteca.libros)
        self.ui.esperar_input()

    def modificar_libro(self):
        titulo = input('\nIntroduzca el título de la obra a editar: ').strip().lower()
        if not titulo:
            self.ui.error('el título del libro no puede ser una cadena vacía.')
        else:
            indice = self.biblioteca.en_biblioteca( titulo)
            if indice < 0:
                self.ui.error('el libro no se encuentra en la biblioteca.')
            else:
                mod = self.biblioteca.modificar_libro( indice )
                if not mod:
                    self.ui.error('la entrada del libro no ha sido modificada.')
                else:
                    self.a.actualizar_archivo(self.biblioteca.libros)
                    print('Entrada modificada y actualizada en el archivo.')
        self.ui.esperar_input()

if __name__ == "__main__":
    gestor = GestorBiblioteca()
    gestor.menu_principal()
