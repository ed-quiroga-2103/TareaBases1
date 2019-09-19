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
   Apellido2 TEXT ,
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
    IdEmpleado INTEGER NOT NULL,
    CodigoAvion TEXT NOT NULL,
    CodigoComunicacion TEXT NOT NULL,
    CodigoVuelo TEXT NOT NULL,
    HoraLlegada TIME NOT NULL,
    PosicionActual TEXT NOT NULL,


    FOREIGN KEY (IdEmpleado) REFERENCES Empleado (IdEmpleado)
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


-- Toda la información de un empleado de la aerolínea y del aeropuerto con
-- el sueldo más alto.

SELECT * 
FROM(   SELECT E.*, "Aeropuerto" AS Empleador
        FROM Empleado E
            INNER JOIN EmpleadoAeropuerto EA ON EA.IdEmpleado = E.IdEmpleado
        ORDER BY E.Salario DESC
        LIMIT 1
    )
    
UNION

SELECT * 
FROM(   SELECT E.*, "Aerolinea" AS Empleador
        FROM Empleado E
            INNER JOIN EmpleadoAerolinea EA ON EA.IdEmpleado = E.IdEmpleado
        ORDER BY E.Salario DESC
        LIMIT 1
    );


--  Promedio de salario para los aeropuertos con mayor número de
--  empleados.

SELECT A.Nombre, AVG(E.Salario) AS PromedioSalarios, COUNT(EA.IdEmpleado) AS NumEmpleados
FROM Empleado E
    INNER JOIN EmpleadoAeropuerto EA ON E.IdEmpleado = EA.IdEmpleado
    INNER JOIN Aeropuerto A ON A.IdAeropuerto = EA.IdAeropuerto 
GROUP BY A.Nombre
ORDER BY NumEmpleados DESC
LIMIT 10;


--  Cantidad de aviones en una aerolínea que están en estado de reparación.

SELECT AL.Nombre, COUNT(A.IdAvion) AS Aviones
FROM Avion A
    INNER JOIN Aerolinea AL ON AL.IdAerolinea = A.IdAerolinea 
WHERE A.IdEstado = "REP"
GROUP BY AL.Nombre
ORDER BY Aviones DESC;


-- Costo de reparación, modelo, fabricante y el código de un avión para una
-- aerolínea perteneciente a un aeropuerto específico.

SELECT AP.Nombre, T.Costo, A.Modelo, A.Fabricante, A.Codigo, AL.Nombre
FROM Taller T
    INNER JOIN Avion A ON T.IdAvion = A.IdAvion
    INNER JOIN Aerolinea AL ON AL.IdAerolinea = A.IdAerolinea
    INNER JOIN AerolineaAeropuerto AA ON AA.IdAerolinea = AL.IdAerolinea
    INNER JOIN Aeropuerto AP ON T.IdAeropuerto = AP.IdAeropuerto
        AND AA.IdAeropuerto = AP.IdAeropuerto
ORDER BY AP.Nombre;


-- Cantidad de aviones activos en un aeropuerto.

SELECT AP.Nombre, COUNT(V.IdVuelo) AS Vuelos
FROM Vuelo V
    INNER JOIN Aeropuerto AP 
    ON AP.Localizacion = V.Origen OR AP.Localizacion = V.Destino 
WHERE V.IdEstado = "Finalizado" OR V.IdEstado = "En Proceso"
GROUP BY AP.Nombre
ORDER BY Vuelos DESC;


-- Promedio de costo de reparación de los aviones para un aeropuerto
-- específico.

SELECT A.Nombre, AVG(T.Costo) AS Promedio, COUNT(T.Costo) AS Aviones
FROM Taller T
    INNER JOIN Aeropuerto A ON A.IdAeropuerto = T.IdAeropuerto 
GROUP BY A.Nombre
ORDER BY Aviones DESC;


-- Cantidad de aviones inactivos dentro de una bodega.

SELECT A.Nombre, COUNT(B.IdAvion) AS Aviones
FROM Bodega B
    INNER JOIN Aeropuerto A ON A.IdAeropuerto = B.IdAeropuerto 
GROUP BY A.Nombre
ORDER BY Aviones DESC;


-- Nombre de los fabricantes con la mayor cantidad de modelos.

SELECT A.Fabricante, COUNT(DISTINCT A.Modelo) AS Modelos
FROM Avion A
GROUP BY A.Fabricante
ORDER BY Modelos DESC;


-- Cantidad de aerolíneas que contienen la letra “A” en el nombre. De este
-- resultado además deben de mostrar cuáles tienen más vuelos activos.

SELECT AL.Nombre, COUNT(A.IdEstado) AS Aviones
FROM Aerolinea AL
    INNER JOIN Avion A ON A.IdAerolinea = AL.IdAerolinea
WHERE AL.Nombre LIKE "%a%" AND A.IdEstado = "ACT"
GROUP BY AL.Nombre
ORDER BY Aviones DESC;


-- Intervalo de horas con la mayor llegada de aviones para un aeropuerto.

SELECT AP.Nombre, 
    SUBSTR(FechaHoraLlegada,INSTR(FechaHoraLlegada," ")+1) AS Llegada,
    COUNT(TIME(V.FechaHoraLlegada)) AS Horas 
FROM Vuelo V
    INNER JOIN Aeropuerto AP ON AP.Localizacion = V.Destino
GROUP BY AP.Nombre
ORDER BY Horas DESC;
                                                                                    


