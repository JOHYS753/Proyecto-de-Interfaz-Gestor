-- Crear la tabla Contenidos con la columna IDENTITY
CREATE TABLE Contenidos (
    id_contenido INT PRIMARY KEY IDENTITY(1,1), -- ¡Esta es la configuración clave!
    titulo VARCHAR(255) NOT NULL,
    fecha DATE NOT NULL,
    autor VARCHAR(255) NOT NULL,
    tipo_contenido VARCHAR(50) NOT NULL
);
GO

-- Crear la tabla Videos con su clave foránea
CREATE TABLE Videos (
    id_contenido INT PRIMARY KEY,
    url_video VARCHAR(MAX) NOT NULL,
    duracion DECIMAL(10,2),
    FOREIGN KEY (id_contenido) REFERENCES Contenidos(id_contenido)
        ON DELETE CASCADE -- Opcional: para que se elimine en cascada si se borra el contenido principal
);
GO

-- Crear la tabla Documentos con su clave foránea
CREATE TABLE Documentos (
    id_contenido INT PRIMARY KEY,
    tipo_documento VARCHAR(50) NOT NULL,
    tamano_documento DECIMAL(10,2),
    FOREIGN KEY (id_contenido) REFERENCES Contenidos(id_contenido)
        ON DELETE CASCADE
);
GO

-- Crear la tabla EnlacesWeb con su clave foránea
CREATE TABLE EnlacesWeb (
    id_contenido INT PRIMARY KEY,
    url_enlace VARCHAR(MAX) NOT NULL,
    FOREIGN KEY (id_contenido) REFERENCES Contenidos(id_contenido)
        ON DELETE CASCADE
);
GO