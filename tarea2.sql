  	CREATE TABLE IF NOT EXISTS Aerolinea --
 (
   IdAerolinea INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
   Codigo TEXT NOT NULL,
   Nombre TEXT NOT NULL
 );
 
 
   	CREATE TABLE IF NOT EXISTS Aeropuerto --
 (
   IdAeropuerto INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
   Nombre TEXT NOT NULL,
   NumeroTelefono TEXT NOT NULL,
   Localizacion TEXT NOT NULL,
   Horario TEXT NOT NULL,
   Codigo TEXT NOT NULL
 );
 
    CREATE TABLE IF NOT EXISTS Vuelo --
 (
   IdVuelo INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
   IdAerolinea INTEGER NOT NULL,
   IdAvion INTEGER NOT NULL,
   NumeroVuelo INTEGER NOT NULL,
   Destino TEXT NOT NULL,
   Origen TEXT NOT NULL,
   FechaHoraSalida DATETIME NOT NULL,
   FechaHoraLlegada DATETIME NOT NULL,
   Precio INTEGER NOT NULL,
   IdEstado INTEGER NOT NULL,
   
   FOREIGN KEY (IdAerolinea) REFERENCES Aerolinea (IdAerolinea),
   FOREIGN KEY (IdAvion) REFERENCES Avion (IdAvion)
 );
 
    CREATE TABLE IF NOT EXISTS Avion --
 (
   IdAvion INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
   IdAerolinea INTEGER NOT NULL,
   Codigo TEXT NOT NULL,
   Modelo TEXT NOT NULL,
   Fabricante TEXT NOT NULL,
   CapacidadTripulacion INTEGER NOT NULL,
   CapacidadItinerario INTEGER NOT NULL,
   ClaseViajes TEXT NOT NULL,
   IdEstado INTEGER NOT NULL,

   FOREIGN KEY (IdAerolinea) REFERENCES Aerolinea (IdAerolinea)
 );
 
 
  	CREATE TABLE IF NOT EXISTS Taller --
 (
   IdAvion INTEGER NOT NULL,
   IdAeropuerto INTEGER NOT NULL,
   CodigoAvion TEXT NOT NULL,
   Repuestos TEXT NOT NULL,
   Costo INTEGER NOT NULL,
   FechaHoraSalida DATETIME NOT NULL,
   FechaHoraLlegada DATETIME NOT NULL,
   Daños TEXT NOT NULL,
   
   FOREIGN KEY (IdAvion) REFERENCES Avion (IdAvion),
   FOREIGN KEY (IdAeropuerto) REFERENCES Aeropuerto (IdAeropuerto)

 );
 
    CREATE TABLE IF NOT EXISTS Pasajero --
 (
   IdPasajero INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
   IdVuelo INTEGER NOT NULL,
   NumeroVuelo INTEGER NOT NULL,
   CantidadEquipaje INTEGER NOT NULL,
   Codigo TEXT NOT NULL,
   Nombre TEXT NOT NULL,
   Apellido1 TEXT NOT NULL,
   Apellido2 TEXT NOT NULL,
   InfoPasaporte TEXT NOT NULL,
   NumeroTelefono TEXT NOT NULL,

   FOREIGN KEY (IdVuelo) REFERENCES Vuelo (IdVuelo)
 );
 
     CREATE TABLE IF NOT EXISTS Equipaje --
 (
   IdEquipaje INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
   IdPasajero INTEGER NOT NULL,
   Codigo TEXT NOT NULL,
   Peso INTEGER NOT NULL,
   
   FOREIGN KEY (IdPasajero) REFERENCES Pasajero (IdPasajero)
 );
 
    CREATE TABLE IF NOT EXISTS Empleado --
(
    IdEmpleado INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    Nombre TEXT NOT NULL,
    Apellido1 TEXT NOT NULL,
    Apellido2 TEXT,
    Salario INTEGER NOT NULL,
    Cedula TEXT NOT NULL,
    Puesto TEXT NOT NULL,
    Codigo TEXT NOT NULL
);


    CREATE TABLE IF NOT EXISTS EmpleadoAerolinea --
(
    IdEmpleado INTEGER NOT NULL,
    IdAerolinea INTEGER NOT NULL,
    Horario TEXT,
    Puesto TEXT NOT NULL,

    FOREIGN KEY (IdEmpleado) REFERENCES Empleado (IdEmpleado),
    FOREIGN KEY (IdAerolinea) REFERENCES Aerolinea (IdAerolinea)

);

    CREATE TABLE IF NOT EXISTS EmpleadoAeropuerto --
(
    IdEmpleado INTEGER NOT NULL,
    IdAeropuerto INTEGER NOT NULL,
    Direccion TEXT,
    Puesto TEXT NOT NULL,

    FOREIGN KEY (IdEmpleado) REFERENCES Empleado (IdEmpleado),
    FOREIGN KEY (IdAeropuerto) REFERENCES Aeropuerto (IdAeropuerto)
);

    CREATE TABLE IF NOT EXISTS AerolineaAeropuerto --
(
    IdAerolinea INT NOT NULL,
    IdAeropuerto INTEGER NOT NULL,

    FOREIGN KEY (IdAerolinea) REFERENCES Aerolinea (IdAerolinea),
    FOREIGN KEY (IdAeropuerto) REFERENCES Aeropuerto (IdAeropuerto)
    
);

    CREATE TABLE IF NOT EXISTS Bodega --
(
    IdAvion INTEGER NOT NULL,
    IdAeropuerto INTEGER NOT NULL,

    FOREIGN KEY (IdAeropuerto) REFERENCES Aeropuerto (IdAeropuerto),
    FOREIGN KEY (IdAvion) REFERENCES Avion (IdAvion)
);

    CREATE TABLE IF NOT EXISTS ControladorVuelo --
(
    IdVuelo INTEGER,
    IdControlador INTEGER NOT NULL,
    CodigoAvion TEXT NOT NULL,
    CodigoComunicacion TEXT NOT NULL,
    CodigoVuelo TEXT NOT NULL,
    HoraLlegada TIME NOT NULL,
    PosicionActual TEXT NOT NULL,


    FOREIGN KEY (IdControlador) REFERENCES Controlador (IdControlador)
);


-- Consultas:

--  TOP 10 de aerolíneas con mayor cantidad de empleados.

SELECT A.Nombre, COUNT(EA.IdEmpleado) AS Empleados
FROM Empleado E
    INNER JOIN EmpleadoAerolinea EA ON E.IdEmpleado = EA.IdEmpleado
    INNER JOIN Aerolinea A ON A.IdAerolinea = EA.IdAerolinea 
GROUP BY A.Nombre
ORDER BY Empleados DESC
LIMIT 10;

-- TOP 10 de aeropuertos con más Aerolíneas.

SELECT AP.Nombre, COUNT(AA.IdAerolinea) AS Aerolineas
FROM Aeropuerto AP
    INNER JOIN AerolineaAeropuerto AA ON AP.IdAeropuerto = AA.IdAeropuerto
    INNER JOIN Aerolinea AL ON AL.IdAerolinea = AA.IdAerolinea 
GROUP BY AP.Nombre
ORDER BY Aerolineas DESC
LIMIT 10;

-- Aerolineas y Aeropuertos donde se encuentran

SELECT AL.Nombre, AP.Nombre
FROM Aerolinea AL
    INNER JOIN AerolineaAeropuerto AA ON AL.IdAerolinea = AA.IdAerolinea
    INNER JOIN Aeropuerto AP ON AP.IdAeropuerto = AA.IdAeropuerto
GROUP BY AL.Nombre;


