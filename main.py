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
import csv

def cargar_biblioteca():
    try:
        with open('Biblioteca.csv', 'rt', encoding='utf-8', newline='') as archivo:
            lector = csv.reader(archivo, delimiter=';')
            for row in lector:
                biblioteca[row[0]] = {'Autor/a':row[1], 'Género':row[2]}
    except:
        print('No se ha podido cargar la Biblioteca correctamente.')

def guardar_biblioteca():
    try:
        with open('Biblioteca.csv', 'wt', encoding='utf-8', newline='') as archivo:
            escritor = csv.writer(archivo, delimiter=';')
            for libro, param in biblioteca.items():
                escritor.writerow([libro, param['Autor/a'], param['Género']])
        print('Biblioteca se ha guardado con éxito.')
    except:
        print('Se ha encontrado un error al intentar guardar la biblioteca.')

def registrar_libro(titulo, autor, genero):
    if titulo in biblioteca.keys():
        print('Ya existe ese libro en los registros.')
        return False
    biblioteca[titulo] = {'Autor/a':autor, 'Género':genero}
    return True

def buscar_libro_autor(autor):
    busqueda = []
    for titulo in biblioteca.keys():
        if biblioteca[titulo]['Autor/a'].lower() == autor.lower():
            busqueda.append(titulo)
    count = 0
    for libro in busqueda:
        count += 1
    if count == 0:
        return [f'No se encontraron libros escritos por: {autor}']
    return busqueda


# En este diccionario se guardarán todos los libros usando el título como KEY y el VALUE será otro diccionario con los KEYs autor y genero
biblioteca = {}


# Bienvenida e Inicializacion
print('¡Bienvenido/a a la Biblioteca!')
cargar_biblioteca()


# Menu (loop principal)
while True:
    print('\nBiblioteca:', '1) Registrar libro', '2) Buscar libro por autor', '3) Listar libros', '4) Salir', sep='\n')
    menu = input()

    if menu == '1': # Registrar libro
        print('\nPara registrar un libro, ingrese los siguientes datos:')
        reg_titulo = input('Título: ')
        reg_autor = input('Autor/a: ')
        reg_genero = input('Género: ')
        if registrar_libro(reg_titulo, reg_autor, reg_genero):
            print('\nSe ha registrado el libro correctamente.')
            input('Presione [Enter] para continuar...')
        else:
            print('\nNo se ha podido registrar el libro.')
            input('Presione [Enter] para continuar...')

    elif menu == '2': # Buscar libro
        autor = input('¿Quién es el/la autor/a del libro que busca?\n\n')
        for libro in buscar_libro_autor(autor):
            print(f'  > {libro}')
        input('\nPresione [Enter] para continuar...')

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
print('\nGracias por usa la Biblioteca.')
print('¡Hasta luego!')