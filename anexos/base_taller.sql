CREATE TABLE Clientes (
id_cliente INT IDENTITY PRIMARY KEY,
nombre VARCHAR(60),
documento INT,
correo VARCHAR(60),
telefono VARCHAR(15)
)

CREATE TABLE Mecanicos(
id_mecanico INT IDENTITY PRIMARY KEY,
nombre VARCHAR(60),
documento INT,
fecha_ingreso DATE,
estado BIT
)

CREATE TABLE Servicios(
id_servicio INT IDENTITY PRIMARY KEY,
nombre VARCHAR(60),
valor DECIMAL(12, 1)
)

CREATE TABLE Vendedores (
id_vendedor INT IDENTITY PRIMARY KEY,
nombre VARCHAR(60),
documento INT,
fecha_ingreso DATE,
estado BIT
)

CREATE TABLE Repuestos (
id_repuesto INT IDENTITY PRIMARY KEY,
codigo NVARCHAR(13),
stock INT,
valor DECIMAL(12, 1),
minimo INT
)

CREATE TABLE Motos(
id_moto INT IDENTITY PRIMARY KEY,
marca VARCHAR(60),
modelo VARCHAR(4),
placa VARCHAR(6),
chasis VARCHAR(20),
color VARCHAR(20),
propietario_id INT FOREIGN KEY REFERENCES Clientes(id_cliente)
)

CREATE TABLE Orden_servicio (
id_ordenservicio INT IDENTITY PRIMARY KEY,
id_moto INT FOREIGN KEY REFERENCES Motos(id_moto),
fecha_ingreso DATETIME DEFAULT GETDATE(),
fecha_salida DATETIME DEFAULT GETDATE(), 
tipo VARCHAR(40),
estado VARCHAR(40),
observaciones VARCHAR(MAX)
)

CREATE TABLE Detalle_servicio(
id_detalleservicio INT IDENTITY PRIMARY KEY,
id_ordenservicio INT FOREIGN KEY REFERENCES Orden_servicio(id_ordenservicio),
id_servicio INT FOREIGN KEY REFERENCES Servicios(id_servicio),
id_mecanico INT FOREIGN KEY REFERENCES Mecanicos(id_mecanico),
valor DECIMAL(12, 1)
)

CREATE TABLE Ventas (
id_venta INT IDENTITY PRIMARY KEY,
factura  VARCHAR(10),
id_cliente INT FOREIGN KEY REFERENCES Clientes(id_cliente),
id_ordenservicio INT FOREIGN KEY REFERENCES Orden_servicio(id_ordenservicio),
id_vendedor INT FOREIGN KEY REFERENCES Vendedores(id_vendedor),
estado VARCHAR(40),
fecha DATETIME DEFAULT GETDATE(),
total DECIMAL(12, 1)
)

CREATE TABLE Detalle_venta (
id_detalleventa INT IDENTITY PRIMARY KEY,
id_venta INT FOREIGN KEY REFERENCES Ventas(id_venta),
id_repuesto INT FOREIGN KEY REFERENCES Repuestos(id_repuesto),
cantidad INT,
valor DECIMAL(12, 1)
)