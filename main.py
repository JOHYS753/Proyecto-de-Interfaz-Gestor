#Integrantes del Poryecto [Karen Carvo , Johana Ibarra Rodriguez , Eumary Ospina]
import sys
import os # Importar el módulo os
from PySide6.QtWidgets import QApplication

import pyodbc

# IMPORTANTE: Asegúrate de que esta línea es 'from src.servicio.contenido import ContenidoServicio'
# y no 'PersonaServicio'
from src.servicio.contenidoP import ContenidoServicio

# Esta parte sigue siendo una buena práctica general, aunque para 'conexion' ya no sea estrictamente
# necesaria si lo moviste a 'src/datos'. Mantenla para robustez en otros imports.
project_root = os.path.dirname(os.path.abspath(__file__))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    try:
        if hasattr(pyodbc, 'pooling') and hasattr(pyodbc.pooling, 'cleanup') and callable(pyodbc.pooling.cleanup):
            app.aboutToQuit.connect(pyodbc.pooling.cleanup)
        else:
            print("Advertencia: pyodbc.pooling.cleanup no está disponible o no es una función. La limpieza automática de la conexión podría no ocurrir.")
    except Exception as e:
        print(f"Error al intentar conectar pyodbc.pooling.cleanup: {e}")

    # INSTANCIAR ContenidoServicio
    vtn_gestor = ContenidoServicio()
    vtn_gestor.show()
    sys.exit(app.exec())
