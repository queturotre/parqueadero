CREATE TABLE clientes (
	cedula DOUBLE NOT NULL,
    nombre TEXT NOT NULL,
    apellido TEXT NOT NULL,
    telefono TEXT NOT NULL,
    PRIMARY KEY (cedula)
);

CREATE TABLE vehiculos (
	placa TEXT NOT NULL,
    tipo_vehiculo TEXT,
    marca TEXT,
    modelo TEXT,
    id_cliente DOUBLE,
    PRIMARY KEY (placa),
    FOREIGN KEY (id_cliente) REFERENCES clientes(cedula)
);

CREATE TABLE tarifas(
	hora_entrada DATETIME,
    hora_salida DATETIME,
    id_vehiculo TEXT,
    valor_total INT,
    PRIMARY KEY (hora_entrada),
    FOREIGN KEY (id_vehiculo) REFERENCES vehiculos(placa)
);
