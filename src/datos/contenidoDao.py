# Integrantes del Poryecto [Karen Carvo , Johana Ibarra Rodriguez , Eumary Ospina]

from datetime import date

from src.datos.conexion import Conexion
from src.dominio.contenido import Contenido
from src.dominio.documento import Documento
from src.dominio.enlaceweb import EnlaceWeb
from src.dominio.video import Video

class ContenidoDao:
    _SELECCIONAR = "SELECT c.id_contenido, c.titulo, c.fecha, c.autor, c.tipo_contenido, " \
                   "v.url_video, v.duracion, d.tipo_documento, d.tamano_documento, ew.url_enlace " \
                   "FROM Contenidos c " \
                   "LEFT JOIN Videos v ON c.id_contenido = v.id_contenido " \
                   "LEFT JOIN Documentos d ON c.id_contenido = d.id_contenido " \
                   "LEFT JOIN EnlacesWeb ew ON c.id_contenido = ew.id_contenido "

    # --- CAMBIO CRÍTICO AQUÍ: USAR OUTPUT INSERTED.id_contenido ---
    _INSERTAR_CONTENIDO = "INSERT INTO Contenidos(titulo, fecha, autor, tipo_contenido) OUTPUT INSERTED.id_contenido VALUES(?, ?, ?, ?);"
    # -------------------------------------------------------------

    _INSERTAR_VIDEO = "INSERT INTO Videos(id_contenido, url_video, duracion) VALUES(?, ?, ?)"
    _INSERTAR_DOCUMENTO = "INSERT INTO Documentos(id_contenido, tipo_documento, tamano_documento) VALUES(?, ?, ?)"
    _INSERTAR_ENLACEWEB = "INSERT INTO EnlacesWeb(id_contenido, url_enlace) VALUES(?, ?)"

    _ACTUALIZAR_CONTENIDO = "UPDATE Contenidos SET titulo=?, fecha=?, autor=?, tipo_contenido=? WHERE id_contenido=?"
    _ACTUALIZAR_VIDEO = "UPDATE Videos SET url_video=?, duracion=? WHERE id_contenido=?"
    _ACTUALIZAR_DOCUMENTO = "UPDATE Documentos SET tipo_documento=?, tamano_documento=? WHERE id_contenido=?"
    _ACTUALIZAR_ENLACEWEB = "UPDATE EnlacesWeb SET url_enlace=? WHERE id_contenido=?"

    _ELIMINAR_CONTENIDO = "DELETE FROM Contenidos WHERE id_contenido=?"
    _ELIMINAR_VIDEO = "DELETE FROM Videos WHERE id_contenido=?"
    _ELIMINAR_DOCUMENTO = "DELETE FROM Documentos WHERE id_contenido=?"
    _ELIMINAR_ENLACEWEB = "DELETE FROM EnlacesWeb WHERE id_contenido=?"


    @classmethod
    def seleccionar(cls, criterio_busqueda=""):
        conexion = Conexion.obtenerConexion()
        cursor = None
        if conexion is None:
            return []

        try:
            cursor = conexion.cursor()
            sql = cls._SELECCIONAR
            parametros = []

            if criterio_busqueda:
                sql += " WHERE c.titulo LIKE ?"
                parametros.append(f"%{criterio_busqueda}%")

            cursor.execute(sql, tuple(parametros))
            registros = cursor.fetchall()
            contenidos = []
            for r in registros:
                id_contenido, titulo, fecha, autor, tipo_contenido, \
                url_video, duracion, tipo_documento, tamano_documento, url_enlace = r

                if tipo_contenido == "Video":
                    contenidos.append(Video(id_contenido, titulo, fecha, autor, url_video, duracion))
                elif tipo_contenido == "Documento":
                    contenidos.append(Documento(id_contenido, titulo, fecha, autor, tipo_documento, tamano_documento))
                elif tipo_contenido == "Enlace Web":
                    contenidos.append(EnlaceWeb(id_contenido, titulo, fecha, autor, url_enlace))
                else:
                    contenidos.append(Contenido(id_contenido, titulo, fecha, autor)) # Fallback
            return contenidos
        except Exception as e:
            print(f"Error al seleccionar contenidos: {e}")
            return []
        finally:
            Conexion.cerrarCursor(cursor)

    @classmethod
    def seleccionar_por_id(cls, id_contenido):
        conexion = Conexion.obtenerConexion()
        cursor = None
        if conexion is None:
            return None

        try:
            cursor = conexion.cursor()
            sql = cls._SELECCIONAR + " WHERE c.id_contenido = ?"
            cursor.execute(sql, (id_contenido,))
            registro = cursor.fetchone()

            if registro:
                id_cont, titulo, fecha, autor, tipo_contenido, \
                url_video, duracion, tipo_documento, tamano_documento, url_enlace = registro

                if tipo_contenido == "Video":
                    return Video(id_cont, titulo, fecha, autor, url_video, duracion)
                elif tipo_contenido == "Documento":
                    return Documento(id_cont, titulo, fecha, autor, tipo_documento, tamano_documento)
                elif tipo_contenido == "Enlace Web":
                    return EnlaceWeb(id_cont, titulo, fecha, autor, url_enlace)
                else:
                    return Contenido(id_cont, titulo, fecha, autor)
            return None
        except Exception as e:
            print(f"Error al seleccionar contenido por ID: {e}")
            return None
        finally:
            Conexion.cerrarCursor(cursor)

    @classmethod
    def insertar(cls, contenido):
        conexion = Conexion.obtenerConexion()
        cursor = None
        if conexion is None:
            print("DEBUG: No se pudo obtener conexión a la base de datos.")
            return False

        try:
            cursor = conexion.cursor()

            print(f"DEBUG: Intentando insertar Contenido: Titulo='{contenido.titulo}', Fecha='{contenido.fecha}', Autor='{contenido.autor}', Tipo='{contenido.tipo_contenido}'")

            # 1. Ejecutar el INSERT con OUTPUT y obtener el ID directamente
            cursor.execute(cls._INSERTAR_CONTENIDO, (contenido.titulo, contenido.fecha, contenido.autor, contenido.tipo_contenido))

            print(f"DEBUG: Filas afectadas por Contenidos INSERT (con OUTPUT): {cursor.rowcount}") # Debería ser -1 o 1

            # 2. Obtener el ID generado directamente de la ejecución del INSERT
            # fetchone() debería funcionar aquí porque OUTPUT genera un conjunto de resultados
            resultado_id = cursor.fetchone()
            id_generado = resultado_id[0] if resultado_id else None

            print(f"DEBUG: OUTPUT INSERTED.id_contenido devolvió: {id_generado}")

            if id_generado is None:
                print("ADVERTENCIA: id_generado es NULL/None. La inserción principal en Contenidos pudo haber fallado.")

            # Insertar en la tabla específica según el tipo
            if isinstance(contenido, Video):
                print(f"DEBUG: Insertando Video con id_generado={id_generado}, URL='{contenido.url_video}', Duracion='{contenido.duracion}'")
                cursor.execute(cls._INSERTAR_VIDEO, (id_generado, contenido.url_video, contenido.duracion))
            elif isinstance(contenido, Documento):
                print(f"DEBUG: Insertando Documento con id_generado={id_generado}, Tipo='{contenido.tipo_documento}', Tamaño='{contenido.tamano_documento}'")
                cursor.execute(cls._INSERTAR_DOCUMENTO, (id_generado, contenido.tipo_documento, contenido.tamano_documento))
            elif isinstance(contenido, EnlaceWeb):
                print(f"DEBUG: Insertando Enlace Web con id_generado={id_generado}, URL='{contenido.url_enlace}'")
                cursor.execute(cls._INSERTAR_ENLACEWEB, (id_generado, contenido.url_enlace))

            conexion.commit()
            print("DEBUG: Transacción completada y confirmada (commit).")
            return True
        except Exception as e:
            print(f"DEBUG: Excepción capturada en insertar: {e}")
            print(f"Error al insertar contenido: {e}")
            if conexion:
                conexion.rollback()
                print("DEBUG: Transacción revertida (rollback).")
            return False
        finally:
            Conexion.cerrarCursor(cursor)

    @classmethod
    def actualizar(cls, contenido):
        conexion = Conexion.obtenerConexion()
        cursor = None
        if conexion is None:
            return False

        try:
            cursor = conexion.cursor()
            # Actualizar tabla Contenidos
            cursor.execute(cls._ACTUALIZAR_CONTENIDO,
                           (contenido.titulo, contenido.fecha, contenido.autor,
                            contenido.tipo_contenido, contenido.id_contenido))

            # Actualizar tabla específica
            if isinstance(contenido, Video):
                cursor.execute(cls._ACTUALIZAR_VIDEO, (contenido.url_video, contenido.duracion, contenido.id_contenido))
            elif isinstance(contenido, Documento):
                cursor.execute(cls._ACTUALIZAR_DOCUMENTO,
                               (contenido.tipo_documento, contenido.tamano_documento, contenido.id_contenido))
            elif isinstance(contenido, EnlaceWeb):
                cursor.execute(cls._ACTUALIZAR_ENLACEWEB, (contenido.url_enlace, contenido.id_contenido))

            conexion.commit()
            return True
        except Exception as e:
            print(f"Error al actualizar contenido: {e}")
            if conexion:
                conexion.rollback()
            return False
        finally:
            Conexion.cerrarCursor(cursor)

    @classmethod
    def eliminar(cls, id_contenido):
        conexion = Conexion.obtenerConexion()
        cursor = None
        if conexion is None:
            return False

        try:
            cursor = conexion.cursor()
            # Primero eliminar de las tablas hijas para evitar problemas de FK
            cursor.execute(cls._ELIMINAR_VIDEO, (id_contenido,))
            cursor.execute(cls._ELIMINAR_DOCUMENTO, (id_contenido,))
            cursor.execute(cls._ELIMINAR_ENLACEWEB, (id_contenido,))

            # Luego eliminar de la tabla padre
            cursor.execute(cls._ELIMINAR_CONTENIDO, (id_contenido,))

            conexion.commit()
            return True
        except Exception as e:
            print(f"Error al eliminar contenido: {e}")
            if conexion:
                conexion.rollback()
            return False
        finally:
            Conexion.cerrarCursor(cursor)
