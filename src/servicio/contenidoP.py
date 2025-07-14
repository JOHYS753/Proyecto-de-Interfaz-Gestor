from PySide6.QtWidgets import QMainWindow, QMessageBox, QTableWidgetItem, QHeaderView, QTableWidget
from PySide6.QtCore import QDate
from src.UI.vtnGestor import Ui_vtnGestor
from src.datos.contenidoDao import ContenidoDao
from src.dominio.documento import Documento
from src.dominio.enlaceweb import EnlaceWeb
from src.dominio.video import Video


class ContenidoServicio(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_vtnGestor()
        self.ui.setupUi(self)
        self.contenido_seleccionado = None

        self.configurar_eventos()
        self.cargar_contenidos_en_tabla()
        self.actualizar_visibilidad_detalles()

    def configurar_eventos(self):
        self.ui.btn_guardar.clicked.connect(self.guardar_contenido)
        self.ui.btn_limpiar.clicked.connect(self.limpiar_campos)
        self.ui.btn_cancelar_edicion.clicked.connect(self.cancelar_edicion)
        self.ui.cmb_tipo_contenido.currentIndexChanged.connect(self.actualizar_visibilidad_detalles)

        self.ui.btn_buscar.clicked.connect(self.cargar_contenidos_en_tabla)
        self.ui.btn_editar_seleccionado.clicked.connect(self.editar_contenido)
        self.ui.btn_eliminar_seleccionado.clicked.connect(self.eliminar_contenido)
        self.ui.tableWidget_contenidos.itemSelectionChanged.connect(self.actualizar_botones_seleccion)
        self.ui.btn_mostrar_todo.clicked.connect(self.cargar_contenidos_en_tabla)
        self.ui.txt_buscar.returnPressed.connect(self.cargar_contenidos_en_tabla)


    def actualizar_visibilidad_detalles(self):
        tipo_seleccionado = self.ui.cmb_tipo_contenido.currentText()

        self.ui.groupBox_detalles_especificos.setVisible(True)

        self.ui.lbl_url_video.setVisible(False)
        self.ui.txt_url_video.setVisible(False)
        self.ui.lbl_duracion.setVisible(False)
        self.ui.txt_duracion.setVisible(False)

        self.ui.lbl_tipo_documento.setVisible(False)
        self.ui.txt_tipo_documento.setVisible(False)
        self.ui.lbl_tamano_documento.setVisible(False)
        self.ui.txt_tamano_documento.setVisible(False)

        self.ui.lbl_url_enlace.setVisible(False)
        self.ui.txt_url_enlace.setVisible(False)

        if tipo_seleccionado == "Video":
            self.ui.lbl_url_video.setVisible(True)
            self.ui.txt_url_video.setVisible(True)
            self.ui.lbl_duracion.setVisible(True)
            self.ui.txt_duracion.setVisible(True)

        elif tipo_seleccionado == "Documento":
            self.ui.lbl_tipo_documento.setVisible(True)
            self.ui.txt_tipo_documento.setVisible(True)
            self.ui.lbl_tamano_documento.setVisible(True)
            self.ui.txt_tamano_documento.setVisible(True)

        elif tipo_seleccionado == "Enlace Web":
            self.ui.lbl_url_enlace.setVisible(True)
            self.ui.txt_url_enlace.setVisible(True)


    def limpiar_campos(self):
        self.ui.txt_titulo.clear()
        self.ui.date_fecha.setDate(QDate.currentDate())
        self.ui.txt_autor.clear()
        self.ui.cmb_tipo_contenido.setCurrentIndex(0)

        self.ui.txt_url_video.clear()
        self.ui.txt_duracion.clear()
        self.ui.txt_tipo_documento.clear()
        self.ui.txt_tamano_documento.clear()
        self.ui.txt_url_enlace.clear()

        self.ui.btn_guardar.setText("Guardar")
        self.ui.btn_cancelar_edicion.setVisible(False)
        self.contenido_seleccionado = None
        self.ui.tabWidget.setCurrentIndex(0)
        self.actualizar_visibilidad_detalles()


    def guardar_contenido(self):
        titulo = self.ui.txt_titulo.text().strip()
        fecha = self.ui.date_fecha.date().toPython()
        autor = self.ui.txt_autor.text().strip()

        if not titulo or len(titulo) < 2:
            self.mostrar_mensaje("Validación de Entrada", "El Título es obligatorio y debe tener al menos 2 caracteres.", "warning")
            return
        if not autor or len(autor) < 2:
            self.mostrar_mensaje("Validación de Entrada", "El Autor es obligatorio y debe tener al menos 2 caracteres.", "warning")
            return

        tipo_contenido = self.ui.cmb_tipo_contenido.currentText()
        contenido = None

        if tipo_contenido == "Video":
            url_video = self.ui.txt_url_video.text().strip()
            duracion_str = self.ui.txt_duracion.text().strip()

            if not url_video:
                self.mostrar_mensaje("Validación de Entrada", "La URL del video es obligatoria.", "warning")
                return
            try:
                duracion = float(duracion_str) if duracion_str else 0.0
                if duracion <= 0:
                    self.mostrar_mensaje("Validación de Entrada", "La duración del video debe ser un número positivo.", "warning")
                    return
            except ValueError:
                self.mostrar_mensaje("Error de Entrada", "La duración del video debe ser un número válido.", "warning")
                return

            contenido = Video(None, titulo, fecha, autor, url_video, duracion)

        elif tipo_contenido == "Documento":
            tipo_documento = self.ui.txt_tipo_documento.text().strip()
            tamano_documento_str = self.ui.txt_tamano_documento.text().strip()

            if not tipo_documento or len(tipo_documento) < 2:
                self.mostrar_mensaje("Validación de Entrada", "El Tipo de Documento es obligatorio y debe tener al menos 2 caracteres.", "warning")
                return
            try:
                tamano_documento = float(tamano_documento_str) if tamano_documento_str else 0.0
                if tamano_documento <= 0:
                     self.mostrar_mensaje("Validación de Entrada", "El Tamaño del documento debe ser un número positivo.", "warning")
                     return
            except ValueError:
                self.mostrar_mensaje("Error de Entrada", "El tamaño del documento debe ser un número válido.", "warning")
                return

            contenido = Documento(None, titulo, fecha, autor, tipo_documento, tamano_documento)

        elif tipo_contenido == "Enlace Web":
            url_enlace = self.ui.txt_url_enlace.text().strip()
            if not url_enlace:
                self.mostrar_mensaje("Validación de Entrada", "La URL del enlace web es obligatoria.", "warning")
                return

            contenido = EnlaceWeb(None, titulo, fecha, autor, url_enlace)
        else:
            self.mostrar_mensaje("Tipo de Contenido Inválido", "Seleccione un tipo de contenido válido.", "warning")
            return

        if self.contenido_seleccionado:
            contenido.id_contenido = self.contenido_seleccionado.id_contenido
            if ContenidoDao.actualizar(contenido):
                self.mostrar_mensaje("Éxito", "Contenido actualizado exitosamente.", "information")
            else:
                self.mostrar_mensaje("Error", "No se pudo actualizar el contenido.", "critical")
        else:
            if ContenidoDao.insertar(contenido):
                self.mostrar_mensaje("Éxito", "Contenido guardado exitosamente.", "information")
            else:
                self.mostrar_mensaje("Error", "No se pudo guardar el contenido.", "critical")

        self.limpiar_campos()
        self.cargar_contenidos_en_tabla()

    def cargar_contenidos_en_tabla(self):
        criterio_busqueda = self.ui.txt_buscar.text().strip()
        contenidos = ContenidoDao.seleccionar(criterio_busqueda)
        self.ui.tableWidget_contenidos.setRowCount(0)

        for row_num, contenido in enumerate(contenidos):
            self.ui.tableWidget_contenidos.insertRow(row_num)
            self.ui.tableWidget_contenidos.setItem(row_num, 0, QTableWidgetItem(str(contenido.id_contenido)))
            self.ui.tableWidget_contenidos.setItem(row_num, 1, QTableWidgetItem(contenido.titulo))
            self.ui.tableWidget_contenidos.setItem(row_num, 2, QTableWidgetItem(str(contenido.fecha)))
            self.ui.tableWidget_contenidos.setItem(row_num, 3, QTableWidgetItem(contenido.autor))

            tipo = ""
            detalles_especificos = ""
            if isinstance(contenido, Video):
                tipo = "Video"
                detalles_especificos = f"URL: {contenido.url_video}, Duración: {contenido.duracion} min"
            elif isinstance(contenido, Documento):
                tipo = "Documento"
                detalles_especificos = f"Tipo: {contenido.tipo_documento}, Tamaño: {contenido.tamano_documento} KB"
            elif isinstance(contenido, EnlaceWeb):
                tipo = "Enlace Web"
                detalles_especificos = f"URL: {contenido.url_enlace}"

            self.ui.tableWidget_contenidos.setItem(row_num, 4, QTableWidgetItem(tipo))
            self.ui.tableWidget_contenidos.setItem(row_num, 5, QTableWidgetItem(detalles_especificos))

        self.ui.tableWidget_contenidos.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.ui.tableWidget_contenidos.verticalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.actualizar_botones_seleccion()

    def editar_contenido(self):
        selected_items = self.ui.tableWidget_contenidos.selectedItems()
        if not selected_items:
            self.mostrar_mensaje("Error de Selección", "Seleccione un contenido de la tabla para editar.", "warning")
            return

        row = selected_items[0].row()
        id_contenido = int(self.ui.tableWidget_contenidos.item(row, 0).text())

        contenido_completo = ContenidoDao.seleccionar_por_id(id_contenido)
        if not contenido_completo:
            self.mostrar_mensaje("Error", "No se encontró el contenido para editar.", "critical")
            return

        self.contenido_seleccionado = contenido_completo

        self.ui.txt_titulo.setText(contenido_completo.titulo)
        self.ui.date_fecha.setDate(
            QDate(contenido_completo.fecha.year, contenido_completo.fecha.month, contenido_completo.fecha.day))
        self.ui.txt_autor.setText(contenido_completo.autor)

        tipo_str = ""
        if isinstance(contenido_completo, Video):
            tipo_str = "Video"
            self.ui.txt_url_video.setText(contenido_completo.url_video)
            self.ui.txt_duracion.setText(str(contenido_completo.duracion))
        elif isinstance(contenido_completo, Documento):
            tipo_str = "Documento"
            self.ui.txt_tipo_documento.setText(contenido_completo.tipo_documento)
            self.ui.txt_tamano_documento.setText(
                str(contenido_completo.tamano_documento))
        elif isinstance(contenido_completo, EnlaceWeb):
            tipo_str = "Enlace Web"
            self.ui.txt_url_enlace.setText(contenido_completo.url_enlace)

        index = self.ui.cmb_tipo_contenido.findText(tipo_str)
        if index != -1:
            self.ui.cmb_tipo_contenido.setCurrentIndex(index)

        self.ui.btn_guardar.setText("Actualizar")
        self.ui.btn_cancelar_edicion.setVisible(True)
        self.ui.tabWidget.setCurrentIndex(1)

    def mostrar_mensaje(self, titulo, mensaje, icono):
        msg_box = QMessageBox()
        msg_box.setWindowTitle(titulo)
        msg_box.setText(mensaje)
        if icono == "information":
            msg_box.setIcon(QMessageBox.Information)
        elif icono == "warning":
            msg_box.setIcon(QMessageBox.Warning)
        elif icono == "critical":
            msg_box.setIcon(QMessageBox.Critical)
        msg_box.exec()

    def actualizar_botones_seleccion(self):
        hay_seleccion = bool(self.ui.tableWidget_contenidos.selectedItems())
        self.ui.btn_editar_seleccionado.setEnabled(hay_seleccion)
        self.ui.btn_eliminar_seleccionado.setEnabled(hay_seleccion)

    def cancelar_edicion(self):
        self.limpiar_campos()
        self.contenido_seleccionado = None
        self.ui.btn_guardar.setText("Guardar")
        self.ui.btn_cancelar_edicion.setVisible(False)
        self.ui.tabWidget.setCurrentIndex(0)

    def eliminar_contenido(self):
        selected_items = self.ui.tableWidget_contenidos.selectedItems()
        if not selected_items:
            self.mostrar_mensaje("Error de Selección", "Seleccione un contenido de la tabla para eliminar.", "warning")
            return

        row = selected_items[0].row()
        id_contenido = int(self.ui.tableWidget_contenidos.item(row, 0).text())
        titulo_contenido = self.ui.tableWidget_contenidos.item(row, 1).text()

        reply = QMessageBox.question(self, 'Confirmar Eliminación', \
                                     f"¿Está seguro de que desea eliminar el contenido '{titulo_contenido}' (ID: {id_contenido})?", \
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            if ContenidoDao.eliminar(id_contenido):
                self.mostrar_mensaje("Éxito", "Contenido eliminado exitosamente.", "information")
                self.cargar_contenidos_en_tabla()
            else:
                self.mostrar_mensaje("Error", "No se pudo eliminar el contenido.", "critical")
