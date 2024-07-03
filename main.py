'''
Gestión de Biblioteca: Desarrolla una aplicación en Python que permita gestionar una biblioteca. La aplicación debe
cumplir con las siguientes funcionalidades que debe proveer al usuario través de un menú de opciones:
Registrar libros: Solicita al usuario ingresar el título, autor y género de un libro. Almacena los datos en una colección,
por ejemplo, en un diccionario.
Buscar libros por autor: Permite al usuario buscar libros por el nombre del autor.
Mostrar lista de libros: Muestra en pantalla la lista completa de libros registrados.
Salir del programa.

Recuerda: implementar cada funcionalidad en funciones separadas y permitir que el programa funcione hasta que el
usuario decida salir. Que los datos de la aplicación persistan entre distintas ejecuciones de este, almacenando y
recuperando sus datos en algún tipo de archivo de texto. Y además que use al menos una librería estándar de
Python.

'''


'''
1) Menu principal con opciones
2) Registrar libros
    ingresar: titulo, autor, genero
3) BUscar libros por autor
4) mostrar libros
'''


def cargar_biblioteca():
    return

def guardar_biblioteca():
    return

def registrar_libro(titulo, autor, genero):
    if titulo in biblioteca.keys():
        print('Ya existe ese libro en los registros.')
        return False
    biblioteca[titulo] = {'Autor':autor, 'Género':genero}
    return True

def buscar_libro():
    return


# En este diccionario se guardarán todos los libros usando el título como KEY y el VALUE será otro diccionario con los KEYs autor y genero
biblioteca = {}

# Biblioteca con algunos ejemplos para ir debugeando el código
biblioteca = {'Papelucho':{'Autor':'Marcela Paz', 'Género':'Literatura infantil'}, 'El Quijote':{'Autor':'Miguel de Cervantes', 'Género':'Novelas de caballería'}, 'Cien años de soledad':{'Autor':'Gabriel García Márquez', 'Género':'Realismo mágico'}}



# Bienvenida e Inicializacion
print('saludo')
cargar_biblioteca()


# Menu (loop principal)
while True:
    print('\nMenu:')
    menu = input()
    if menu == '1': # Registrar libro
        pass

    elif menu == '2': # Buscar libro
        pass

    elif menu == '3': # Listar libros
        print('\nBiblioteca:')
        for key in biblioteca.keys():
            print(f'  > {key}')
        input('\nPresione [Enter] para continuar...')

    elif menu == '4': # Salir
        print('Finalizando biblioteca, por favor espere un momento.')
        break

    else:
        print('Opción no válida.\nIngrese un número según la opción que desee.')




# Despedida / Cierre
guardar_biblioteca()
print('despedida')