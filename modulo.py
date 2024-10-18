class Libro:
    def __init__(self, isbn, titulo, autor, idioma, precio):
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor
        self.idioma = idioma
        self.precio = precio

    def __str__(self):
        return 'Código ISBN: ' + str(self.isbn) + ' - Titulo: ' + str(self.titulo) + \
            ' - Autor: ' + str(self.autor) + ' - Idioma: ' + str(self.idioma) + \
            ' - Precio: ' + str(self.precio)

