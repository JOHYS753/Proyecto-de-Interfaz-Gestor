# Integrantes del Poryecto [Karen Carvo , Johana Ibarra Rodriguez , Eumary Ospina]
import pyodbc as bd
import sys

class Conexion:
    _SERVIDOR = 'johyspa'       # El nombre de tu máquina
    _INSTANCIA = ''             # ¡Importante! Deja esto vacío para la instancia predeterminada (MSSQLSERVER)
    _BBDD = 'GestionContenidoDB' # Asegúrate de que esta es la base de datos correcta.
    _USUARIO = 'Johana'
    _PASSWORD = '0123456789'  # La contraseña que te funcionó en SSMS
    _conexion = None
    _cursor = None

    @classmethod
    def obtenerConexion(cls):
        if cls._conexion is None:
            try:
                # La cadena de conexión no debe incluir "\\{cls._INSTANCIA}" si _INSTANCIA es vacío
                # Solo usa SERVER={cls._SERVIDOR} para la instancia predeterminada
                connection_string = (
                    f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={cls._SERVIDOR};'
                    f'DATABASE={cls._BBDD};UID={cls._USUARIO};PWD={cls._PASSWORD};'
                    f'TrustServerCertificate=yes'
                )
                cls._conexion = bd.connect(connection_string)
                print("Conexión exitosa a la base de datos.")
                return cls._conexion
            except Exception as e:
                print(f"Error al conectar a la base de datos: {e}")
                cls._conexion = None
                return None
        else:
            return cls._conexion

    @classmethod
    def obtenerCursor(cls):
        if cls._cursor is None:
            try:
                conn = cls.obtenerConexion()
                if conn:
                    cls._cursor = conn.cursor()
                    return cls._cursor
                else:
                    print("Error: No se pudo obtener la conexión para crear el cursor.")
                    return None
            except Exception as e:
                print(f"Error al obtener el cursor: {e}")
                cls._cursor = None
                return None
        else:
            return cls._cursor

    @classmethod
    def cerrarConexion(cls):
        if cls._conexion:
            try:
                cls._conexion.close()
                cls._conexion = None
                cls._cursor = None
                print("Conexión a la base de datos cerrada.")
            except Exception as e:
                print(f"Error al cerrar la conexión: {e}")

    @classmethod
    def cerrarCursor(cls, cursor):
        if cursor:
            try:
                cursor.close()
            except Exception as e:
                print(f"Error al cerrar el cursor: {e}")

if __name__ == '__main__':
    print("Iniciando prueba de conexión con la instancia predeterminada...")
    try:
        conn = Conexion.obtenerConexion()
        if conn:
            cursor = Conexion.obtenerCursor()
            if cursor:
                print("Conexión y cursor obtenidos exitosamente.")
                cursor.execute("SELECT GETDATE()")
                fecha_db = cursor.fetchone()
                print(f"Fecha actual de la DB: {fecha_db[0]}")
                Conexion.cerrarConexion()
                print("Prueba de conexión finalizada.")
            else:
                print("No se pudo obtener el cursor.")
        else:
            print("No se pudo obtener la conexión.")
    except Exception as e:
        print(f"Error general en la prueba de conexión: {e}")
