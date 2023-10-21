CREATE TABLE clientes (
	cedula DOUBLE NOT NULL,
    nombre TEXT NOT NULL,
    apellido TEXT NOT NULL,
    telefono TEXT NOT NULL,
    PRIMARY KEY (cedula)
);

CREATE TABLE vehiculos (
	id_vehiculo INT NOT NULL,
	placa TEXT NOT NULL,
    tipo_vehiculo TEXT,
    marca TEXT,
    modelo TEXT,
    id_cliente DOUBLE,
    PRIMARY KEY (id_vehiculo),
    FOREIGN KEY (id_cliente) REFERENCES clientes(cedula)
);

CREATE TABLE tarifas(
	id_tarifa INT,
	hora_entrada DATETIME,
    hora_salida DATETIME,
    id_vehiculo INT,
    valor_total INT,
    PRIMARY KEY (id_tarifa),
    FOREIGN KEY (id_vehiculo) REFERENCES vehiculos(id_vehiculo)
);

INSERT INTO clientes
VALUES (
	10104568231, 'Amelia', 'Cruz', '3195502684' 
);

select * from clientes;