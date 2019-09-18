from random import choice
import string


def linesToList(path):
    file = open(path,"r")
    nameList = []

    for line in file:
        line = line.rstrip()      
        if line:                  
            nameList.append(line)

    file.close()

    return nameList

def randPickNames(nameList, num):
    finalList = []
    for i in range(num):
        finalList.append(choice(nameList))
    
    return finalList

def randPickNamesNoRepeat(nameList, num):
    indList = []
    finalList = []
    for i in range(num):

        ind = choice(range(0,len(nameList)))

        while ind in indList:
            ind = choice(range(0,len(nameList)))
        
        indList.append(ind)

        finalList.append(nameList[ind])

    return finalList

def createEmployeeAerolinea(nameList, lastNameList, idNum):

    name = choice(nameList)
    lastname1 = choice(lastNameList)
    lastname2 = choice(lastNameList)
    salary = choice([1000,2000,5000,10000,30000,50000])

    identification = ""

    for i in range(8):
        identification += str(choice(range(10)))
    
    job = choice(["Piloto","Azafata","Copiloto"])

    code = job[0].upper() + job[1].upper() + lastname1[0] + lastname2[0] + identification[-2] + identification[-1]

    return (idNum,name,lastname1,lastname2,salary,identification,job,code)

def createEmployeeAeropuerto(nameList, lastNameList, idNum):

    name = choice(nameList)
    lastname1 = choice(lastNameList)
    lastname2 = choice(lastNameList)
    salary = choice([1000,2000,5000,10000,30000,50000])

    identification = ""

    for i in range(8):
        identification += str(choice(range(10)))
    
    job = choice(["Despachador","Tecnico","Agente","Auxiliar"])

    code = job[0].upper() + job[1].upper() + lastname1[0] + lastname2[0] + identification[-2] + identification[-1]

    return (idNum,name,lastname1,lastname2,salary,identification,job,code)

def createAeropuerto(name, idNum):
    location = name

    name += " International Airport"

    phone = ""

    for i in range(8):
        phone += str(choice(range(10)))

    code = name[0].upper() + name [1].upper() + name[2].upper() + phone[0] + phone[1]

    sched = choice(["De 5 A.M. a 1 A.M.", "De 7 A.M. a 7 P.M.", "De 4 A.M. a 12 M.N.", "24/7"])

    return (idNum,name,phone,location,sched,code)

def createAerolinea(name, idNum):

    code = name[0].upper() + name [1].upper() + name[2].upper() + str(idNum)

    return (idNum,code,name)

def getAerolineaAeropuerto():

    for i in range(30):
        for j in range(8):

            querry = (j+1,i+1)
            print(querry,",")

def createModelos():
    for i in range(500):
        model = str(choice(range(10))) + str(choice(range(10)))+ str(choice(range(10))) +"-"+ str(choice(range(10)))
        
        for i in range(4):
            model += choice(string.ascii_uppercase)
        
        print(model)
        model = ""

def createAvion(idNum, manufact, idAero, model):

    model = manufact[0].upper() + manufact[1].upper() + model

    schedCapacity = choice(range(1,4))
    tripCapacity = choice(range(500,2500))

    flightClass = choice(["Econ","Premium","Econ/Premium","Private"])
    state = choice(["ACT", "INACT", "REP"])

    code = model[0].upper()+manufact[0].upper()+str(schedCapacity)+str(tripCapacity)

    return (idNum, idAero, code, model, manufact, tripCapacity, schedCapacity, flightClass, state)

def createVuelo(idNum, idAero, idAvion, origin, destiny):
    num = idNum
    price = choice([75,100,150,200,300,500,750])
    state = choice(["Preparandose","En Proceso","Finalizado"])
    
    date = "2019-"+ str(choice(range(12))+1)+ "-"+ str(choice(range(31))+ 1)

    ind = choice(range(4))

    iniTimes = ["01:00:00", "13:45:00", "17:00:00", "19:00:00"]
    finTimes = ["05:30:00", "17:00:00", "23:00:00", "22:45:00"] 

    time1 = iniTimes[ind]
    time2 = finTimes[ind]

    datetime1 = date+" "+time1
    datetime2 = date+" "+time2

    return (idNum, idAero, idAvion, num, destiny, origin, datetime1, datetime2, price, state)

def getVuelos():

    for i in range(300):
        
        idAvion = choice(range(80))+1
        idAero = choice(range(8))+1

        origin = choice(linesToList("aeropuertos.txt"))
        destiny = choice(linesToList("aeropuertos.txt"))

        while origin == destiny:
            destiny = choice(linesToList("aeropuertos.txt"))    

        querry = createVuelo(i+1, idAero, idAvion, origin, destiny)
        print(querry,",")

def createPasajero(idNum, idVuelo, nameList, lastNameList):

    numVuelo = idVuelo
    bags = choice(range(5))
    name = choice(nameList)
    lastname1 = choice(lastNameList)
    lastname2 = choice(lastNameList)
    code = str(numVuelo) + name[0].upper() + lastname1[0].upper() + lastname2[0].upper()
    passport = ""
    for i in range(8):
        passport += str(choice(range(10)))
    phone = ""

    for i in range(8):
        phone += str(choice(range(10)))

    return (idNum, idVuelo,numVuelo,bags,code,name,lastname1,lastname2,passport,phone)

def createEquipaje(idNum, idPasajero, pasCode):

    code = str(idNum) + pasCode

    weight = choice(range(50))+1

    return (idNum, idPasajero, code, weight)

def getPasajeros():

    querryLists = ([],[])
    equipajeId = 0

    for i in range(1000):
        querry1 = createPasajero(i+1, choice(range(300))+1,linesToList("nombres.txt"), linesToList("apellidos.txt"))
        querryLists[0].append(querry1)

        for j in range(querry1[3]):
            equipajeId+=1

            querry2 = createEquipaje(equipajeId,i+1,querry1[4])

            querryLists[1].append(querry2)
    
    file = open("pasajerosEquipaje.txt", "w+")

    file.write("\nINSERT INTO Pasajero VALUES\n")

    for i in querryLists[0]:
        file.write(str(i)+",\n")

    file.write("\nINSERT INTO Equipaje VALUES\n")

    for i in querryLists[1]:
        file.write(str(i)+",\n")

    file.close()

getPasajeros()
        
def createControlador(idNum):
    return (idNum)

def createEmpleadoAerolinea(idEmpl, idAero, job):

    sched = choice(["De 5 A.M. a 1 A.M.", "De 7 A.M. a 7 P.M.", "De 4 A.M. a 12 M.N."])

    return (idEmpl, idAero, sched, job)

def createEmpleadoAeropuerto(idEmpl, idAero, job):

    address = choice(["Alajuela", "Cartago", "San José", "Heredia","Puntarenas","Guanacaste","Limon"])

    return (idEmpl, idAero, address, job)

def getAeropuertosAndAerolineas():

    querryList1 = []
    querryList2 = []

    fileAerolineas = "aerolineas.txt"
    fileAeropuertos = "aeropuertos.txt"

    listAerolineas = randPickNamesNoRepeat(linesToList(fileAerolineas),8)
    listAeropuertos = randPickNamesNoRepeat(linesToList(fileAeropuertos),30)

    for i in range(8):

        querry = createAerolinea(listAerolineas[i], i+1)

        querryList1.append(querry)

    for i in range(30):

        querry = createAeropuerto(listAeropuertos[i], i+1)

        querryList2.append(querry)

    return [querryList1, querryList2]

def getEmpleadosAeropuerto():

    querryList1 = []
    querryList2 = []

    idNum = 200

    for i in range(300):
        
        idNum+=1
        querry1 = createEmployeeAeropuerto(linesToList("nombres.txt"),linesToList("apellidos.txt"),idNum)
        querryList1.append(querry1)

        
        aeroId = choice(range(30))

        querry2 = createEmpleadoAeropuerto(idNum,aeroId+1, querry1[-2])
        querryList2.append(querry2)
    
    return (querryList1,querryList2)

def getEmpleadosAerolinea():

    querryList1 = []
    querryList2 = []

    idNum = 0

    for i in range(200):
        
        idNum+=1
        querry1 = createEmployeeAerolinea(linesToList("nombres.txt"),linesToList("apellidos.txt"),idNum)
        querryList1.append(querry1)

        
        aeroId = choice(range(8))

        querry2 = createEmpleadoAerolinea(idNum,aeroId+1, querry1[-2])
        querryList2.append(querry2)
    
    return (querryList1,querryList2)

def createEmployeeControlador(nameList, lastNameList, idNum):
    name = choice(nameList)
    lastname1 = choice(lastNameList)
    lastname2 = choice(lastNameList)
    salary = choice([1000,2000,5000,10000,30000,50000])

    identification = ""

    for i in range(8):
        identification += str(choice(range(10)))
    
    job = "Controlador"

    code = job[0].upper() + job[1].upper() + lastname1[0] + lastname2[0] + identification[-2] + identification[-1]

    return (idNum,name,lastname1,lastname2,salary,identification,job,code)



def createEmpleadosControlador():

    querryList1 = []
    querryList2 = []

    idNum = 500

    for i in range(300):
        
        idNum+=1
        querry1 = createEmployeeControlador(linesToList("nombres.txt"),linesToList("apellidos.txt"),idNum)
        querryList1.append(querry1)

        
        aeroId = choice(range(30))

        querry2 = createEmpleadoAeropuerto(idNum,aeroId+1, querry1[-2])
        querryList2.append(querry2)
    
    return (querryList1,querryList2)

