# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'vtnGestor.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QFormLayout,
    QGroupBox, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QSpacerItem, QStatusBar, QTabWidget,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_vtnGestor(object):
    def setupUi(self, vtnGestor):
        if not vtnGestor.objectName():
            vtnGestor.setObjectName(u"vtnGestor")
        vtnGestor.resize(800, 600)
        self.centralwidget = QWidget(vtnGestor)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab_registro = QWidget()
        self.tab_registro.setObjectName(u"tab_registro")
        self.verticalLayout_2 = QVBoxLayout(self.tab_registro)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.groupBox_datos_contenido = QGroupBox(self.tab_registro)
        self.groupBox_datos_contenido.setObjectName(u"groupBox_datos_contenido")
        self.formLayout = QFormLayout(self.groupBox_datos_contenido)
        self.formLayout.setObjectName(u"formLayout")
        self.lbl_id = QLabel(self.groupBox_datos_contenido)
        self.lbl_id.setObjectName(u"lbl_id")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.lbl_id)

        self.txt_id = QLineEdit(self.groupBox_datos_contenido)
        self.txt_id.setObjectName(u"txt_id")
        self.txt_id.setReadOnly(True)

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.txt_id)

        self.lbl_titulo = QLabel(self.groupBox_datos_contenido)
        self.lbl_titulo.setObjectName(u"lbl_titulo")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.lbl_titulo)

        self.txt_titulo = QLineEdit(self.groupBox_datos_contenido)
        self.txt_titulo.setObjectName(u"txt_titulo")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.txt_titulo)

        self.lbl_fecha = QLabel(self.groupBox_datos_contenido)
        self.lbl_fecha.setObjectName(u"lbl_fecha")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.lbl_fecha)

        self.date_fecha = QDateEdit(self.groupBox_datos_contenido)
        self.date_fecha.setObjectName(u"date_fecha")
        self.date_fecha.setCalendarPopup(True)

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.date_fecha)

        self.lbl_autor = QLabel(self.groupBox_datos_contenido)
        self.lbl_autor.setObjectName(u"lbl_autor")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.lbl_autor)

        self.txt_autor = QLineEdit(self.groupBox_datos_contenido)
        self.txt_autor.setObjectName(u"txt_autor")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.txt_autor)

        self.lbl_tipo_contenido = QLabel(self.groupBox_datos_contenido)
        self.lbl_tipo_contenido.setObjectName(u"lbl_tipo_contenido")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.lbl_tipo_contenido)

        self.cmb_tipo_contenido = QComboBox(self.groupBox_datos_contenido)
        self.cmb_tipo_contenido.addItem("")
        self.cmb_tipo_contenido.addItem("")
        self.cmb_tipo_contenido.addItem("")
        self.cmb_tipo_contenido.setObjectName(u"cmb_tipo_contenido")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.cmb_tipo_contenido)

        self.groupBox_detalles_especificos = QGroupBox(self.groupBox_datos_contenido)
        self.groupBox_detalles_especificos.setObjectName(u"groupBox_detalles_especificos")
        self.formLayout_2 = QFormLayout(self.groupBox_detalles_especificos)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.lbl_url_video = QLabel(self.groupBox_detalles_especificos)
        self.lbl_url_video.setObjectName(u"lbl_url_video")

        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.LabelRole, self.lbl_url_video)

        self.txt_url_video = QLineEdit(self.groupBox_detalles_especificos)
        self.txt_url_video.setObjectName(u"txt_url_video")

        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.FieldRole, self.txt_url_video)

        self.lbl_duracion = QLabel(self.groupBox_detalles_especificos)
        self.lbl_duracion.setObjectName(u"lbl_duracion")

        self.formLayout_2.setWidget(1, QFormLayout.ItemRole.LabelRole, self.lbl_duracion)

        self.txt_duracion = QLineEdit(self.groupBox_detalles_especificos)
        self.txt_duracion.setObjectName(u"txt_duracion")

        self.formLayout_2.setWidget(1, QFormLayout.ItemRole.FieldRole, self.txt_duracion)

        self.lbl_tipo_documento = QLabel(self.groupBox_detalles_especificos)
        self.lbl_tipo_documento.setObjectName(u"lbl_tipo_documento")

        self.formLayout_2.setWidget(2, QFormLayout.ItemRole.LabelRole, self.lbl_tipo_documento)

        self.txt_tipo_documento = QLineEdit(self.groupBox_detalles_especificos)
        self.txt_tipo_documento.setObjectName(u"txt_tipo_documento")

        self.formLayout_2.setWidget(2, QFormLayout.ItemRole.FieldRole, self.txt_tipo_documento)

        self.lbl_tamano_documento = QLabel(self.groupBox_detalles_especificos)
        self.lbl_tamano_documento.setObjectName(u"lbl_tamano_documento")

        self.formLayout_2.setWidget(3, QFormLayout.ItemRole.LabelRole, self.lbl_tamano_documento)

        self.txt_tamano_documento = QLineEdit(self.groupBox_detalles_especificos)
        self.txt_tamano_documento.setObjectName(u"txt_tamano_documento")

        self.formLayout_2.setWidget(3, QFormLayout.ItemRole.FieldRole, self.txt_tamano_documento)

        self.lbl_url_enlace = QLabel(self.groupBox_detalles_especificos)
        self.lbl_url_enlace.setObjectName(u"lbl_url_enlace")

        self.formLayout_2.setWidget(4, QFormLayout.ItemRole.LabelRole, self.lbl_url_enlace)

        self.txt_url_enlace = QLineEdit(self.groupBox_detalles_especificos)
        self.txt_url_enlace.setObjectName(u"txt_url_enlace")

        self.formLayout_2.setWidget(4, QFormLayout.ItemRole.FieldRole, self.txt_url_enlace)


        self.formLayout.setWidget(5, QFormLayout.ItemRole.SpanningRole, self.groupBox_detalles_especificos)


        self.verticalLayout_2.addWidget(self.groupBox_datos_contenido)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_guardar = QPushButton(self.tab_registro)
        self.btn_guardar.setObjectName(u"btn_guardar")

        self.horizontalLayout.addWidget(self.btn_guardar)

        self.btn_limpiar = QPushButton(self.tab_registro)
        self.btn_limpiar.setObjectName(u"btn_limpiar")

        self.horizontalLayout.addWidget(self.btn_limpiar)

        self.btn_cancelar_edicion = QPushButton(self.tab_registro)
        self.btn_cancelar_edicion.setObjectName(u"btn_cancelar_edicion")

        self.horizontalLayout.addWidget(self.btn_cancelar_edicion)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.tabWidget.addTab(self.tab_registro, "")
        self.tab_consulta = QWidget()
        self.tab_consulta.setObjectName(u"tab_consulta")
        self.verticalLayout_3 = QVBoxLayout(self.tab_consulta)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.groupBox_busqueda = QGroupBox(self.tab_consulta)
        self.groupBox_busqueda.setObjectName(u"groupBox_busqueda")
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox_busqueda)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lbl_buscar = QLabel(self.groupBox_busqueda)
        self.lbl_buscar.setObjectName(u"lbl_buscar")

        self.horizontalLayout_2.addWidget(self.lbl_buscar)

        self.txt_buscar = QLineEdit(self.groupBox_busqueda)
        self.txt_buscar.setObjectName(u"txt_buscar")

        self.horizontalLayout_2.addWidget(self.txt_buscar)

        self.btn_buscar = QPushButton(self.groupBox_busqueda)
        self.btn_buscar.setObjectName(u"btn_buscar")

        self.horizontalLayout_2.addWidget(self.btn_buscar)

        self.btn_mostrar_todo = QPushButton(self.groupBox_busqueda)
        self.btn_mostrar_todo.setObjectName(u"btn_mostrar_todo")

        self.horizontalLayout_2.addWidget(self.btn_mostrar_todo)


        self.verticalLayout_3.addWidget(self.groupBox_busqueda)

        self.tableWidget_contenidos = QTableWidget(self.tab_consulta)
        if (self.tableWidget_contenidos.columnCount() < 6):
            self.tableWidget_contenidos.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_contenidos.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_contenidos.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget_contenidos.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget_contenidos.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget_contenidos.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget_contenidos.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.tableWidget_contenidos.setObjectName(u"tableWidget_contenidos")

        self.verticalLayout_3.addWidget(self.tableWidget_contenidos)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.btn_editar_seleccionado = QPushButton(self.tab_consulta)
        self.btn_editar_seleccionado.setObjectName(u"btn_editar_seleccionado")

        self.horizontalLayout_3.addWidget(self.btn_editar_seleccionado)

        self.btn_eliminar_seleccionado = QPushButton(self.tab_consulta)
        self.btn_eliminar_seleccionado.setObjectName(u"btn_eliminar_seleccionado")

        self.horizontalLayout_3.addWidget(self.btn_eliminar_seleccionado)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.tabWidget.addTab(self.tab_consulta, "")

        self.verticalLayout.addWidget(self.tabWidget)

        vtnGestor.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(vtnGestor)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 33))
        vtnGestor.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(vtnGestor)
        self.statusbar.setObjectName(u"statusbar")
        vtnGestor.setStatusBar(self.statusbar)

        self.retranslateUi(vtnGestor)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(vtnGestor)
    # setupUi

    def retranslateUi(self, vtnGestor):
        vtnGestor.setWindowTitle(QCoreApplication.translate("vtnGestor", u"Gestor de Contenido Digital para Cursos", None))
        self.groupBox_datos_contenido.setTitle(QCoreApplication.translate("vtnGestor", u"Datos del Contenido", None))
        self.lbl_id.setText(QCoreApplication.translate("vtnGestor", u"ID (Solo Edici\u00f3n):", None))
        self.lbl_titulo.setText(QCoreApplication.translate("vtnGestor", u"T\u00edtulo:", None))
        self.lbl_fecha.setText(QCoreApplication.translate("vtnGestor", u"Fecha:", None))
        self.date_fecha.setDisplayFormat(QCoreApplication.translate("vtnGestor", u"yyyy-MM-dd", None))
        self.lbl_autor.setText(QCoreApplication.translate("vtnGestor", u"Autor:", None))
        self.lbl_tipo_contenido.setText(QCoreApplication.translate("vtnGestor", u"Tipo de Contenido:", None))
        self.cmb_tipo_contenido.setItemText(0, QCoreApplication.translate("vtnGestor", u"Video", None))
        self.cmb_tipo_contenido.setItemText(1, QCoreApplication.translate("vtnGestor", u"Documento", None))
        self.cmb_tipo_contenido.setItemText(2, QCoreApplication.translate("vtnGestor", u"EnlaceWeb", None))

        self.groupBox_detalles_especificos.setTitle(QCoreApplication.translate("vtnGestor", u"Detalles Espec\u00edficos", None))
        self.lbl_url_video.setText(QCoreApplication.translate("vtnGestor", u"URL Video:", None))
        self.lbl_duracion.setText(QCoreApplication.translate("vtnGestor", u"Duraci\u00f3n (min):", None))
        self.lbl_tipo_documento.setText(QCoreApplication.translate("vtnGestor", u"Tipo Documento:", None))
        self.lbl_tamano_documento.setText(QCoreApplication.translate("vtnGestor", u"Tama\u00f1o (KB):", None))
        self.lbl_url_enlace.setText(QCoreApplication.translate("vtnGestor", u"URL Enlace:", None))
        self.btn_guardar.setText(QCoreApplication.translate("vtnGestor", u"Guardar", None))
        self.btn_limpiar.setText(QCoreApplication.translate("vtnGestor", u"Limpiar", None))
        self.btn_cancelar_edicion.setText(QCoreApplication.translate("vtnGestor", u"Cancelar Edici\u00f3n", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_registro), QCoreApplication.translate("vtnGestor", u"Registro / Edici\u00f3n", None))
        self.groupBox_busqueda.setTitle(QCoreApplication.translate("vtnGestor", u"Buscar Contenido", None))
        self.lbl_buscar.setText(QCoreApplication.translate("vtnGestor", u"T\u00edtulo a buscar:", None))
        self.btn_buscar.setText(QCoreApplication.translate("vtnGestor", u"Buscar", None))
        self.btn_mostrar_todo.setText(QCoreApplication.translate("vtnGestor", u"Mostrar Todo", None))
        ___qtablewidgetitem = self.tableWidget_contenidos.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("vtnGestor", u"ID", None));
        ___qtablewidgetitem1 = self.tableWidget_contenidos.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("vtnGestor", u"T\u00edtulo", None));
        ___qtablewidgetitem2 = self.tableWidget_contenidos.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("vtnGestor", u"Fecha", None));
        ___qtablewidgetitem3 = self.tableWidget_contenidos.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("vtnGestor", u"Autor", None));
        ___qtablewidgetitem4 = self.tableWidget_contenidos.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("vtnGestor", u"Tipo", None));
        ___qtablewidgetitem5 = self.tableWidget_contenidos.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("vtnGestor", u"Detalles Espec\u00edficos", None));
        self.btn_editar_seleccionado.setText(QCoreApplication.translate("vtnGestor", u"Editar Seleccionado", None))
        self.btn_eliminar_seleccionado.setText(QCoreApplication.translate("vtnGestor", u"Eliminar Seleccionado", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_consulta), QCoreApplication.translate("vtnGestor", u"Consulta / Eliminaci\u00f3n", None))
    # retranslateUi

