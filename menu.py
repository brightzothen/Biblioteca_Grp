mport os 
from metodo import Usuarios, Biblioteca, Usuario, Utiles, GestorArchivo, GArchivo_Usuario

import json

# =====================================================
# EJECUCIÓN PRINCIPAL
# =====================================================


# from libros import Libro, Biblioteca
# from archivos import Archivo as a


class GestorBiblioteca:
    
    def __init__(self):
        self.a = GestorArchivo('libros.json')
        self.biblioteca = Biblioteca(self.a.leer_archivo()) #mecoge la clase biblioteca con la lectura del archivo
        self.ui = Utiles() #Antiguo utiles
        self.us = GArchivo_Usuario('usuarios.json')
        self.usuarios = Usuarios("usuarios.json")
        
        # self.usuario = Usuarios()  # Aquí creas el objeto Usuarios
        # self.biblioteca = Biblioteca()  # si tienes biblioteca también

        # self.a = GestorArchivo('libros.json')
        # # self.biblioteca = met.Biblioteca(self.a.leer_archivo()) #mecoge la clase biblioteca con la lectura del archivo
        # self.ui = Utiles() #Antiguo utiles
        # self.us = GestorArchivo('usuarios.json')
        # self.usuario = met.Usuarios(self.us.leer_archivo()) #mecoge la clase usuarios con la lectura del archivo




    def menu_principal(self):
        salir = False
        while not salir:
            self.ui.limpiar_pantalla()
            self.ui.mostrar_menu_principal()
            opcion = self.ui.pedir_entero('Escoja opción [1-9]: ', 1, 9)


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
                    self.agregar_user()
                case 6:
                    self.modificar_usuario()
                case 7:
                    self.hacer_devolucion()
                case 8:
                    self.hacer_prestamo()
                case 9:
                    print('\nGracias por usar el Gestor de Biblioteca. Guardando el archivo. ¡Hasta la próxima!\n')
                    self.a.actualizar_archivo(self.biblioteca.libros)
                    salir = True
                case _:
                    self.ui.error('opción no contemplada en el menú.')
                    self.ui.esperar_input()


            if opcion in [1, 2, 3, 5, 6, 8]:
                self.ui.esperar_input()



    def agregar_libro(self):
        titulo = input('\nIntroduzca el título de la obra: ')
        autor = input('Introduzca el autor de la obra: ')
        genero = input('Introduzca el género de la obra: ').strip().lower()
        isbn = self.ui.pedir_entero('Introduzca el ISBN de la obra: ',1,None)
        stock = self.ui.pedir_entero('Introduzca las unidades en biblioteca: ',1,None)


        if not titulo or not autor or not genero:
            self.ui.error("Datos de entrada erróneos.")
            return
        else:
            if self.biblioteca.en_biblioteca ( titulo ) == -1: # comprobamos que el libro no esté en nuestra biblioteca ya.
                if self.ui.validar_datos(titulo, autor, genero, isbn, stock): #ideas
                    print(f'Añadiendo {titulo} a la biblioteca personal.')

                    libro = {
                        'título': titulo,
                        'autor': autor,
                        'género': genero,
                        'ISBN': isbn,
                        'stock': stock
                    }




                    self.biblioteca.agregar_libro(libro)
                    self.a.actualizar_archivo(self.biblioteca.libros)
                else:
                    print('Entrada descartada.')
            else:
                self.ui.error(' el libro ya está en la biblioteca, no se puede añadir otra instancia nueva.')
        # self.ui.esperar_input()

             
   
    def eliminar_libro(self):
        indice = self.biblioteca.eliminar_libro()
        if indice < 0:
            self.ui.error('El libro no se ha podido eliminar.')
        else:
            print(f'\nEliminando {self.biblioteca.libros[indice]['título']} de la biblioteca.')
            del(self.biblioteca.libros[indice])
            self.a.actualizar_archivo(self.biblioteca.libros)
        # self.ui.esperar_input()

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
        # self.ui.esperar_input()

    def agregar_user(self):
        
        nombre = input('\nIntroduzca el nombre del usuario: ').strip().lower()
        email = input('Introduzca el email  del usuario: ').strip().lower()
        idn = self.ui.pedir_entero('Introduzca el id del usuario: ',1,None)
        prestamos = []
        
        if not nombre or not email:
            self.ui.error("Datos de entrada erróneos.")
            return
        else:
            if self.usuarios.en_usuarios ( nombre ) == -1: # comprobamos que el usuario no esté en nuestra lista ya.
                if self.ui.validar_datos_user(nombre, email): #ideas
                    print(f'Añadiendo {nombre} a la lista de usuarios.')

                    userd = Usuario(idn, nombre, email, [], 0)
        
                    self.usuarios.agregar_user(userd)
                    self.usuarios.guardar_usuarios()

                else:
                    print('Entrada descartada.')
            else:
                self.ui.error(' el usuario ya está en la biblioteca, no se puede añadir otra instancia nueva.')

    def modificar_usuario(self):
        nombre = input('\nIntroduzca el nombre del usuario a modificar: ').strip().lower()
        if not nombre:
            self.ui.error('el nombre no puede ser una cadena vacía.')
        else:
            indice = self.usuarios.en_usuarios(nombre)
            if indice < 0:
                self.ui.error('el usuario no se encuentra en la biblioteca.')
            else:
                mod = self.usuarios.modificar_usuario(indice)
                if not mod:
                    self.ui.error('la entrada del usuario no ha sido modificada.')
                else:
                    self.usuarios.guardar_usuarios()  # Guardamos los cambios

                    # self.us.actualizar_archivo(self.usuario.users)
                    print('Entrada modificada y actualizada en el archivo.')
        # self.ui.esperar_input()

    def hacer_prestamo(self):
        # Función que gestiona los préstamos de libros.
        # Tiene como entrada el Gestor de Biblioteca, que contiene una lista de Libros y una lista de Usuarios.
        # Por convención hemos decidido que sólo se podrán modificar los datos de un usuario en referencia a sus préstamos mediante "hacer_prestamo" y "hacer_devolucion"
        # Y como mucho un usuario podrá tener 3 libros prestados.

        nombre = input('\nIntroduzca el nombre del usuario que solicita el préstamo: ').strip().lower()
        if not nombre:
            self.ui.error('el nombre no puede ser una cadena vacía.')
        else:
            indice = self.usuarios.en_usuarios(nombre.lower())
            if indice < 0:
                self.ui.error('el usuario no se encuentra en la biblioteca.')
            else:
                mod = self.usuarios.hacer_prestamo(indice)
                if not mod:
                    self.ui.error('la entrada del usuario no ha sido modificada.')
                else:
                    self.usuarios.guardar_usuarios()  # Guardamos los cambios

    #FUNCION MODIFICADA 07/11/2025
    def hacer_devolucion(self):

        nombre = input('\nIntroduzca el nombre del usuario que devuelve un libro: ').strip().lower()
        if not nombre:
            self.ui.error('El nombre no puede ser una cadena vacía.')
        else:
            indice = self.usuarios.en_usuarios(nombre)
            if indice < 0:
                self.ui.error('El usuario no se encuentra en la biblioteca.')
            else:
                mod = self.usuarios.hacer_devolucion(indice)
                if not mod:
                    self.ui.error('la entrada del usuario no ha sido modificada.')
                else:
                    self.usuarios.guardar_usuarios()  # Guardamos los cambios


if __name__ == "__main__":
    gestor = GestorBiblioteca()
    gestor.menu_principal()
