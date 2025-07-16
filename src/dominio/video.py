# Integrantes del Poryecto [Karen Carvo , Johana Ibarra Rodriguez , Eumary Ospina]
from src.dominio.contenido import Contenido

class Video(Contenido):
    def __init__(self, id_contenido, titulo, fecha, autor, url_video, duracion):
        super().__init__(id_contenido, titulo, fecha, autor, tipo_contenido="Video")
        self._url_video = url_video
        self._duracion = duracion

    @property
    def url_video(self):
        return self._url_video

    @url_video.setter
    def url_video(self, url_video):
        self._url_video = url_video

    @property
    def duracion(self):
        return self._duracion

    @duracion.setter
    def duracion(self, duracion):
        self._duracion = duracion

    def __str__(self):
        return f"Video[ID: {self.id_contenido}, Título: {self.titulo}, Fecha: {self.fecha}, Autor: {self.autor}, URL: {self.url_video}, Duración: {self.duracion}]"
