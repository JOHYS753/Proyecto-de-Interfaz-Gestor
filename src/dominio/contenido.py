# Integrantes del Poryecto [Karen Carvo , Johana Ibarra Rodriguez , Eumary Ospina]
class Contenido:
    def __init__(self, id_contenido, titulo, fecha, autor, tipo_contenido=None):
        self._id_contenido = id_contenido
        self._titulo = titulo
        self._fecha = fecha
        self._autor = autor
        self._tipo_contenido = tipo_contenido

    @property
    def id_contenido(self):
        return self._id_contenido

    @id_contenido.setter
    def id_contenido(self, id_contenido):
        self._id_contenido = id_contenido

    @property
    def titulo(self):
        return self._titulo

    @titulo.setter
    def titulo(self, titulo):
        self._titulo = titulo

    @property
    def fecha(self):
        return self._fecha

    @fecha.setter
    def fecha(self, fecha):
        self._fecha = fecha

    @property
    def autor(self):
        return self._autor

    @autor.setter
    def autor(self, autor):
        self._autor = autor

    @property
    def tipo_contenido(self):
        return self._tipo_contenido

    @tipo_contenido.setter
    def tipo_contenido(self, tipo_contenido):
        self._tipo_contenido = tipo_contenido

    def __str__(self):
        return f"ID: {self._id_contenido}, Título: {self._titulo}, Fecha: {self._fecha}, Autor: {self._autor}, Tipo: {self._tipo_contenido}"
