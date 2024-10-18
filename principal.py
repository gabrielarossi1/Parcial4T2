import random
import pickle
import os.path
from modulo import *


def menu():
    print('Menú de opciones: ')
    print('1. Cargar arreglo')
    print('2. Mostrar arreglo')
    print('3. Cargar y mostrar matriz')
    print('4. Generar archivo binario')
    print('5. Mostrar archivo binario')
    print('6. Salir')


def validar_n():
    n = int(input('Ingrese una cantidad mayor a 0: '))
    while n <= 0:
        n = int(input('ERROR, ingrese un numero mayor a 0'))
    return n

#------------------Punto 1
def cargar_en_orden(vec, libro):
    n = len(vec)
    izq = 0
    der = n - 1
    posicion = n

    while izq <= der:
        valor_central = (izq + der) // 2
        if libro.idioma < vec[valor_central].idioma:
            posicion = valor_central
            break
        elif libro.idioma < vec[valor_central].idioma:
            der = valor_central + 1
        else:
            izq = valor_central + 1
    if izq > der:
        posicion = izq
    vec[posicion:posicion] = [libro]


#-----------------punto 2
def cargar_vector(vec):
    n = validar_n()

    for i in range(n):
        isbn = random.randint(1000000000000, 9999999999999)
        titulo = 'Titulo' + str(random.randint(1, 1000))
        autor = 'Autor' + str(random.randint(1, 1000))
        idioma = random.randint(1, 5)
        precio = random.randint(100, 10000)

        libro = Libro(isbn, titulo, autor, idioma, precio)

        cargar_en_orden(vec, libro)


def mostrar(vec):
    for libro in vec:
        if libro.idioma == 1:
            idioma_str = 'Español'
        elif libro.idioma == 2:
            idioma_str = 'Inglés'
        elif libro.idioma == 3:
            idioma_str = 'Portugués'
        elif libro.idioma == 4:
            idioma_str = 'Francés'
        elif libro.idioma == 5:
            idioma_str = 'Italiano'

        print('Código ISBN: ' + str(libro.isbn) + ' - Título: ' + libro.titulo + \
              ' - Autor: ' + libro.autor + ' - Idioma: ' + idioma_str + \
              ' - Precio: ' + str(libro.precio))


#--------------------Punto 3
def buscar_libro_por_isbn(vec):
    isbn_a_buscar = int(input('Ingrese el ISBN del libro que desea buscar: '))
    encontrado = False

    for libro in vec:
        if libro.isbn == isbn_a_buscar:
            encontrado = True
            print('Datos del libro encontrado: ')
            print(libro)

            #verifico que el idioma sea frances
            if libro.idioma == 4:
                print('\nEl libro esta en francés y tiene un descuento del 22%.')
                precio_original = libro.precio
                nuevo_precio = precio_original * 0.78
                print('Precio original: ', precio_original)
                print('Nuevo precio: ', nuevo_precio)
                #actualizo el precio del libro
                libro.precio = nuevo_precio
            break
    if not encontrado:
        print('No contamos con el libro ', str(isbn_a_buscar), 'pero no deje de visitar nuestra seccion de oferta')


#------------------punto 4
def generar_archivo_binario(vec):
    autor_a_buscar = input('Ingrese el autor que desea buscar: ')
    precio_maximo = float(input('Ingrese el precio máximo: '))

    #filtrar libros por autor y precio
    libros_filtrados = []
    for libro in vec:
        if libro.autor == autor_a_buscar and libro.precio <= precio_maximo:
            libros_filtrados.append(libro)

    if libros_filtrados:
        archivo = open('libros_filtrados.dat', 'wb')
        for libro in libros_filtrados:
            pickle.dump(libro, archivo)

        archivo.close()
        print('Archivo binario generado con éxito!')
    else:
        print('No se encontraron libros del autor: ' + autor_a_buscar + ' con un precio menor o igual a: ' + str(precio_maximo) + '.')


#-----------Punto 5
def mostrar_archivo_binario(archivo):
    if not os.path.exists(archivo):
        print('El archivo no existe')
    else:
        memoria = open(archivo, 'rb')
        contador_libros = 0

        tamaño_del_archivo = os.path.getsize(archivo)
        while memoria.tell() < tamaño_del_archivo:
            libro = pickle.load(memoria)
            contador_libros += 1

        memoria.close()

        if contador_libros != 0:
            print('La cantidad de libros es: ', contador_libros)



def main():
    vec = []
    archivo = 'libros_filtrados.dat'

    op = 1
    while op != 6:
        menu()
        op = int(input('Ingrese una opcion: '))
        if op == 1:
            cargar_vector(vec)
        elif op == 2:
            if vec == []:
                print('Tiene que cargar un vector primero')
            else:
                mostrar(vec)
        elif op == 3:
            if vec == []:
                print('Tiene que cargar un vector primero')
            else:
                buscar_libro_por_isbn(vec)
        elif op == 4:
            if vec == []:
                print('Tiene que cargar un vector primero')
            else:
                generar_archivo_binario(vec)
        elif op == 5:
            mostrar_archivo_binario(archivo)


if __name__ == '__main__':
    main()