querries = createEmpleadosControlador()

file = open("empleadosControlador.txt","w+")

for tup in querries[0]:
    file.write(str(tup)+",\n")

file.write("\n++++++++++++++++++++++++++++\n")

for tup in querries[1]:
    file.write(str(tup)+",\n")

def getAviones(numAviones):
    querryList = []
    manufactList = linesToList("fabricantes.txt")
    modelList = randPickNamesNoRepeat(linesToList("modelos.txt"), 80)
    idNum = 0
    for i in range(8):

        for j in range(numAviones):
            idNum+=1
            querry = createAvion(idNum, choice(manufactList),i+1, choice(modelList))
            querryList.append(querry)
            print(querry,",")
    return querryList

def getTallerAndBodega(avionesList):
    resTup = ([],[])

    for i in avionesList:
        if i[8] == "REP":
            resTup[0].append(i)
        elif i[8] == "INACT":
            resTup[1].append(i)
    
    file = open("TallerYBodega.txt", "w+")

    for i in resTup:
        for j in i:
            file.write(str(j))
            file.write(",\n")

        file.write("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
    
    file.close()

    return resTup

def createFactura(idNum, idAero, code):

    damage = choice(["Alas", "Motores","Ruedas", "Controles"])

    parts = damage

    cost = choice([1000,2000,5000,10000,15000,50000])

    date = "2019-"+ str(choice(range(12))+1)+ "-"+ str(choice(range(31))+ 1)

    ind = choice(range(4))

    iniTimes = ["01:00:00", "13:45:00", "17:00:00", "19:00:00"]
    finTimes = ["05:30:00", "17:00:00", "23:00:00", "22:45:00"] 

    time1 = iniTimes[ind]
    time2 = finTimes[ind]

    datetime1 = date+" "+time1
    datetime2 = date+" "+time2

    return (idNum, idAero, code, parts, cost, datetime1, datetime2, damage)

def getBodega(avionesList):

    while(avionesList != []):

        for i in range(30): 
            
            posib = choice(range(10))

            if posib < 5 and avionesList != []:

                avion = choice(avionesList)
                avionesList.remove(avion)

                querry = (avion[0], i+1)

                print(querry,",")

def getTaller(avionesList):

    while(avionesList != []):

            for i in range(30): 
                
                posib = choice(range(10))

                if posib < 5 and avionesList != []:
                    
                    avion = choice(avionesList)
                    avionesList.remove(avion)

                    querry = createFactura(avion[0],i+1,avion[2])

                    print(querry,",")

def createControladorVuelo(avionesList, vuelosList):
    
    file = open("ControladorVuelo.txt", "w+")

    file.write("INSERT INTO ControladorVuelo VALUES\n")


    for i in range(80):
        
        idContr = choice(range(30))+1

        size = len(avionesList)
        codigoAvion = getCodigoAvionFromVuelo(i+1,avionesList)
        codigoCom = codigoAvion
        codigoVuelo = i+1
        horaLlegada = vuelosList[i][7].split()[1]
        pos = choice(linesToList("posiciones.txt"))

        querry = str((i+1, idContr, codigoAvion, codigoCom,codigoVuelo, horaLlegada, pos))

        file.write(querry +",\n")

    file.close()

def getCodigoAvionFromVuelo(ind, listaAviones):
    for avion in listaAviones:
        if avion[0] == ind:
            print(avion[2])
            return avion[2]
    return "UNASSIGNED"


listaAviones = [(1, 1, 'BB32361', 'BU750-9QONA', 'Bushby', 2361, 3, 'Econ/Premium', 'INACT') ,
(2, 1, 'EE11662', 'EM656-5OTQZ', 'Embraer-Empresa Brasileira DR AeronÁutica', 1662, 1, 'Econ/Premium', 'INACT') ,
(3, 1, 'EE31168', 'EM802-9PJUF', 'Embraer-Empresa Brasileira DR AeronÁutica', 1168, 3, 'Econ/Premium', 'REP') ,
(4, 1, 'BB31169', 'BU333-8ZCTJ', 'Burgess', 1169, 3, 'Econ', 'REP') ,
(5, 1, 'BB22353', 'BU155-9GDER', 'Burgess', 2353, 2, 'Econ', 'INACT') ,
(6, 1, 'BB1687', 'BU611-0JTAF', 'Bushby', 687, 1, 'Premium', 'ACT') ,
(7, 1, 'AA21069', 'AI720-5FBYK', 'Airbus Corporate Jets', 1069, 2, 'Econ/Premium', 'ACT') ,
(8, 1, 'BB3814', 'BU007-7WNCJ', 'Burgess', 814, 3, 'Private', 'ACT') ,
(9, 1, 'BB2586', 'BO847-9ZQKH', 'Boeing Business Jets', 586, 2, 'Econ/Premium', 'REP') ,
(10, 1, 'BB31863', 'BU782-5KCAJ', 'Buhl', 1863, 3, 'Premium', 'ACT') ,
(11, 2, 'GG11679', 'GU538-8MVJV', 'Gulfstream Aerospace', 1679, 1, 'Econ', 'INACT') ,
(12, 2, 'TT2617', 'TE010-1TMAZ', 'Textron Aviation', 617, 2, 'Private', 'ACT') ,
(13, 2, 'BB32454', 'BU866-5SNGB', 'Buhl', 2454, 3, 'Econ', 'INACT') ,
(14, 2, 'BB12043', 'BY971-1MNGO', 'Bye Aerospace', 2043, 1, 'Econ/Premium', 'REP') ,
(15, 2, 'BB1976', 'BU264-2DONZ', 'Buhl', 976, 1, 'Premium', 'ACT') ,
(16, 2, 'AA2997', 'AI286-1LJES', 'Airbus Corporate Jets', 997, 2, 'Econ', 'INACT') ,
(17, 2, 'BB31563', 'BU375-9HBMB', 'Bushby', 1563, 3, 'Econ/Premium', 'INACT') ,
(18, 2, 'BB32389', 'BU124-9ONWW', 'Bushby', 2389, 3, 'Premium', 'INACT') ,
(19, 2, 'BB31691', 'BU109-5ZXNJ', 'Burnelli', 1691, 3, 'Econ/Premium', 'INACT') ,
(20, 2, 'TT21901', 'TE584-3TFSJ', 'Textron Aviation', 1901, 2, 'Private', 'REP') ,
(21, 3, 'BB11771', 'BO477-6HHYX', 'Boeing Business Jets', 1771, 1, 'Private', 'REP') ,
(22, 3, 'BB3536', 'BU187-7VWMG', 'Buethe', 536, 3, 'Private', 'ACT') ,
(23, 3, 'DD22271', 'DA019-1FWIF', 'Dassault Falcon', 2271, 2, 'Econ', 'INACT') ,
(24, 3, 'EE1636', 'EM776-7TWDR', 'Embraer-Empresa Brasileira DR AeronÁutica', 636, 1, 'Econ', 'INACT') ,
(25, 3, 'BB3791', 'BU018-2OWPV', 'Bushby', 791, 3, 'Private', 'INACT') ,
(26, 3, 'BB3617', 'BU396-0LEGB', "Burl's Aircraft", 617, 3, 'Econ/Premium', 'REP') ,
(27, 3, 'BB12212', 'BU228-3KILW', "Burl's Aircraft", 2212, 1, 'Econ/Premium', 'ACT') ,
(28, 3, 'BB11831', 'BU992-2IXYM', 'Bushby', 1831, 1, 'Premium', 'REP') ,
(29, 3, 'BB21592', 'BU007-7WNCJ', 'Bushby', 1592, 2, 'Econ/Premium', 'INACT') ,
(30, 3, 'GG22260', 'GU856-3JEYV', 'Gulfstream Aerospace', 2260, 2, 'Econ/Premium', 'ACT') ,
(31, 4, 'AA11934', 'AI525-7IIRB', 'Airbus Corporate Jets', 1934, 1, 'Econ', 'REP') ,
(32, 4, 'BB11590', 'BU581-1NUPI', 'Buhl', 1590, 1, 'Private', 'INACT') ,
(33, 4, 'BB22466', 'BO157-3BBSJ', 'Boeing Business Jets', 2466, 2, 'Premium', 'ACT') ,
(34, 4, 'BB11893', 'BY324-8PUVT', 'Bye Aerospace', 1893, 1, 'Private', 'REP') ,
(35, 4, 'BB31675', 'BU871-2HFEI', 'Bushby', 1675, 3, 'Econ/Premium', 'INACT') ,
(36, 4, 'BB11969', 'BU920-8SPCM', 'Buethe', 1969, 1, 'Econ/Premium', 'ACT') ,
(37, 4, 'BB21721', 'BO554-3SIVD', 'Bombardier Aerospace', 1721, 2, 'Econ', 'INACT') ,
(38, 4, 'PP21525', 'PI587-0GPDH', 'Pilatus Business Aircraft', 1525, 2, 'Econ', 'ACT') ,
(39, 4, 'EE31440', 'EM663-5XCSJ', 'Embraer-Empresa Brasileira DR AeronÁutica', 1440, 3, 'Private', 'INACT') ,
(40, 4, 'AA22388', 'AI187-7VWMG', 'Airbus Corporate Jets', 2388, 2, 'Private', 'ACT') ,
(41, 5, 'BB11484', 'BÜ335-0AHBM', 'Büttner Propeller', 1484, 1, 'Econ/Premium', 'REP') ,
(42, 5, 'BB1720', 'BU157-3BBSJ', 'Buhl', 720, 1, 'Econ/Premium', 'ACT') ,
(43, 5, 'DD21875', 'DA920-8SPCM', 'Dassault Falcon', 1875, 2, 'Econ', 'INACT') ,
(44, 5, 'BB32355', 'BU440-0QYPN', 'Bushby', 2355, 3, 'Private', 'ACT') ,
(45, 5, 'GG31045', 'GU802-9PJUF', 'Gulfstream Aerospace', 1045, 3, 'Private', 'REP') ,
(46, 5, 'BB31017', 'BU963-6FRIN', "Burl's Aircraft", 1017, 3, 'Private', 'INACT') ,
(47, 5, 'BB21445', 'BÜ663-5XCSJ', 'Büttner Propeller', 1445, 2, 'Private', 'ACT') ,
(48, 5, 'BB21462', 'BU611-0JTAF', 'Buhl', 1462, 2, 'Private', 'REP') ,
(49, 5, 'DD21430', 'DA391-3VIGW', 'Dassault Falcon', 1430, 2, 'Premium', 'ACT') ,
(50, 5, 'GG11911', 'GU277-0OCUF', 'Gulfstream Aerospace', 1911, 1, 'Private', 'ACT') ,
(51, 6, 'BB2558', 'BO007-7WNCJ', 'Bombardier Aerospace', 558, 2, 'Econ', 'REP') ,
(52, 6, 'BB22336', 'BY648-6BFOV', 'Bye Aerospace', 2336, 2, 'Econ/Premium', 'REP') ,
(53, 6, 'EE31348', 'EM520-6YXJB', 'Embraer-Empresa Brasileira DR AeronÁutica', 1348, 3, 'Econ', 'INACT') ,
(54, 6, 'BB12369', 'BU776-7TWDR', 'Buhl', 2369, 1, 'Econ/Premium', 'REP') ,
(55, 6, 'BB1831', 'BU095-5VMMN', "Burl's Aircraft", 831, 1, 'Premium', 'REP') ,
(56, 6, 'BB2814', 'BÜ928-6ICID', 'Büttner Propeller', 814, 2, 'Private', 'REP') ,
(57, 6, 'PP2761', 'PI157-3BBSJ', 'Pilatus Business Aircraft', 761, 2, 'Econ/Premium', 'INACT') ,
(58, 6, 'PP32272', 'PI920-8SPCM', 'Pilatus Business Aircraft', 2272, 3, 'Econ/Premium', 'INACT') ,
(59, 6, 'BB31125', 'BU587-0GPDH', "Burl's Aircraft", 1125, 3, 'Premium', 'REP') ,
(60, 6, 'BB31846', 'BY286-1LJES', 'Bye Aerospace', 1846, 3, 'Private', 'INACT') ,
(61, 7, 'BB11839', 'BU041-3DAPR', 'Burgess', 1839, 1, 'Econ', 'ACT') ,
(62, 7, 'BB1785', 'BU871-2HFEI', 'Buhl', 785, 1, 'Econ', 'INACT') ,
(63, 7, 'BB31936', 'BU587-0GPDH', 'Buhl', 1936, 3, 'Premium', 'REP') ,
(64, 7, 'DD2730', 'DA818-5LFFA', 'Dassault Falcon', 730, 2, 'Private', 'REP') ,
(65, 7, 'BB22174', 'BO095-2DIFY', 'Bombardier Aerospace', 2174, 2, 'Private', 'INACT') ,
(66, 7, 'BB3590', 'BU210-7VHQI', "Burl's Aircraft", 590, 3, 'Premium', 'INACT') ,
(67, 7, 'BB3581', 'BO890-2XBAD', 'Boeing Business Jets', 581, 3, 'Econ/Premium', 'ACT') ,
(68, 7, 'BB21652', 'BU525-7IIRB', 'Buethe', 1652, 2, 'Econ/Premium', 'INACT') ,
(69, 7, 'BB22224', 'BU112-2QTPQ', 'Burgess', 2224, 2, 'Econ/Premium', 'INACT') ,
(70, 7, 'BB11827', 'BU770-0YSPE', 'Buhl', 1827, 1, 'Econ', 'INACT') ,
(71, 8, 'PP3758', 'PI095-5VMMN', 'Pilatus Business Aircraft', 758, 3, 'Premium', 'ACT') ,
(72, 8, 'BB1726', 'BU210-7VHQI', 'Burgess', 726, 1, 'Econ', 'REP') ,
(73, 8, 'BB3908', 'BU007-7WNCJ', 'Buhl', 908, 3, 'Econ', 'REP') ,
(74, 8, 'EE3682', 'EM333-8ZCTJ', 'Embraer-Empresa Brasileira DR AeronÁutica', 682, 3, 'Premium', 'REP') ,
(75, 8, 'BB21439', 'BU124-9ONWW', 'Buethe', 1439, 2, 'Econ/Premium', 'REP') ,
(76, 8, 'DD22453', 'DA061-1HCOT', 'Dassault Falcon', 2453, 2, 'Private', 'ACT') ,
(77, 8, 'DD21450', 'DA312-0SWOH', 'Dassault Falcon', 1450, 2, 'Private', 'REP') ,
(78, 8, 'EE31473', 'EM866-5SNGB', 'Embraer-Empresa Brasileira DR AeronÁutica', 1473, 3, 'Econ/Premium', 'INACT') ,
(79, 8, 'BB1547', 'BÜ095-5VMMN', 'Büttner Propeller', 547, 1, 'Private', 'REP') ,
(80, 8, 'BB3726', 'BU611-0JTAF', 'Bushby', 726, 3, 'Econ/Premium', 'REP')]

listaVuelos = [
(1, 6, 13, 1, 'Nevada', 'Alaska', '2019-8-7 13:45:00', '2019-8-7 17:00:00', 750, 'Preparandose') ,
(2, 8, 3, 2, 'Connecticut', 'Rhode Island', '2019-11-14 13:45:00', '2019-11-14 17:00:00', 75, 'Finalizado') ,
(3, 7, 76, 3, 'West Virginia', 'Arkansas', '2019-2-13 19:00:00', '2019-2-13 22:45:00', 200, 'Finalizado') ,
(4, 5, 33, 4, 'Delaware', 'Massachusetts', '2019-7-8 01:00:00', '2019-7-8 05:30:00', 200, 'Finalizado') ,
(5, 6, 63, 5, 'New Hampshire', 'Wyoming', '2019-2-3 19:00:00', '2019-2-3 22:45:00', 500, 'Finalizado') ,
(6, 7, 18, 6, 'Hawaii', 'West Virginia', '2019-2-6 01:00:00', '2019-2-6 05:30:00', 300, 'En Proceso') ,
(7, 6, 56, 7, 'Hawaii', 'Illinois', '2019-9-4 17:00:00', '2019-9-4 23:00:00', 200, 'Finalizado') ,
(8, 8, 39, 8, 'Kansas', 'Texas', '2019-4-14 19:00:00', '2019-4-14 22:45:00', 500, 'Preparandose') ,
(9, 4, 56, 9, 'New Hampshire', 'West Virginia', '2019-1-25 13:45:00', '2019-1-25 17:00:00', 75, 'En Proceso') ,
(10, 6, 79, 10, 'Minnesota', 'Oklahoma', '2019-5-3 01:00:00', '2019-5-3 05:30:00', 75, 'Finalizado') ,
(11, 2, 45, 11, 'Wyoming', 'Pennsylvania', '2019-8-29 01:00:00', '2019-8-29 05:30:00', 500, 'Finalizado') ,
(12, 2, 41, 12, 'Wisconsin', 'Oklahoma', '2019-1-3 19:00:00', '2019-1-3 22:45:00', 300, 'Preparandose') ,
(13, 3, 57, 13, 'Montana', 'Florida', '2019-10-19 01:00:00', '2019-10-19 05:30:00', 75, 'Preparandose') ,
(14, 3, 63, 14, 'Virginia', 'Vermont', '2019-1-17 13:45:00', '2019-1-17 17:00:00', 200, 'Finalizado') ,
(15, 7, 16, 15, 'Arkansas', 'Oregon', '2019-2-8 13:45:00', '2019-2-8 17:00:00', 500, 'Preparandose') ,
(16, 1, 57, 16, 'New Hampshire', 'Nebraska', '2019-5-12 19:00:00', '2019-5-12 22:45:00', 300, 'En Proceso') ,
(17, 1, 12, 17, 'Montana', 'New Jersey', '2019-2-31 13:45:00', '2019-2-31 17:00:00', 100, 'Finalizado') ,
(18, 7, 77, 18, 'Texas', 'Nevada', '2019-12-10 17:00:00', '2019-12-10 23:00:00', 750, 'En Proceso') ,
(19, 7, 14, 19, 'Florida', 'New York', '2019-7-8 13:45:00', '2019-7-8 17:00:00', 500, 'Preparandose') ,
(20, 3, 58, 20, 'Hawaii', 'Maryland', '2019-9-25 19:00:00', '2019-9-25 22:45:00', 200, 'Finalizado') ,
(21, 8, 29, 21, 'Colorado', 'Wisconsin', '2019-5-23 01:00:00', '2019-5-23 05:30:00', 500, 'En Proceso') ,
(22, 1, 50, 22, 'Kentucky', 'Maine', '2019-6-26 13:45:00', '2019-6-26 17:00:00', 500, 'Preparandose') ,
(23, 6, 56, 23, 'Montana', 'Louisiana', '2019-1-24 17:00:00', '2019-1-24 23:00:00', 200, 'Finalizado') ,
(24, 6, 68, 24, 'Minnesota', 'Connecticut', '2019-4-9 19:00:00', '2019-4-9 22:45:00', 300, 'Preparandose') ,
(25, 4, 37, 25, 'Vermont', 'Massachusetts', '2019-2-5 19:00:00', '2019-2-5 22:45:00', 500, 'Preparandose') ,
(26, 8, 2, 26, 'Arizona', 'Florida', '2019-2-29 19:00:00', '2019-2-29 22:45:00', 100, 'En Proceso') ,
(27, 2, 34, 27, 'West Virginia', 'Arkansas', '2019-1-10 17:00:00', '2019-1-10 23:00:00', 100, 'Preparandose') ,
(28, 4, 12, 28, 'Pennsylvania', 'Connecticut', '2019-12-24 17:00:00', '2019-12-24 23:00:00', 100, 'En Proceso') ,
(29, 7, 29, 29, 'Idaho', 'Connecticut', '2019-5-8 01:00:00', '2019-5-8 05:30:00', 100, 'Finalizado') ,
(30, 2, 38, 30, 'Indiana', 'Montana', '2019-3-2 13:45:00', '2019-3-2 17:00:00', 100, 'Preparandose') ,
(31, 3, 28, 31, 'Virginia', 'Kentucky', '2019-2-14 17:00:00', '2019-2-14 23:00:00', 100, 'En Proceso') ,
(32, 5, 4, 32, 'New Jersey', 'South Dakota', '2019-11-9 01:00:00', '2019-11-9 05:30:00', 300, 'Preparandose') ,
(33, 4, 37, 33, 'Virginia', 'Maine', '2019-8-4 19:00:00', '2019-8-4 22:45:00', 750, 'En Proceso') ,
(34, 8, 15, 34, 'Alaska', 'Oregon', '2019-3-3 13:45:00', '2019-3-3 17:00:00', 200, 'Preparandose') ,
(35, 2, 52, 35, 'South Dakota', 'Colorado', '2019-5-14 19:00:00', '2019-5-14 22:45:00', 200, 'En Proceso') ,
(36, 4, 16, 36, 'Arkansas', 'Maine', '2019-3-13 13:45:00', '2019-3-13 17:00:00', 150, 'En Proceso') ,
(37, 4, 74, 37, 'Wyoming', 'Utah', '2019-9-31 13:45:00', '2019-9-31 17:00:00', 500, 'Finalizado') ,
(38, 3, 79, 38, 'Nebraska', 'Indiana', '2019-5-14 13:45:00', '2019-5-14 17:00:00', 750, 'En Proceso') ,
(39, 3, 59, 39, 'Oklahoma', 'Vermont', '2019-10-18 19:00:00', '2019-10-18 22:45:00', 75, 'En Proceso') ,
(40, 6, 9, 40, 'Alaska', 'New Jersey', '2019-10-29 13:45:00', '2019-10-29 17:00:00', 500, 'Preparandose') ,
(41, 7, 18, 41, 'New York', 'Nevada', '2019-12-24 19:00:00', '2019-12-24 22:45:00', 500, 'Finalizado') ,
(42, 6, 24, 42, 'Utah', 'California', '2019-2-11 13:45:00', '2019-2-11 17:00:00', 100, 'En Proceso') ,
(43, 4, 5, 43, 'Missouri', 'Delaware', '2019-10-3 01:00:00', '2019-10-3 05:30:00', 200, 'En Proceso') ,
(44, 4, 70, 44, 'New Jersey', 'Ohio', '2019-12-16 17:00:00', '2019-12-16 23:00:00', 150, 'Preparandose') ,
(45, 4, 22, 45, 'Hawaii', 'Maryland', '2019-9-31 13:45:00', '2019-9-31 17:00:00', 75, 'En Proceso') ,
(46, 5, 78, 46, 'Ohio', 'New Mexico', '2019-5-23 19:00:00', '2019-5-23 22:45:00', 500, 'En Proceso') ,
(47, 4, 25, 47, 'Arizona', 'Virginia', '2019-2-26 19:00:00', '2019-2-26 22:45:00', 300, 'Finalizado') ,
(48, 4, 62, 48, 'Indiana', 'Kansas', '2019-5-19 17:00:00', '2019-5-19 23:00:00', 500, 'Preparandose') ,
(49, 2, 6, 49, 'Ohio', 'Nevada', '2019-3-3 17:00:00', '2019-3-3 23:00:00', 150, 'En Proceso') ,
(50, 1, 45, 50, 'Wisconsin', 'Idaho', '2019-5-16 01:00:00', '2019-5-16 05:30:00', 750, 'Finalizado') ,
(51, 2, 70, 51, 'Ohio', 'New Mexico', '2019-8-27 19:00:00', '2019-8-27 22:45:00', 75, 'Finalizado') ,
(52, 1, 16, 52, 'Arizona', 'Kentucky', '2019-10-2 19:00:00', '2019-10-2 22:45:00', 300, 'Finalizado') ,
(53, 7, 75, 53, 'West Virginia', 'Missouri', '2019-9-16 01:00:00', '2019-9-16 05:30:00', 750, 'Finalizado') ,
(54, 2, 19, 54, 'North Carolina', 'California', '2019-10-8 17:00:00', '2019-10-8 23:00:00', 75, 'Preparandose') ,
(55, 6, 77, 55, 'Arizona', 'New Jersey', '2019-1-18 17:00:00', '2019-1-18 23:00:00', 100, 'En Proceso') ,
(56, 7, 4, 56, 'Kentucky', 'Louisiana', '2019-10-7 17:00:00', '2019-10-7 23:00:00', 75, 'Finalizado') ,
(57, 2, 71, 57, 'Kentucky', 'Ohio', '2019-12-2 13:45:00', '2019-12-2 17:00:00', 75, 'Finalizado') ,
(58, 7, 65, 58, 'New York', 'Minnesota', '2019-1-1 17:00:00', '2019-1-1 23:00:00', 500, 'Finalizado') ,
(59, 3, 23, 59, 'West Virginia', 'Louisiana', '2019-1-14 17:00:00', '2019-1-14 23:00:00', 75, 'Preparandose') ,
(60, 5, 34, 60, 'Alabama', 'Oregon', '2019-10-5 01:00:00', '2019-10-5 05:30:00', 100, 'Preparandose') ,
(61, 1, 8, 61, 'Massachusetts', 'Georgia', '2019-3-5 19:00:00', '2019-3-5 22:45:00', 150, 'En Proceso') ,
(62, 8, 9, 62, 'Hawaii', 'Georgia', '2019-4-19 17:00:00', '2019-4-19 23:00:00', 300, 'Finalizado') ,
(63, 4, 43, 63, 'New York', 'New Hampshire', '2019-4-14 19:00:00', '2019-4-14 22:45:00', 75, 'Finalizado') ,
(64, 4, 24, 64, 'Mississippi', 'Maryland', '2019-4-26 17:00:00', '2019-4-26 23:00:00', 100, 'Finalizado') ,
(65, 3, 62, 65, 'Nevada', 'California', '2019-2-2 19:00:00', '2019-2-2 22:45:00', 750, 'Preparandose') ,
(66, 4, 5, 66, 'Alabama', 'Indiana', '2019-12-24 17:00:00', '2019-12-24 23:00:00', 150, 'Finalizado') ,
(67, 6, 18, 67, 'New Hampshire', 'Wyoming', '2019-9-8 17:00:00', '2019-9-8 23:00:00', 200, 'En Proceso') ,
(68, 3, 8, 68, 'Kentucky', 'West Virginia', '2019-11-2 17:00:00', '2019-11-2 23:00:00', 300, 'En Proceso') ,
(69, 8, 76, 69, 'North Carolina', 'Nevada', '2019-9-17 13:45:00', '2019-9-17 17:00:00', 150, 'Finalizado') ,
(70, 5, 29, 70, 'Utah', 'Massachusetts', '2019-12-26 13:45:00', '2019-12-26 17:00:00', 75, 'Finalizado') ,
(71, 4, 30, 71, 'Massachusetts', 'Idaho', '2019-7-29 19:00:00', '2019-7-29 22:45:00', 150, 'Preparandose') ,
(72, 3, 57, 72, 'Idaho', 'Missouri', '2019-12-7 19:00:00', '2019-12-7 22:45:00', 750, 'Preparandose') ,
(73, 6, 46, 73, 'Indiana', 'Kentucky', '2019-8-14 01:00:00', '2019-8-14 05:30:00', 300, 'Preparandose') ,
(74, 2, 22, 74, 'Arkansas', 'Utah', '2019-8-12 19:00:00', '2019-8-12 22:45:00', 100, 'En Proceso') ,
(75, 7, 18, 75, 'Missouri', 'South Dakota', '2019-9-31 01:00:00', '2019-9-31 05:30:00', 100, 'En Proceso') ,
(76, 6, 2, 76, 'Rhode Island', 'Montana', '2019-3-9 17:00:00', '2019-3-9 23:00:00', 300, 'En Proceso') ,
(77, 2, 21, 77, 'Kentucky', 'Kansas', '2019-6-8 19:00:00', '2019-6-8 22:45:00', 200, 'En Proceso') ,
(78, 8, 31, 78, 'South Carolina', 'Kentucky', '2019-5-3 01:00:00', '2019-5-3 05:30:00', 500, 'Preparandose') ,
(79, 6, 5, 79, 'Missouri', 'New Hampshire', '2019-1-11 17:00:00', '2019-1-11 23:00:00', 75, 'Preparandose') ,
(80, 6, 79, 80, 'Ohio', 'New York', '2019-7-23 01:00:00', '2019-7-23 05:30:00', 750, 'Finalizado') ,
(81, 7, 41, 81, 'South Carolina', 'Iowa', '2019-1-24 01:00:00', '2019-1-24 05:30:00', 750, 'En Proceso') ,
(82, 5, 48, 82, 'Maine', 'Utah', '2019-1-27 01:00:00', '2019-1-27 05:30:00', 300, 'Finalizado') ,
(83, 1, 17, 83, 'Oregon', 'Minnesota', '2019-8-18 13:45:00', '2019-8-18 17:00:00', 300, 'Finalizado') ,
(84, 5, 48, 84, 'Idaho', 'Missouri', '2019-6-28 17:00:00', '2019-6-28 23:00:00', 150, 'Preparandose') ,
(85, 3, 27, 85, 'New Hampshire', 'West Virginia', '2019-2-23 01:00:00', '2019-2-23 05:30:00', 750, 'Finalizado') ,
(86, 1, 45, 86, 'Kentucky', 'Arkansas', '2019-8-31 17:00:00', '2019-8-31 23:00:00', 300, 'Finalizado') ,
(87, 6, 7, 87, 'Vermont', 'New Jersey', '2019-6-12 13:45:00', '2019-6-12 17:00:00', 300, 'Preparandose') ,
(88, 3, 67, 88, 'Louisiana', 'Kentucky', '2019-9-13 19:00:00', '2019-9-13 22:45:00', 100, 'Preparandose') ,
(89, 5, 19, 89, 'Pennsylvania', 'Utah', '2019-6-23 19:00:00', '2019-6-23 22:45:00', 75, 'Finalizado') ,
(90, 7, 37, 90, 'California', 'Michigan', '2019-12-26 19:00:00', '2019-12-26 22:45:00', 500, 'Preparandose') ,
(91, 1, 43, 91, 'Massachusetts', 'North Dakota', '2019-8-24 01:00:00', '2019-8-24 05:30:00', 300, 'Preparandose') ,
(92, 8, 7, 92, 'Ohio', 'Massachusetts', '2019-5-28 01:00:00', '2019-5-28 05:30:00', 300, 'Preparandose') ,
(93, 5, 53, 93, 'Colorado', 'Tennessee', '2019-10-25 19:00:00', '2019-10-25 22:45:00', 100, 'Preparandose') ,
(94, 2, 69, 94, 'Wyoming', 'West Virginia', '2019-6-8 19:00:00', '2019-6-8 22:45:00', 500, 'En Proceso') ,
(95, 3, 1, 95, 'Mississippi', 'Illinois', '2019-5-4 19:00:00', '2019-5-4 22:45:00', 150, 'Finalizado') ,
(96, 2, 60, 96, 'Alabama', 'South Carolina', '2019-10-7 01:00:00', '2019-10-7 05:30:00', 75, 'En Proceso') ,
(97, 1, 16, 97, 'Arkansas', 'Wisconsin', '2019-4-5 17:00:00', '2019-4-5 23:00:00', 300, 'Finalizado') ,
(98, 3, 16, 98, 'Georgia', 'Oregon', '2019-4-9 13:45:00', '2019-4-9 17:00:00', 300, 'Preparandose') ,
(99, 1, 47, 99, 'Maryland', 'Wyoming', '2019-5-23 19:00:00', '2019-5-23 22:45:00', 300, 'Preparandose') ,
(100, 2, 59, 100, 'Montana', 'Delaware', '2019-8-25 17:00:00', '2019-8-25 23:00:00', 200, 'Finalizado') ,
(101, 5, 49, 101, 'Oregon', 'Illinois', '2019-3-6 17:00:00', '2019-3-6 23:00:00', 200, 'Finalizado') ,
(102, 5, 53, 102, 'California', 'Kansas', '2019-5-4 19:00:00', '2019-5-4 22:45:00', 750, 'Preparandose') ,
(103, 6, 30, 103, 'Montana', 'Missouri', '2019-4-10 13:45:00', '2019-4-10 17:00:00', 750, 'En Proceso') ,
(104, 2, 53, 104, 'Texas', 'Michigan', '2019-9-27 19:00:00', '2019-9-27 22:45:00', 200, 'Preparandose') ,
(105, 7, 21, 105, 'Maryland', 'South Carolina', '2019-3-23 01:00:00', '2019-3-23 05:30:00', 300, 'Finalizado') ,
(106, 3, 1, 106, 'Vermont', 'Massachusetts', '2019-7-24 13:45:00', '2019-7-24 17:00:00', 300, 'Preparandose') ,
(107, 4, 70, 107, 'Indiana', 'Wisconsin', '2019-6-21 13:45:00', '2019-6-21 17:00:00', 750, 'Preparandose') ,
(108, 1, 1, 108, 'Kentucky', 'South Dakota', '2019-6-25 17:00:00', '2019-6-25 23:00:00', 100, 'Finalizado') ,
(109, 7, 10, 109, 'North Dakota', 'Montana', '2019-11-3 19:00:00', '2019-11-3 22:45:00', 150, 'Finalizado') ,
(110, 8, 58, 110, 'Pennsylvania', 'Virginia', '2019-11-19 13:45:00', '2019-11-19 17:00:00', 75, 'Finalizado') ,
(111, 6, 66, 111, 'Nevada', 'Maryland', '2019-7-7 13:45:00', '2019-7-7 17:00:00', 150, 'Preparandose') ,
(112, 3, 22, 112, 'Missouri', 'New Hampshire', '2019-11-2 19:00:00', '2019-11-2 22:45:00', 75, 'Preparandose') ,
(113, 7, 76, 113, 'Indiana', 'Massachusetts', '2019-1-30 19:00:00', '2019-1-30 22:45:00', 750, 'En Proceso') ,
(114, 4, 58, 114, 'Oregon', 'Missouri', '2019-5-8 01:00:00', '2019-5-8 05:30:00', 300, 'En Proceso') ,
(115, 3, 72, 115, 'Alabama', 'North Carolina', '2019-8-6 19:00:00', '2019-8-6 22:45:00', 750, 'En Proceso') ,
(116, 5, 63, 116, 'Illinois', 'West Virginia', '2019-8-8 01:00:00', '2019-8-8 05:30:00', 750, 'Finalizado') ,
(117, 1, 76, 117, 'North Carolina', 'New Hampshire', '2019-3-8 13:45:00', '2019-3-8 17:00:00', 150, 'Finalizado') ,
(118, 6, 2, 118, 'New Jersey', 'Louisiana', '2019-10-1 17:00:00', '2019-10-1 23:00:00', 200, 'En Proceso') ,
(119, 5, 76, 119, 'Maine', 'Tennessee', '2019-2-13 17:00:00', '2019-2-13 23:00:00', 150, 'Preparandose') ,
(120, 7, 52, 120, 'Louisiana', 'Connecticut', '2019-12-9 19:00:00', '2019-12-9 22:45:00', 75, 'En Proceso') ,
(121, 8, 45, 121, 'Idaho', 'Texas', '2019-2-7 01:00:00', '2019-2-7 05:30:00', 500, 'Preparandose') ,
(122, 7, 3, 122, 'Connecticut', 'New Jersey', '2019-5-29 13:45:00', '2019-5-29 17:00:00', 75, 'Preparandose') ,
(123, 7, 18, 123, 'Alabama', 'Connecticut', '2019-11-16 01:00:00', '2019-11-16 05:30:00', 300, 'Finalizado') ,
(124, 5, 28, 124, 'South Carolina', 'Wisconsin', '2019-12-17 19:00:00', '2019-12-17 22:45:00', 750, 'Preparandose') ,
(125, 6, 39, 125, 'West Virginia', 'Oklahoma', '2019-12-23 01:00:00', '2019-12-23 05:30:00', 200, 'Preparandose') ,
(126, 3, 13, 126, 'Kansas', 'Maine', '2019-3-26 01:00:00', '2019-3-26 05:30:00', 100, 'En Proceso') ,
(127, 2, 56, 127, 'New Hampshire', 'Oregon', '2019-11-29 19:00:00', '2019-11-29 22:45:00', 100, 'Preparandose') ,
(128, 5, 40, 128, 'Nebraska', 'Oregon', '2019-8-16 19:00:00', '2019-8-16 22:45:00', 150, 'En Proceso') ,
(129, 6, 57, 129, 'South Carolina', 'Utah', '2019-11-11 19:00:00', '2019-11-11 22:45:00', 100, 'En Proceso') ,
(130, 4, 24, 130, 'Georgia', 'Delaware', '2019-11-31 17:00:00', '2019-11-31 23:00:00', 75, 'Preparandose') ,
(131, 4, 44, 131, 'Montana', 'Vermont', '2019-11-26 13:45:00', '2019-11-26 17:00:00', 75, 'Preparandose') ,
(132, 2, 33, 132, 'Connecticut', 'Missouri', '2019-10-16 17:00:00', '2019-10-16 23:00:00', 500, 'Finalizado') ,
(133, 3, 9, 133, 'Missouri', 'Indiana', '2019-8-24 01:00:00', '2019-8-24 05:30:00', 750, 'En Proceso') ,
(134, 4, 15, 134, 'Pennsylvania', 'Colorado', '2019-9-2 17:00:00', '2019-9-2 23:00:00', 500, 'En Proceso') ,
(135, 5, 10, 135, 'Rhode Island', 'Kansas', '2019-6-21 13:45:00', '2019-6-21 17:00:00', 750, 'Finalizado') ,
(136, 6, 26, 136, 'Alaska', 'Maryland', '2019-12-29 01:00:00', '2019-12-29 05:30:00', 75, 'Preparandose') ,
(137, 4, 45, 137, 'Iowa', 'Louisiana', '2019-3-1 01:00:00', '2019-3-1 05:30:00', 300, 'En Proceso') ,
(138, 1, 77, 138, 'New Mexico', 'Colorado', '2019-4-28 19:00:00', '2019-4-28 22:45:00', 300, 'Preparandose') ,
(139, 2, 49, 139, 'Washington', 'Oregon', '2019-5-15 13:45:00', '2019-5-15 17:00:00', 750, 'Finalizado') ,
(140, 5, 27, 140, 'Utah', 'Kansas', '2019-9-19 17:00:00', '2019-9-19 23:00:00', 100, 'Finalizado') ,
(141, 2, 71, 141, 'Missouri', 'Kansas', '2019-9-9 01:00:00', '2019-9-9 05:30:00', 500, 'Preparandose') ,
(142, 1, 38, 142, 'Michigan', 'New Mexico', '2019-8-7 01:00:00', '2019-8-7 05:30:00', 100, 'Preparandose') ,
(143, 8, 61, 143, 'North Carolina', 'Connecticut', '2019-7-3 01:00:00', '2019-7-3 05:30:00', 200, 'Finalizado') ,
(144, 7, 6, 144, 'Hawaii', 'Missouri', '2019-9-31 13:45:00', '2019-9-31 17:00:00', 750, 'En Proceso') ,
(145, 7, 6, 145, 'Alaska', 'Missouri', '2019-11-20 01:00:00', '2019-11-20 05:30:00', 150, 'Finalizado') ,
(146, 3, 5, 146, 'Mississippi', 'Nebraska', '2019-9-26 13:45:00', '2019-9-26 17:00:00', 200, 'Finalizado') ,
(147, 3, 71, 147, 'Hawaii', 'New York', '2019-4-15 01:00:00', '2019-4-15 05:30:00', 750, 'Finalizado') ,
(148, 2, 16, 148, 'New Hampshire', 'Maine', '2019-7-4 19:00:00', '2019-7-4 22:45:00', 750, 'Finalizado') ,
(149, 2, 26, 149, 'Arizona', 'South Carolina', '2019-8-20 13:45:00', '2019-8-20 17:00:00', 200, 'Finalizado') ,
(150, 5, 32, 150, 'South Dakota', 'Kentucky', '2019-12-9 13:45:00', '2019-12-9 17:00:00', 750, 'Preparandose') ,
(151, 6, 8, 151, 'Texas', 'Virginia', '2019-4-12 17:00:00', '2019-4-12 23:00:00', 200, 'En Proceso') ,
(152, 7, 8, 152, 'Alaska', 'New Jersey', '2019-8-24 17:00:00', '2019-8-24 23:00:00', 150, 'En Proceso') ,
(153, 8, 68, 153, 'Wyoming', 'Pennsylvania', '2019-9-1 19:00:00', '2019-9-1 22:45:00', 500, 'Preparandose') ,
(154, 5, 80, 154, 'Arkansas', 'North Carolina', '2019-10-20 19:00:00', '2019-10-20 22:45:00', 150, 'Preparandose') ,
(155, 3, 4, 155, 'Arizona', 'Massachusetts', '2019-3-3 13:45:00', '2019-3-3 17:00:00', 750, 'Preparandose') ,
(156, 5, 6, 156, 'North Carolina', 'New Mexico', '2019-1-8 13:45:00', '2019-1-8 17:00:00', 500, 'Preparandose') ,
(157, 8, 35, 157, 'Kentucky', 'Illinois', '2019-2-16 19:00:00', '2019-2-16 22:45:00', 500, 'Finalizado') ,
(158, 5, 14, 158, 'New Mexico', 'Wisconsin', '2019-1-7 13:45:00', '2019-1-7 17:00:00', 300, 'Finalizado') ,
(159, 3, 25, 159, 'South Carolina', 'North Dakota', '2019-3-2 17:00:00', '2019-3-2 23:00:00', 750, 'En Proceso') ,
(160, 4, 65, 160, 'South Dakota', 'Florida', '2019-2-24 13:45:00', '2019-2-24 17:00:00', 200, 'En Proceso') ,
(161, 8, 6, 161, 'Rhode Island', 'New York', '2019-9-10 13:45:00', '2019-9-10 17:00:00', 100, 'Finalizado') ,
(162, 6, 37, 162, 'Tennessee', 'Indiana', '2019-9-24 13:45:00', '2019-9-24 17:00:00', 200, 'Preparandose') ,
(163, 3, 11, 163, 'Missouri', 'Pennsylvania', '2019-3-16 13:45:00', '2019-3-16 17:00:00', 300, 'Preparandose') ,
(164, 6, 65, 164, 'Texas', 'South Carolina', '2019-10-10 01:00:00', '2019-10-10 05:30:00', 150, 'Finalizado') ,
(165, 5, 70, 165, 'Nevada', 'Rhode Island', '2019-3-6 01:00:00', '2019-3-6 05:30:00', 100, 'En Proceso') ,
(166, 2, 78, 166, 'Tennessee', 'New Jersey', '2019-10-18 01:00:00', '2019-10-18 05:30:00', 100, 'En Proceso') ,
(167, 1, 13, 167, 'Nevada', 'Nebraska', '2019-3-9 17:00:00', '2019-3-9 23:00:00', 75, 'En Proceso') ,
(168, 8, 39, 168, 'Arkansas', 'Virginia', '2019-5-6 01:00:00', '2019-5-6 05:30:00', 100, 'En Proceso') ,
(169, 6, 33, 169, 'Minnesota', 'Iowa', '2019-5-12 13:45:00', '2019-5-12 17:00:00', 150, 'Finalizado') ,
(170, 7, 26, 170, 'Delaware', 'Massachusetts', '2019-1-14 19:00:00', '2019-1-14 22:45:00', 75, 'Preparandose') ,
(171, 7, 1, 171, 'Mississippi', 'Louisiana', '2019-9-11 13:45:00', '2019-9-11 17:00:00', 750, 'En Proceso') ,
(172, 1, 2, 172, 'New Jersey', 'Kansas', '2019-11-20 13:45:00', '2019-11-20 17:00:00', 750, 'Preparandose') ,
(173, 2, 78, 173, 'Alabama', 'West Virginia', '2019-7-18 17:00:00', '2019-7-18 23:00:00', 750, 'En Proceso') ,
(174, 7, 53, 174, 'Wisconsin', 'Missouri', '2019-12-8 17:00:00', '2019-12-8 23:00:00', 150, 'Preparandose') ,
(175, 6, 5, 175, 'Maryland', 'Nevada', '2019-3-21 17:00:00', '2019-3-21 23:00:00', 75, 'Finalizado') ,
(176, 5, 11, 176, 'Georgia', 'Maine', '2019-6-19 19:00:00', '2019-6-19 22:45:00', 300, 'En Proceso') ,
(177, 7, 12, 177, 'Washington', 'Iowa', '2019-7-31 01:00:00', '2019-7-31 05:30:00', 200, 'En Proceso') ,
(178, 1, 32, 178, 'Virginia', 'Washington', '2019-11-10 01:00:00', '2019-11-10 05:30:00', 100, 'Preparandose') ,
(179, 5, 5, 179, 'Alaska', 'Kentucky', '2019-5-19 01:00:00', '2019-5-19 05:30:00', 150, 'Preparandose') ,
(180, 5, 21, 180, 'Alaska', 'Connecticut', '2019-1-23 13:45:00', '2019-1-23 17:00:00', 300, 'Finalizado') ,
(181, 7, 32, 181, 'Maryland', 'Vermont', '2019-5-28 19:00:00', '2019-5-28 22:45:00', 200, 'Preparandose') ,
(182, 7, 11, 182, 'Arizona', 'Colorado', '2019-6-28 01:00:00', '2019-6-28 05:30:00', 150, 'Preparandose') ,
(183, 5, 58, 183, 'Maine', 'Oklahoma', '2019-9-7 17:00:00', '2019-9-7 23:00:00', 500, 'Finalizado') ,
(184, 4, 70, 184, 'Nevada', 'New Jersey', '2019-4-2 01:00:00', '2019-4-2 05:30:00', 200, 'Finalizado') ,
(185, 7, 9, 185, 'Vermont', 'Missouri', '2019-6-9 13:45:00', '2019-6-9 17:00:00', 500, 'En Proceso') ,
(186, 5, 56, 186, 'Colorado', 'Oregon', '2019-6-30 13:45:00', '2019-6-30 17:00:00', 75, 'Finalizado') ,
(187, 4, 46, 187, 'Iowa', 'West Virginia', '2019-3-23 19:00:00', '2019-3-23 22:45:00', 75, 'Finalizado') ,
(188, 1, 38, 188, 'Mississippi', 'South Dakota', '2019-1-21 01:00:00', '2019-1-21 05:30:00', 75, 'Preparandose') ,
(189, 2, 43, 189, 'Florida', 'Texas', '2019-11-15 17:00:00', '2019-11-15 23:00:00', 100, 'En Proceso') ,
(190, 4, 65, 190, 'South Dakota', 'Oklahoma', '2019-9-27 19:00:00', '2019-9-27 22:45:00', 500, 'Finalizado') ,
(191, 4, 79, 191, 'Nevada', 'Colorado', '2019-1-8 17:00:00', '2019-1-8 23:00:00', 200, 'Preparandose') ,
(192, 2, 41, 192, 'Maine', 'Wisconsin', '2019-3-1 13:45:00', '2019-3-1 17:00:00', 200, 'Preparandose') ,
(193, 5, 67, 193, 'Massachusetts', 'Idaho', '2019-9-30 13:45:00', '2019-9-30 17:00:00', 100, 'Preparandose') ,
(194, 4, 39, 194, 'North Carolina', 'Minnesota', '2019-2-27 19:00:00', '2019-2-27 22:45:00', 100, 'Finalizado') ,
(195, 7, 68, 195, 'Kansas', 'Kentucky', '2019-4-11 01:00:00', '2019-4-11 05:30:00', 300, 'En Proceso') ,
(196, 2, 56, 196, 'Georgia', 'Pennsylvania', '2019-7-1 01:00:00', '2019-7-1 05:30:00', 150, 'En Proceso') ,
(197, 8, 25, 197, 'New Hampshire', 'Arkansas', '2019-11-29 19:00:00', '2019-11-29 22:45:00', 150, 'Finalizado') ,
(198, 5, 77, 198, 'Wisconsin', 'Arizona', '2019-12-29 19:00:00', '2019-12-29 22:45:00', 200, 'En Proceso') ,
(199, 7, 36, 199, 'Utah', 'Michigan', '2019-10-30 19:00:00', '2019-10-30 22:45:00', 75, 'Preparandose') ,
(200, 4, 63, 200, 'Louisiana', 'West Virginia', '2019-11-8 19:00:00', '2019-11-8 22:45:00', 75, 'Preparandose') ,
(201, 8, 2, 201, 'West Virginia', 'Missouri', '2019-5-25 13:45:00', '2019-5-25 17:00:00', 750, 'Finalizado') ,
(202, 4, 22, 202, 'Texas', 'New Hampshire', '2019-4-7 13:45:00', '2019-4-7 17:00:00', 300, 'Finalizado') ,
(203, 5, 37, 203, 'Maryland', 'Oregon', '2019-9-27 19:00:00', '2019-9-27 22:45:00', 200, 'Finalizado') ,
(204, 1, 12, 204, 'Virginia', 'Connecticut', '2019-9-21 17:00:00', '2019-9-21 23:00:00', 300, 'Preparandose') ,
(205, 8, 5, 205, 'Delaware', 'Alaska', '2019-2-2 01:00:00', '2019-2-2 05:30:00', 750, 'En Proceso') ,
(206, 2, 13, 206, 'New York', 'Maryland', '2019-10-11 13:45:00', '2019-10-11 17:00:00', 150, 'En Proceso') ,
(207, 2, 44, 207, 'Colorado', 'Delaware', '2019-9-16 19:00:00', '2019-9-16 22:45:00', 300, 'En Proceso') ,
(208, 6, 33, 208, 'Vermont', 'Texas', '2019-7-29 17:00:00', '2019-7-29 23:00:00', 200, 'Finalizado') ,
(209, 1, 67, 209, 'Vermont', 'Montana', '2019-2-10 01:00:00', '2019-2-10 05:30:00', 200, 'Finalizado') ,
(210, 5, 43, 210, 'Wisconsin', 'New Mexico', '2019-8-6 17:00:00', '2019-8-6 23:00:00', 500, 'Finalizado') ,
(211, 3, 49, 211, 'Illinois', 'Texas', '2019-4-4 01:00:00', '2019-4-4 05:30:00', 200, 'En Proceso') ,
(212, 1, 11, 212, 'Hawaii', 'Alaska', '2019-4-22 17:00:00', '2019-4-22 23:00:00', 750, 'Finalizado') ,
(213, 8, 74, 213, 'Kentucky', 'Wyoming', '2019-11-19 17:00:00', '2019-11-19 23:00:00', 200, 'Finalizado') ,
(214, 3, 52, 214, 'New Mexico', 'Florida', '2019-6-28 01:00:00', '2019-6-28 05:30:00', 300, 'En Proceso') ,
(215, 6, 56, 215, 'Montana', 'Wyoming', '2019-6-24 13:45:00', '2019-6-24 17:00:00', 300, 'Preparandose') ,
(216, 7, 39, 216, 'Colorado', 'Maryland', '2019-5-18 01:00:00', '2019-5-18 05:30:00', 200, 'Finalizado') ,
(217, 2, 26, 217, 'Louisiana', 'Hawaii', '2019-6-21 19:00:00', '2019-6-21 22:45:00', 750, 'Finalizado') ,
(218, 4, 8, 218, 'Texas', 'Nebraska', '2019-1-10 19:00:00', '2019-1-10 22:45:00', 300, 'Finalizado') ,
(219, 8, 28, 219, 'Illinois', 'Pennsylvania', '2019-2-2 13:45:00', '2019-2-2 17:00:00', 100, 'Finalizado') ,
(220, 1, 3, 220, 'New Hampshire', 'Montana', '2019-9-18 01:00:00', '2019-9-18 05:30:00', 200, 'En Proceso') ,
(221, 6, 26, 221, 'Florida', 'Virginia', '2019-2-24 13:45:00', '2019-2-24 17:00:00', 75, 'Finalizado') ,
(222, 7, 74, 222, 'Michigan', 'Kansas', '2019-12-8 17:00:00', '2019-12-8 23:00:00', 75, 'En Proceso') ,
(223, 6, 55, 223, 'Maine', 'New Mexico', '2019-10-13 13:45:00', '2019-10-13 17:00:00', 100, 'En Proceso') ,
(224, 6, 10, 224, 'Nebraska', 'Kansas', '2019-1-8 01:00:00', '2019-1-8 05:30:00', 100, 'En Proceso') ,
(225, 4, 48, 225, 'Louisiana', 'New Mexico', '2019-1-29 17:00:00', '2019-1-29 23:00:00', 150, 'En Proceso') ,
(226, 7, 76, 226, 'Virginia', 'Texas', '2019-12-2 17:00:00', '2019-12-2 23:00:00', 100, 'Preparandose') ,
(227, 2, 56, 227, 'Washington', 'Ohio', '2019-3-31 01:00:00', '2019-3-31 05:30:00', 150, 'En Proceso') ,
(228, 3, 71, 228, 'Utah', 'Florida', '2019-1-6 17:00:00', '2019-1-6 23:00:00', 200, 'En Proceso') ,
(229, 1, 42, 229, 'Virginia', 'Washington', '2019-12-5 19:00:00', '2019-12-5 22:45:00', 500, 'Finalizado') ,
(230, 3, 13, 230, 'Maryland', 'California', '2019-4-27 17:00:00', '2019-4-27 23:00:00', 200, 'Preparandose') ,
(231, 2, 10, 231, 'West Virginia', 'Oklahoma', '2019-3-28 19:00:00', '2019-3-28 22:45:00', 300, 'Preparandose') ,
(232, 1, 71, 232, 'Utah', 'Connecticut', '2019-3-21 01:00:00', '2019-3-21 05:30:00', 500, 'Finalizado') ,
(233, 3, 43, 233, 'Connecticut', 'New Mexico', '2019-6-11 19:00:00', '2019-6-11 22:45:00', 100, 'Preparandose') ,
(234, 8, 30, 234, 'Kentucky', 'New Jersey', '2019-10-29 19:00:00', '2019-10-29 22:45:00', 750, 'Preparandose') ,
(235, 5, 72, 235, 'Louisiana', 'Maryland', '2019-3-8 17:00:00', '2019-3-8 23:00:00', 200, 'En Proceso') ,
(236, 7, 47, 236, 'New Hampshire', 'Connecticut', '2019-12-31 19:00:00', '2019-12-31 22:45:00', 75, 'En Proceso') ,
(237, 1, 6, 237, 'Idaho', 'Rhode Island', '2019-6-2 19:00:00', '2019-6-2 22:45:00', 200, 'Preparandose') ,
(238, 1, 19, 238, 'New Hampshire', 'Illinois', '2019-5-5 17:00:00', '2019-5-5 23:00:00', 100, 'Preparandose') ,
(239, 8, 66, 239, 'Rhode Island', 'West Virginia', '2019-11-26 17:00:00', '2019-11-26 23:00:00', 150, 'Preparandose') ,
(240, 1, 38, 240, 'Alaska', 'Texas', '2019-10-20 01:00:00', '2019-10-20 05:30:00', 75, 'En Proceso') ,
(241, 5, 49, 241, 'North Dakota', 'New York', '2019-7-20 13:45:00', '2019-7-20 17:00:00', 500, 'Finalizado') ,
(242, 5, 70, 242, 'Arizona', 'Ohio', '2019-12-10 13:45:00', '2019-12-10 17:00:00', 75, 'Preparandose') ,
(243, 1, 18, 243, 'Texas', 'South Carolina', '2019-5-11 19:00:00', '2019-5-11 22:45:00', 75, 'Finalizado') ,
(244, 2, 1, 244, 'Virginia', 'Montana', '2019-7-18 17:00:00', '2019-7-18 23:00:00', 200, 'En Proceso') ,
(245, 4, 33, 245, 'Louisiana', 'Missouri', '2019-1-27 17:00:00', '2019-1-27 23:00:00', 300, 'Finalizado') ,
(246, 5, 66, 246, 'Utah', 'Virginia', '2019-8-14 17:00:00', '2019-8-14 23:00:00', 750, 'Finalizado') ,
(247, 6, 46, 247, 'Ohio', 'Maryland', '2019-10-1 01:00:00', '2019-10-1 05:30:00', 300, 'En Proceso') ,
(248, 7, 16, 248, 'South Dakota', 'Texas', '2019-6-30 13:45:00', '2019-6-30 17:00:00', 500, 'En Proceso') ,
(249, 3, 36, 249, 'Massachusetts', 'Kentucky', '2019-4-17 19:00:00', '2019-4-17 22:45:00', 75, 'En Proceso') ,
(250, 8, 20, 250, 'Iowa', 'North Carolina', '2019-7-10 17:00:00', '2019-7-10 23:00:00', 200, 'Finalizado') ,
(251, 5, 49, 251, 'Iowa', 'Alaska', '2019-5-27 19:00:00', '2019-5-27 22:45:00', 150, 'Finalizado') ,
(252, 1, 26, 252, 'Rhode Island', 'South Dakota', '2019-3-12 19:00:00', '2019-3-12 22:45:00', 200, 'En Proceso') ,
(253, 3, 28, 253, 'Kansas', 'California', '2019-5-7 19:00:00', '2019-5-7 22:45:00', 500, 'Finalizado') ,
(254, 5, 49, 254, 'Maine', 'North Carolina', '2019-10-16 13:45:00', '2019-10-16 17:00:00', 100, 'Preparandose') ,
(255, 8, 65, 255, 'California', 'Kansas', '2019-1-19 19:00:00', '2019-1-19 22:45:00', 200, 'Preparandose') ,
(256, 7, 24, 256, 'West Virginia', 'Wyoming', '2019-2-29 19:00:00', '2019-2-29 22:45:00', 75, 'En Proceso') ,
(257, 7, 72, 257, 'Colorado', 'Iowa', '2019-11-3 13:45:00', '2019-11-3 17:00:00', 300, 'Preparandose') ,
(258, 8, 50, 258, 'Virginia', 'Utah', '2019-8-31 19:00:00', '2019-8-31 22:45:00', 500, 'Preparandose') ,
(259, 2, 74, 259, 'Alaska', 'Connecticut', '2019-2-29 13:45:00', '2019-2-29 17:00:00', 500, 'Preparandose') ,
(260, 6, 55, 260, 'North Dakota', 'Alabama', '2019-7-5 01:00:00', '2019-7-5 05:30:00', 100, 'Finalizado') ,
(261, 3, 7, 261, 'Oklahoma', 'New Jersey', '2019-5-11 13:45:00', '2019-5-11 17:00:00', 750, 'En Proceso') ,
(262, 5, 61, 262, 'Texas', 'South Carolina', '2019-10-16 19:00:00', '2019-10-16 22:45:00', 200, 'Finalizado') ,
(263, 4, 24, 263, 'Delaware', 'Virginia', '2019-9-25 17:00:00', '2019-9-25 23:00:00', 750, 'Preparandose') ,
(264, 7, 37, 264, 'Maryland', 'South Carolina', '2019-8-28 01:00:00', '2019-8-28 05:30:00', 100, 'Finalizado') ,
(265, 6, 64, 265, 'Colorado', 'Arkansas', '2019-9-8 19:00:00', '2019-9-8 22:45:00', 300, 'Finalizado') ,
(266, 3, 44, 266, 'Arkansas', 'New York', '2019-2-17 17:00:00', '2019-2-17 23:00:00', 750, 'En Proceso') ,
(267, 5, 65, 267, 'Delaware', 'Illinois', '2019-12-22 17:00:00', '2019-12-22 23:00:00', 100, 'Preparandose') ,
(268, 8, 6, 268, 'Rhode Island', 'Wyoming', '2019-12-28 13:45:00', '2019-12-28 17:00:00', 500, 'Preparandose') ,
(269, 8, 34, 269, 'Montana', 'Connecticut', '2019-12-9 13:45:00', '2019-12-9 17:00:00', 750, 'Preparandose') ,
(270, 6, 15, 270, 'New Mexico', 'Arkansas', '2019-2-15 17:00:00', '2019-2-15 23:00:00', 75, 'Finalizado') ,
(271, 3, 28, 271, 'Ohio', 'Louisiana', '2019-7-23 17:00:00', '2019-7-23 23:00:00', 150, 'Preparandose') ,
(272, 3, 74, 272, 'New Hampshire', 'California', '2019-5-22 19:00:00', '2019-5-22 22:45:00', 75, 'Finalizado') ,
(273, 3, 45, 273, 'California', 'Louisiana', '2019-12-16 19:00:00', '2019-12-16 22:45:00', 100, 'En Proceso') ,
(274, 5, 77, 274, 'Iowa', 'Ohio', '2019-8-10 13:45:00', '2019-8-10 17:00:00', 300, 'Preparandose') ,
(275, 5, 64, 275, 'Kansas', 'Mississippi', '2019-5-17 17:00:00', '2019-5-17 23:00:00', 150, 'Preparandose') ,
(276, 2, 20, 276, 'New Jersey', 'Colorado', '2019-5-18 01:00:00', '2019-5-18 05:30:00', 100, 'Preparandose') ,
(277, 1, 55, 277, 'Maine', 'Massachusetts', '2019-11-22 17:00:00', '2019-11-22 23:00:00', 300, 'En Proceso') ,
(278, 5, 59, 278, 'Wisconsin', 'Arkansas', '2019-3-30 17:00:00', '2019-3-30 23:00:00', 300, 'Preparandose') ,
(279, 1, 38, 279, 'Georgia', 'New Jersey', '2019-8-23 19:00:00', '2019-8-23 22:45:00', 300, 'Finalizado') ,
(280, 3, 47, 280, 'New Hampshire', 'Montana', '2019-12-1 01:00:00', '2019-12-1 05:30:00', 750, 'Preparandose') ,
(281, 1, 8, 281, 'Indiana', 'Oregon', '2019-5-25 13:45:00', '2019-5-25 17:00:00', 100, 'En Proceso') ,
(282, 3, 6, 282, 'Virginia', 'Nevada', '2019-7-8 17:00:00', '2019-7-8 23:00:00', 150, 'Finalizado') ,
(283, 8, 37, 283, 'Maine', 'Florida', '2019-1-3 01:00:00', '2019-1-3 05:30:00', 750, 'En Proceso') ,
(284, 5, 18, 284, 'Rhode Island', 'Montana', '2019-4-13 17:00:00', '2019-4-13 23:00:00', 100, 'Finalizado') ,
(285, 2, 42, 285, 'Oregon', 'Pennsylvania', '2019-9-20 19:00:00', '2019-9-20 22:45:00', 200, 'Preparandose') ,
(286, 2, 67, 286, 'Oklahoma', 'North Dakota', '2019-4-10 01:00:00', '2019-4-10 05:30:00', 100, 'En Proceso') ,
(287, 2, 34, 287, 'New Mexico', 'Georgia', '2019-3-11 19:00:00', '2019-3-11 22:45:00', 200, 'En Proceso') ,
(288, 1, 55, 288, 'Mississippi', 'Oregon', '2019-3-30 13:45:00', '2019-3-30 17:00:00', 500, 'Preparandose') ,
(289, 1, 37, 289, 'Alabama', 'Arizona', '2019-11-6 17:00:00', '2019-11-6 23:00:00', 150, 'En Proceso') ,
(290, 5, 76, 290, 'Connecticut', 'Wyoming', '2019-5-6 19:00:00', '2019-5-6 22:45:00', 200, 'Finalizado') ,
(291, 3, 46, 291, 'Oregon', 'Ohio', '2019-9-16 19:00:00', '2019-9-16 22:45:00', 75, 'En Proceso') ,
(292, 2, 4, 292, 'Indiana', 'Washington', '2019-8-11 17:00:00', '2019-8-11 23:00:00', 500, 'Finalizado') ,
(293, 4, 35, 293, 'Georgia', 'Maryland', '2019-11-26 01:00:00', '2019-11-26 05:30:00', 150, 'Preparandose') ,
(294, 5, 60, 294, 'Tennessee', 'Michigan', '2019-4-12 13:45:00', '2019-4-12 17:00:00', 150, 'Finalizado') ,
(295, 5, 66, 295, 'Texas', 'Alabama', '2019-7-21 01:00:00', '2019-7-21 05:30:00', 100, 'Finalizado') ,
(296, 8, 12, 296, 'Nevada', 'North Dakota', '2019-11-22 01:00:00', '2019-11-22 05:30:00', 200, 'Preparandose') ,
(297, 7, 4, 297, 'Arkansas', 'Rhode Island', '2019-12-21 13:45:00', '2019-12-21 17:00:00', 500, 'Finalizado') ,
(298, 2, 11, 298, 'Washington', 'Indiana', '2019-12-11 13:45:00', '2019-12-11 17:00:00', 500, 'En Proceso') ,
(299, 1, 32, 299, 'Oklahoma', 'Florida', '2019-5-27 13:45:00', '2019-5-27 17:00:00', 150, 'En Proceso') ,
(300, 7, 80, 300, 'Alaska', 'Texas', '2019-4-3 01:00:00', '2019-4-3 05:30:00', 500, 'En Proceso')]

createControladorVuelo(listaAviones,listaVuelos)