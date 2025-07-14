from src.dominio.contenido import Contenido

class EnlaceWeb(Contenido):
    def __init__(self, id_contenido, titulo, fecha, autor, url_enlace):
        super().__init__(id_contenido, titulo, fecha, autor, tipo_contenido="Enlace Web")
        self._url_enlace = url_enlace

    @property
    def url_enlace(self):
        return self._url_enlace

    @url_enlace.setter
    def url_enlace(self, url_enlace):
        self._url_enlace = url_enlace

    def __str__(self):
        return f"EnlaceWeb[ID: {self.id_contenido}, Título: {self.titulo}, Fecha: {self.fecha}, Autor: {self.autor}, URL: {self.url_enlace}]"