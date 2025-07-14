from src.dominio.contenido import Contenido

class Documento(Contenido):
    def __init__(self, id_contenido, titulo, fecha, autor, tipo_documento, tamano_documento):
        super().__init__(id_contenido, titulo, fecha, autor, tipo_contenido="Documento")
        self._tipo_documento = tipo_documento
        self._tamano_documento = tamano_documento

    @property
    def tipo_documento(self):
        return self._tipo_documento

    @tipo_documento.setter
    def tipo_documento(self, tipo_documento):
        self._tipo_documento = tipo_documento

    @property
    def tamano_documento(self):
        return self._tamano_documento

    @tamano_documento.setter
    def tamano_documento(self, tamano_documento):
        self._tamano_documento = tamano_documento

    def __str__(self):
        return f"Documento[ID: {self.id_contenido}, Título: {self.titulo}, Fecha: {self.fecha}, Autor: {self.autor}, Tipo Doc: {self.tipo_documento}, Tamaño: {self.tamano_documento}]"