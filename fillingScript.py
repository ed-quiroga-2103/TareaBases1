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
    querryList = []
    for i in range(30):
        for j in range(choice(range(15))+1):
            
            querry = (choice(range(25))+1, i+1)
            querryList.append(querry)
    return querryList
            
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
    querryList = []
    for i in range(300):
        
        idAvion = choice(range(80))+1
        idAero = choice(range(25))+1

        origin = choice(linesToList("aeropuertos.txt"))
        destiny = choice(linesToList("aeropuertos.txt"))

        while origin == destiny:
            destiny = choice(linesToList("aeropuertos.txt"))    

        querry = createVuelo(i+1, idAero, idAvion, origin, destiny)
        querryList.append(querry)
    return querryList

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

    listAerolineas = randPickNamesNoRepeat(linesToList(fileAerolineas),25)
    listAeropuertos = randPickNamesNoRepeat(linesToList(fileAeropuertos),30)

    for i in range(25):

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

        
        aeroId = choice(range(25))

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

def getAviones(numAviones):
    querryList = []
    manufactList = linesToList("fabricantes.txt")
    modelList = randPickNamesNoRepeat(linesToList("modelos.txt"), 80)
    idNum = 0
    for i in range(25):

        for j in range(numAviones):
            idNum+=1
            querry = createAvion(idNum, choice(manufactList),i+1, choice(modelList))
            querryList.append(querry)
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
    querryList = []
    while(avionesList != []):

        for i in range(30): 
            
            posib = choice(range(10))

            if posib < 5 and avionesList != []:

                avion = choice(avionesList)
                avionesList.remove(avion)

                querry = (avion[0], i+1)
                querryList.append(querry)
    return querryList

def getTaller(avionesList):

    querryList = []

    while(avionesList != []):


            for i in range(30): 
                
                posib = choice(range(10))

                if posib < 5 and avionesList != []:
                    
                    avion = choice(avionesList)
                    avionesList.remove(avion)

                    querry = createFactura(avion[0],i+1,avion[2])
                    querryList.append(querry)
    return querryList

def createControladorVuelo(avionesList, vuelosList):
    
    file = open("ControladorVuelo.txt", "w+")

    file.write("INSERT INTO ControladorVuelo VALUES\n")


    for i in range(80):
        
        idContr = 500 + choice(range(300))+1

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


listaAviones = [(1, 1, 'EE2711', 'EM445-7ZKPG', 'Embraer-Empresa Brasileira DR AeronÁutica', 711, 2, 'Premium', 'ACT') ,
(2, 1, 'BB31728', 'BY977-2LNVY', 'Bye Aerospace', 1728, 3, 'Econ/Premium', 'REP') ,
(3, 1, 'EE31601', 'EM140-1IWYA', 'Embraer-Empresa Brasileira DR AeronÁutica', 1601, 3, 'Premium', 'ACT') ,
(4, 1, 'BB11270', 'BU132-9CXSN', 'Burnelli', 1270, 1, 'Private', 'INACT') ,
(5, 1, 'BB11854', 'BU633-8FMIQ', 'Bushby', 1854, 1, 'Econ', 'REP') ,
(6, 1, 'BB1957', 'BO034-3IVQO', 'Boeing Business Jets', 957, 1, 'Econ', 'INACT') ,
(7, 1, 'BB22043', 'BU411-3XVVO', 'Buhl', 2043, 2, 'Econ/Premium', 'INACT') ,
(8, 1, 'BB32102', 'BU760-8ZSGL', 'Buhl', 2102, 3, 'Private', 'REP') ,
(9, 1, 'BB21631', 'BÜ399-2GHSD', 'Büttner Propeller', 1631, 2, 'Private', 'ACT') ,
(10, 1, 'BB32412', 'BU760-8ZSGL', 'Buethe', 2412, 3, 'Econ/Premium', 'REP') ,
(11, 1, 'BB22498', 'BY651-2LXYQ', 'Bye Aerospace', 2498, 2, 'Econ', 'INACT') ,
(12, 1, 'PP11155', 'PI832-2DMTK', 'Pilatus Business Aircraft', 1155, 1, 'Premium', 'INACT') ,
(13, 1, 'EE22040', 'EM798-8QYRO', 'Embraer-Empresa Brasileira DR AeronÁutica', 2040, 2, 'Private', 'ACT') ,
(14, 1, 'BB21481', 'BY944-3BDSL', 'Bye Aerospace', 1481, 2, 'Premium', 'REP') ,
(15, 1, 'AA31698', 'AI832-2DMTK', 'Airbus Corporate Jets', 1698, 3, 'Econ', 'INACT') ,
(16, 1, 'AA21212', 'AI189-6HXVJ', 'Airbus Corporate Jets', 1212, 2, 'Econ', 'INACT') ,
(17, 1, 'TT22280', 'TE551-0RCSM', 'Textron Aviation', 2280, 2, 'Econ/Premium', 'REP') ,
(18, 1, 'BB1818', 'BU963-6FRIN', 'Buhl', 818, 1, 'Econ', 'ACT') ,
(19, 1, 'BB2939', 'BÜ673-0UBWG', 'Büttner Propeller', 939, 2, 'Econ/Premium', 'ACT') ,
(20, 1, 'BB21142', 'BU992-5DYJF', 'Burgess', 1142, 2, 'Econ/Premium', 'REP') ,
(21, 2, 'TT31736', 'TE673-0UBWG', 'Textron Aviation', 1736, 3, 'Private', 'ACT') ,
(22, 2, 'BB31597', 'BU166-6EDCR', "Burl's Aircraft", 1597, 3, 'Private', 'ACT') ,
(23, 2, 'BB21816', 'BU944-3BDSL', 'Buethe', 1816, 2, 'Private', 'REP') ,
(24, 2, 'BB21544', 'BÜ004-9VHRK', 'Büttner Propeller', 1544, 2, 'Premium', 'REP') ,
(25, 2, 'BB3706', 'BO220-9JCDF', 'Bombardier Aerospace', 706, 3, 'Econ', 'ACT') ,
(26, 2, 'BB31767', 'BU677-2FYOI', 'Buethe', 1767, 3, 'Private', 'ACT') ,
(27, 2, 'EE22473', 'EM464-3ANYM', 'Embraer-Empresa Brasileira DR AeronÁutica', 2473, 2, 'Premium', 'REP') ,
(28, 2, 'BB1939', 'BÜ004-9VHRK', 'Büttner Propeller', 939, 1, 'Econ/Premium', 'ACT') ,
(29, 2, 'BB31034', 'BO869-3LKQA', 'Bombardier Aerospace', 1034, 3, 'Econ/Premium', 'ACT') ,
(30, 2, 'BB31405', 'BO148-4XRPQ', 'Boeing Business Jets', 1405, 3, 'Premium', 'REP') ,
(31, 2, 'BB32079', 'BU004-9VHRK', 'Bushby', 2079, 3, 'Econ/Premium', 'ACT') ,
(32, 2, 'BB2764', 'BU891-9LGJU', 'Burnelli', 764, 2, 'Econ/Premium', 'ACT') ,
(33, 2, 'EE21434', 'EM941-5LQKT', 'Embraer-Empresa Brasileira DR AeronÁutica', 1434, 2, 'Econ/Premium', 'ACT') ,
(34, 2, 'BB2726', 'BU634-3QCUZ', "Burl's Aircraft", 726, 2, 'Private', 'ACT') ,
(35, 2, 'AA1565', 'AI856-3JEYV', 'Airbus Corporate Jets', 565, 1, 'Econ/Premium', 'INACT') ,
(36, 2, 'BB32229', 'BO399-2GHSD', 'Bombardier Aerospace', 2229, 3, 'Private', 'ACT') ,
(37, 2, 'BB12397', 'BO873-0UVAD', 'Bombardier Aerospace', 2397, 1, 'Econ', 'INACT') ,
(38, 2, 'TT3540', 'TE673-0UBWG', 'Textron Aviation', 540, 3, 'Private', 'REP') ,
(39, 2, 'BB1698', 'BU971-1MNGO', 'Buhl', 698, 1, 'Private', 'REP') ,
(40, 2, 'AA31416', 'AI810-0XOKL', 'Airbus Corporate Jets', 1416, 3, 'Econ/Premium', 'REP') ,
(41, 3, 'EE21947', 'EM038-9VMAI', 'Embraer-Empresa Brasileira DR AeronÁutica', 1947, 2, 'Private', 'INACT') ,
(42, 3, 'PP3805', 'PI538-8MVJV', 'Pilatus Business Aircraft', 805, 3, 'Econ/Premium', 'INACT') ,
(43, 3, 'PP32284', 'PI760-8ZSGL', 'Pilatus Business Aircraft', 2284, 3, 'Econ/Premium', 'REP') ,
(44, 3, 'BB21732', 'BU941-5LQKT', 'Burnelli', 1732, 2, 'Econ/Premium', 'REP') ,
(45, 3, 'BB32469', 'BU944-3BDSL', 'Bushby', 2469, 3, 'Premium', 'INACT') ,
(46, 3, 'BB12037', 'BU313-7TJGA', 'Burgess', 2037, 1, 'Econ/Premium', 'ACT') ,
(47, 3, 'BB12452', 'BU432-4SAWP', 'Burnelli', 2452, 1, 'Private', 'REP') ,
(48, 3, 'BB31229', 'BU202-9SCLT', "Burl's Aircraft", 1229, 3, 'Premium', 'INACT') ,
(49, 3, 'DD3772', 'DA189-6HXVJ', 'Dassault Falcon', 772, 3, 'Private', 'REP') ,
(50, 3, 'EE31524', 'EM699-6TLUQ', 'Embraer-Empresa Brasileira DR AeronÁutica', 1524, 3, 'Econ/Premium', 'INACT') ,
(51, 3, 'BB3813', 'BU728-2AFDZ', 'Bushby', 813, 3, 'Premium', 'REP') ,
(52, 3, 'BB31534', 'BU709-3MKBC', 'Burgess', 1534, 3, 'Private', 'ACT') ,
(53, 3, 'BB1727', 'BU699-6TLUQ', 'Burnelli', 727, 1, 'Premium', 'ACT') ,
(54, 3, 'BB11924', 'BU387-5REYZ', 'Buethe', 1924, 1, 'Premium', 'ACT') ,
(55, 3, 'BB2847', 'BO200-8KKUZ', 'Boeing Business Jets', 847, 2, 'Econ', 'INACT') ,
(56, 3, 'BB31305', 'BU034-3IVQO', 'Buethe', 1305, 3, 'Private', 'REP') ,
(57, 3, 'BB31190', 'BU443-5LZYA', 'Buethe', 1190, 3, 'Econ', 'REP') ,
(58, 3, 'EE22222', 'EM202-9SCLT', 'Embraer-Empresa Brasileira DR AeronÁutica', 2222, 2, 'Premium', 'INACT') ,
(59, 3, 'PP21787', 'PI432-4SAWP', 'Pilatus Business Aircraft', 1787, 2, 'Econ/Premium', 'ACT') ,
(60, 3, 'PP2880', 'PI996-7RTPT', 'Pilatus Business Aircraft', 880, 2, 'Premium', 'ACT') ,
(61, 4, 'TT21649', 'TE856-3JEYV', 'Textron Aviation', 1649, 2, 'Premium', 'INACT') ,
(62, 4, 'BB11695', 'BU551-0RCSM', 'Buethe', 1695, 1, 'Econ/Premium', 'INACT') ,
(63, 4, 'BB1506', 'BU633-8FMIQ', "Burl's Aircraft", 506, 1, 'Private', 'ACT') ,
(64, 4, 'BB21400', 'BU200-8KKUZ', 'Buethe', 1400, 2, 'Econ/Premium', 'ACT') ,
(65, 4, 'BB12269', 'BY716-5MQKS', 'Bye Aerospace', 2269, 1, 'Private', 'INACT') ,
(66, 4, 'BB11163', 'BO634-3QCUZ', 'Boeing Business Jets', 1163, 1, 'Econ', 'INACT') ,
(67, 4, 'BB12463', 'BY520-5QWGV', 'Bye Aerospace', 2463, 1, 'Econ/Premium', 'INACT') ,
(68, 4, 'EE22322', 'EM792-1CUDL', 'Embraer-Empresa Brasileira DR AeronÁutica', 2322, 2, 'Premium', 'ACT') ,
(69, 4, 'AA21659', 'AI732-2YRMW', 'Airbus Corporate Jets', 1659, 2, 'Premium', 'INACT') ,
(70, 4, 'BB31928', 'BU839-9DOST', 'Buhl', 1928, 3, 'Private', 'INACT') ,
(71, 4, 'BB2902', 'BU166-6EDCR', 'Burnelli', 902, 2, 'Econ/Premium', 'REP') ,
(72, 4, 'DD1849', 'DA709-3MKBC', 'Dassault Falcon', 849, 1, 'Premium', 'ACT') ,
(73, 4, 'BB1811', 'BU399-2GHSD', "Burl's Aircraft", 811, 1, 'Premium', 'REP') ,
(74, 4, 'BB21174', 'BU750-9QONA', "Burl's Aircraft", 1174, 2, 'Premium', 'REP') ,
(75, 4, 'BB31379', 'BU189-6HXVJ', 'Buhl', 1379, 3, 'Premium', 'ACT') ,
(76, 4, 'BB2991', 'BU985-9OCBD', 'Buhl', 991, 2, 'Econ/Premium', 'INACT') ,
(77, 4, 'GG21918', 'GU732-2YRMW', 'Gulfstream Aerospace', 1918, 2, 'Premium', 'ACT') ,
(78, 4, 'BB32067', 'BU672-9JZZP', 'Burnelli', 2067, 3, 'Econ/Premium', 'INACT') ,
(79, 4, 'BB32032', 'BU200-8KKUZ', "Burl's Aircraft", 2032, 3, 'Econ/Premium', 'INACT') ,
(80, 4, 'BB12078', 'BU716-5MQKS', 'Buhl', 2078, 1, 'Econ/Premium', 'ACT') ,
(81, 5, 'BB11016', 'BU916-7WHGQ', 'Burgess', 1016, 1, 'Econ/Premium', 'INACT') ,
(82, 5, 'BB1971', 'BU387-5REYZ', "Burl's Aircraft", 971, 1, 'Private', 'INACT') ,
(83, 5, 'AA3687', 'AI916-7WHGQ', 'Airbus Corporate Jets', 687, 3, 'Private', 'REP') ,
(84, 5, 'BB31037', 'BU677-2FYOI', 'Buethe', 1037, 3, 'Econ/Premium', 'REP') ,
(85, 5, 'BB21868', 'BO992-5DYJF', 'Boeing Business Jets', 1868, 2, 'Private', 'REP') ,
(86, 5, 'EE31145', 'EM551-0RCSM', 'Embraer-Empresa Brasileira DR AeronÁutica', 1145, 3, 'Econ/Premium', 'ACT') ,
(87, 5, 'BB12211', 'BÜ714-2HAXR', 'Büttner Propeller', 2211, 1, 'Premium', 'REP') ,
(88, 5, 'BB31803', 'BY839-9DOST', 'Bye Aerospace', 1803, 3, 'Premium', 'INACT') ,
(89, 5, 'BB11655', 'BU432-4SAWP', 'Buethe', 1655, 1, 'Private', 'ACT') ,
(90, 5, 'BB22096', 'BU873-0UVAD', 'Burnelli', 2096, 2, 'Econ', 'ACT') ,
(91, 5, 'BB11160', 'BY856-3JEYV', 'Bye Aerospace', 1160, 1, 'Private', 'REP') ,
(92, 5, 'BB32497', 'BO800-9GCBL', 'Bombardier Aerospace', 2497, 3, 'Private', 'ACT') ,
(93, 5, 'TT32201', 'TE202-9SCLT', 'Textron Aviation', 2201, 3, 'Econ/Premium', 'REP') ,
(94, 5, 'PP31394', 'PI985-9OCBD', 'Pilatus Business Aircraft', 1394, 3, 'Econ/Premium', 'REP') ,
(95, 5, 'BB2896', 'BU992-5DYJF', 'Bushby', 896, 2, 'Private', 'ACT') ,
(96, 5, 'BB31198', 'BU633-8FMIQ', 'Buethe', 1198, 3, 'Premium', 'ACT') ,
(97, 5, 'AA3978', 'AI950-0RLLI', 'Airbus Corporate Jets', 978, 3, 'Private', 'REP') ,
(98, 5, 'BB31801', 'BO423-7VVTJ', 'Boeing Business Jets', 1801, 3, 'Econ/Premium', 'ACT') ,
(99, 5, 'BB1943', 'BU798-8QYRO', 'Burgess', 943, 1, 'Premium', 'ACT') ,
(100, 5, 'GG11574', 'GU714-2HAXR', 'Gulfstream Aerospace', 1574, 1, 'Premium', 'ACT') ,
(101, 6, 'DD21625', 'DA782-5KCAJ', 'Dassault Falcon', 1625, 2, 'Private', 'ACT') ,
(102, 6, 'BB22024', 'BU140-1IWYA', 'Burnelli', 2024, 2, 'Premium', 'REP') ,
(103, 6, 'GG21407', 'GU038-9VMAI', 'Gulfstream Aerospace', 1407, 2, 'Private', 'REP') ,
(104, 6, 'BB21761', 'BU166-6EDCR', 'Buethe', 1761, 2, 'Econ', 'REP') ,
(105, 6, 'GG21302', 'GU445-7ZKPG', 'Gulfstream Aerospace', 1302, 2, 'Premium', 'INACT') ,
(106, 6, 'BB12225', 'BU034-3IVQO', 'Bushby', 2225, 1, 'Premium', 'ACT') ,
(107, 6, 'BB21274', 'BÜ977-2LNVY', 'Büttner Propeller', 1274, 2, 'Private', 'REP') ,
(108, 6, 'BB11181', 'BU750-9QONA', 'Burgess', 1181, 1, 'Econ/Premium', 'ACT') ,
(109, 6, 'BB2687', 'BU034-3IVQO', 'Buhl', 687, 2, 'Premium', 'INACT') ,
(110, 6, 'EE22377', 'EM200-1LMUI', 'Embraer-Empresa Brasileira DR AeronÁutica', 2377, 2, 'Private', 'ACT') ,
(111, 6, 'BB31692', 'BU387-5REYZ', "Burl's Aircraft", 1692, 3, 'Premium', 'REP') ,
(112, 6, 'DD1888', 'DA839-9DOST', 'Dassault Falcon', 888, 1, 'Econ/Premium', 'INACT') ,
(113, 6, 'EE32039', 'EM916-7WHGQ', 'Embraer-Empresa Brasileira DR AeronÁutica', 2039, 3, 'Econ/Premium', 'INACT') ,
(114, 6, 'PP11887', 'PI538-8MVJV', 'Pilatus Business Aircraft', 1887, 1, 'Premium', 'INACT') ,
(115, 6, 'EE11355', 'EM634-3QCUZ', 'Embraer-Empresa Brasileira DR AeronÁutica', 1355, 1, 'Econ', 'ACT') ,
(116, 6, 'EE21769', 'EM677-2FYOI', 'Embraer-Empresa Brasileira DR AeronÁutica', 1769, 2, 'Premium', 'REP') ,
(117, 6, 'BB11717', 'BU538-8MVJV', 'Buethe', 1717, 1, 'Premium', 'REP') ,
(118, 6, 'BB22051', 'BÜ716-5MQKS', 'Büttner Propeller', 2051, 2, 'Private', 'REP') ,
(119, 6, 'BB31869', 'BO220-9JCDF', 'Bombardier Aerospace', 1869, 3, 'Private', 'INACT') ,
(120, 6, 'BB12236', 'BÜ944-3BDSL', 'Büttner Propeller', 2236, 1, 'Econ', 'ACT') ,
(121, 7, 'BB3874', 'BU477-6HHYX', 'Buhl', 874, 3, 'Private', 'ACT') ,
(122, 7, 'TT22382', 'TE443-5LZYA', 'Textron Aviation', 2382, 2, 'Econ', 'REP') ,
(123, 7, 'BB21202', 'BU916-7WHGQ', 'Buethe', 1202, 2, 'Premium', 'INACT') ,
(124, 7, 'EE22491', 'EM677-2FYOI', 'Embraer-Empresa Brasileira DR AeronÁutica', 2491, 2, 'Premium', 'ACT') ,
(125, 7, 'EE11755', 'EM200-8KKUZ', 'Embraer-Empresa Brasileira DR AeronÁutica', 1755, 1, 'Econ', 'INACT') ,
(126, 7, 'BB31658', 'BÜ252-0JCJN', 'Büttner Propeller', 1658, 3, 'Private', 'INACT') ,
(127, 7, 'AA12000', 'AI273-2DJVB', 'Airbus Corporate Jets', 2000, 1, 'Econ/Premium', 'REP') ,
(128, 7, 'BB32038', 'BU728-2AFDZ', 'Buhl', 2038, 3, 'Econ', 'INACT') ,
(129, 7, 'BB22246', 'BÜ832-2DMTK', 'Büttner Propeller', 2246, 2, 'Premium', 'ACT') ,
(130, 7, 'DD11103', 'DA399-2GHSD', 'Dassault Falcon', 1103, 1, 'Econ/Premium', 'ACT') ,
(131, 7, 'BB11448', 'BU038-9VMAI', 'Buhl', 1448, 1, 'Econ/Premium', 'ACT') ,
(132, 7, 'EE12158', 'EM944-3BDSL', 'Embraer-Empresa Brasileira DR AeronÁutica', 2158, 1, 'Premium', 'INACT') ,
(133, 7, 'AA11981', 'AI634-3QCUZ', 'Airbus Corporate Jets', 1981, 1, 'Econ/Premium', 'REP') ,
(134, 7, 'PP2888', 'PI672-9JZZP', 'Pilatus Business Aircraft', 888, 2, 'Econ/Premium', 'INACT') ,
(135, 7, 'BB21863', 'BY667-7AWLH', 'Bye Aerospace', 1863, 2, 'Private', 'ACT') ,
(136, 7, 'PP11810', 'PI709-3MKBC', 'Pilatus Business Aircraft', 1810, 1, 'Econ/Premium', 'INACT') ,
(137, 7, 'BB21264', 'BÜ866-5SNGB', 'Büttner Propeller', 1264, 2, 'Private', 'ACT') ,
(138, 7, 'BB31415', 'BY760-8ZSGL', 'Bye Aerospace', 1415, 3, 'Private', 'REP') ,
(139, 7, 'DD22142', 'DA944-3BDSL', 'Dassault Falcon', 2142, 2, 'Private', 'REP') ,
(140, 7, 'BB11138', 'BÜ773-9RRSK', 'Büttner Propeller', 1138, 1, 'Private', 'ACT') ,
(141, 8, 'AA11480', 'AI273-2DJVB', 'Airbus Corporate Jets', 1480, 1, 'Premium', 'REP') ,
(142, 8, 'BB1717', 'BU520-5QWGV', 'Burnelli', 717, 1, 'Premium', 'INACT') ,
(143, 8, 'BB2525', 'BO798-8QYRO', 'Boeing Business Jets', 525, 2, 'Premium', 'ACT') ,
(144, 8, 'BB2912', 'BY714-2HAXR', 'Bye Aerospace', 912, 2, 'Econ', 'REP') ,
(145, 8, 'AA12210', 'AI411-3XVVO', 'Airbus Corporate Jets', 2210, 1, 'Private', 'REP') ,
(146, 8, 'BB32403', 'BU873-0UVAD', 'Buhl', 2403, 3, 'Econ/Premium', 'ACT') ,
(147, 8, 'BB12361', 'BU971-1MNGO', 'Bushby', 2361, 1, 'Econ', 'INACT') ,
(148, 8, 'BB2617', 'BU148-4XRPQ', "Burl's Aircraft", 617, 2, 'Private', 'ACT') ,
(149, 8, 'BB11126', 'BU203-3JCWQ', 'Buhl', 1126, 1, 'Private', 'REP') ,
(150, 8, 'BB21383', 'BU866-5SNGB', 'Buethe', 1383, 2, 'Econ', 'INACT') ,
(151, 8, 'DD3933', 'DA950-0RLLI', 'Dassault Falcon', 933, 3, 'Premium', 'ACT') ,
(152, 8, 'BB3801', 'BÜ839-9DOST', 'Büttner Propeller', 801, 3, 'Econ', 'REP') ,
(153, 8, 'EE12400', 'EM432-4SAWP', 'Embraer-Empresa Brasileira DR AeronÁutica', 2400, 1, 'Premium', 'INACT') ,
(154, 8, 'GG21233', 'GU873-8YOQU', 'Gulfstream Aerospace', 1233, 2, 'Premium', 'INACT') ,
(155, 8, 'BB3734', 'BU520-5QWGV', 'Burnelli', 734, 3, 'Private', 'INACT') ,
(156, 8, 'PP11382', 'PI189-6HXVJ', 'Pilatus Business Aircraft', 1382, 1, 'Premium', 'REP') ,
(157, 8, 'BB12319', 'BU714-2HAXR', 'Buhl', 2319, 1, 'Econ/Premium', 'REP') ,
(158, 8, 'PP22221', 'PI996-7RTPT', 'Pilatus Business Aircraft', 2221, 2, 'Private', 'INACT') ,
(159, 8, 'BB22211', 'BU810-0XOKL', 'Burnelli', 2211, 2, 'Econ/Premium', 'REP') ,
(160, 8, 'BB21665', 'BO208-4FPOG', 'Bombardier Aerospace', 1665, 2, 'Econ', 'REP') ,
(161, 9, 'BB21237', 'BU996-7RTPT', 'Burnelli', 1237, 2, 'Econ', 'ACT') ,
(162, 9, 'BB11899', 'BU189-6HXVJ', 'Buethe', 1899, 1, 'Premium', 'ACT') ,
(163, 9, 'BB31119', 'BU202-9SCLT', 'Bushby', 1119, 3, 'Premium', 'INACT') ,
(164, 9, 'BB32191', 'BÜ132-9CXSN', 'Büttner Propeller', 2191, 3, 'Econ', 'ACT') ,
(165, 9, 'BB21577', 'BO132-9CXSN', 'Bombardier Aerospace', 1577, 2, 'Econ', 'REP') ,
(166, 9, 'BB31366', 'BU773-9RRSK', 'Burnelli', 1366, 3, 'Econ/Premium', 'REP') ,
(167, 9, 'BB21674', 'BÜ732-2YRMW', 'Büttner Propeller', 1674, 2, 'Econ/Premium', 'ACT') ,
(168, 9, 'BB1680', 'BÜ399-2GHSD', 'Büttner Propeller', 680, 1, 'Econ', 'ACT') ,
(169, 9, 'BB32091', 'BO750-9QONA', 'Boeing Business Jets', 2091, 3, 'Econ/Premium', 'ACT') ,
(170, 9, 'BB22104', 'BU038-9VMAI', 'Buethe', 2104, 2, 'Premium', 'REP') ,
(171, 9, 'TT31164', 'TE728-2AFDZ', 'Textron Aviation', 1164, 3, 'Econ', 'INACT') ,
(172, 9, 'PP2514', 'PI800-9GCBL', 'Pilatus Business Aircraft', 514, 2, 'Private', 'REP') ,
(173, 9, 'AA2778', 'AI986-6KDJJ', 'Airbus Corporate Jets', 778, 2, 'Econ/Premium', 'REP') ,
(174, 9, 'BB3502', 'BU891-9LGJU', 'Burgess', 502, 3, 'Premium', 'ACT') ,
(175, 9, 'BB12210', 'BU902-0MMNV', 'Buhl', 2210, 1, 'Private', 'ACT') ,
(176, 9, 'BB21980', 'BU532-8VNYA', 'Buethe', 1980, 2, 'Econ/Premium', 'INACT') ,
(177, 9, 'AA21521', 'AI764-3DVVD', 'Airbus Corporate Jets', 1521, 2, 'Econ', 'ACT') ,
(178, 9, 'DD21410', 'DA732-2YRMW', 'Dassault Falcon', 1410, 2, 'Econ/Premium', 'ACT') ,
(179, 9, 'BB2550', 'BU986-6KDJJ', 'Burgess', 550, 2, 'Econ', 'REP') ,
(180, 9, 'GG11068', 'GU866-5SNGB', 'Gulfstream Aerospace', 1068, 1, 'Econ/Premium', 'INACT') ,
(181, 10, 'BB11312', 'BU728-2AFDZ', 'Burnelli', 1312, 1, 'Private', 'ACT') ,
(182, 10, 'TT11686', 'TE716-5MQKS', 'Textron Aviation', 1686, 1, 'Premium', 'ACT') ,
(183, 10, 'BB31638', 'BU866-5SNGB', 'Buhl', 1638, 3, 'Private', 'ACT') ,
(184, 10, 'BB2688', 'BU673-0UBWG', "Burl's Aircraft", 688, 2, 'Econ/Premium', 'REP') ,
(185, 10, 'BB32007', 'BU464-3ANYM', 'Burgess', 2007, 3, 'Private', 'INACT') ,
(186, 10, 'BB22335', 'BU252-0JCJN', 'Burnelli', 2335, 2, 'Premium', 'ACT') ,
(187, 10, 'BB12411', 'BY538-8MVJV', 'Bye Aerospace', 2411, 1, 'Econ', 'REP') ,
(188, 10, 'BB32000', 'BU977-2LNVY', "Burl's Aircraft", 2000, 3, 'Private', 'ACT') ,
(189, 10, 'BB12277', 'BU992-5DYJF', "Burl's Aircraft", 2277, 1, 'Econ', 'REP') ,
(190, 10, 'BB1587', 'BO313-7TJGA', 'Boeing Business Jets', 587, 1, 'Private', 'REP') ,
(191, 10, 'DD21568', 'DA773-9RRSK', 'Dassault Falcon', 1568, 2, 'Premium', 'INACT') ,
(192, 10, 'EE3752', 'EM464-3ANYM', 'Embraer-Empresa Brasileira DR AeronÁutica', 752, 3, 'Private', 'REP') ,
(193, 10, 'BB21030', 'BU985-9OCBD', 'Burgess', 1030, 2, 'Private', 'REP') ,
(194, 10, 'DD21649', 'DA677-2FYOI', 'Dassault Falcon', 1649, 2, 'Premium', 'REP') ,
(195, 10, 'BB21676', 'BU166-6EDCR', 'Burnelli', 1676, 2, 'Econ', 'ACT') ,
(196, 10, 'BB22446', 'BU447-1JCVI', 'Burnelli', 2446, 2, 'Econ', 'ACT') ,
(197, 10, 'BB31588', 'BU313-7TJGA', "Burl's Aircraft", 1588, 3, 'Premium', 'INACT') ,
(198, 10, 'EE11372', 'EM252-0JCJN', 'Embraer-Empresa Brasileira DR AeronÁutica', 1372, 1, 'Econ/Premium', 'REP') ,
(199, 10, 'EE11105', 'EM538-8MVJV', 'Embraer-Empresa Brasileira DR AeronÁutica', 1105, 1, 'Premium', 'INACT') ,
(200, 10, 'PP22231', 'PI699-6TLUQ', 'Pilatus Business Aircraft', 2231, 2, 'Econ', 'ACT') ,
(201, 11, 'BB31010', 'BÜ971-1MNGO', 'Büttner Propeller', 1010, 3, 'Econ', 'REP') ,
(202, 11, 'BB11278', 'BU963-6FRIN', 'Bushby', 1278, 1, 'Premium', 'REP') ,
(203, 11, 'BB1771', 'BO782-5KCAJ', 'Bombardier Aerospace', 771, 1, 'Econ/Premium', 'INACT') ,
(204, 11, 'BB11412', 'BU963-6FRIN', "Burl's Aircraft", 1412, 1, 'Econ/Premium', 'REP') ,
(205, 11, 'GG12191', 'GU873-0UVAD', 'Gulfstream Aerospace', 2191, 1, 'Econ/Premium', 'INACT') ,
(206, 11, 'BB3505', 'BU203-3JCWQ', 'Burnelli', 505, 3, 'Econ', 'ACT') ,
(207, 11, 'BB2504', 'BU916-7WHGQ', 'Buhl', 504, 2, 'Private', 'INACT') ,
(208, 11, 'BB31405', 'BU203-3JCWQ', 'Burnelli', 1405, 3, 'Private', 'INACT') ,
(209, 11, 'EE31750', 'EM387-5REYZ', 'Embraer-Empresa Brasileira DR AeronÁutica', 1750, 3, 'Premium', 'ACT') ,
(210, 11, 'DD11246', 'DA672-9JZZP', 'Dassault Falcon', 1246, 1, 'Econ', 'ACT') ,
(211, 11, 'BB12038', 'BU663-5XCSJ', "Burl's Aircraft", 2038, 1, 'Econ', 'INACT') ,
(212, 11, 'AA2538', 'AI040-8WBTB', 'Airbus Corporate Jets', 538, 2, 'Private', 'REP') ,
(213, 11, 'GG2754', 'GU873-8YOQU', 'Gulfstream Aerospace', 754, 2, 'Premium', 'INACT') ,
(214, 11, 'BB31929', 'BU634-3QCUZ', 'Burgess', 1929, 3, 'Private', 'INACT') ,
(215, 11, 'GG11930', 'GU810-0XOKL', 'Gulfstream Aerospace', 1930, 1, 'Econ', 'REP') ,
(216, 11, 'BB21356', 'BÜ034-3IVQO', 'Büttner Propeller', 1356, 2, 'Private', 'ACT') ,
(217, 11, 'BB3883', 'BU250-3IZRJ', "Burl's Aircraft", 883, 3, 'Econ', 'ACT') ,
(218, 11, 'TT11088', 'TE651-2LXYQ', 'Textron Aviation', 1088, 1, 'Premium', 'REP') ,
(219, 11, 'BB11600', 'BU208-4FPOG', 'Burgess', 1600, 1, 'Econ/Premium', 'REP') ,
(220, 11, 'DD32474', 'DA985-9OCBD', 'Dassault Falcon', 2474, 3, 'Econ/Premium', 'REP') ,
(221, 12, 'DD21406', 'DA667-7AWLH', 'Dassault Falcon', 1406, 2, 'Econ/Premium', 'ACT') ,
(222, 12, 'BB1622', 'BY714-2HAXR', 'Bye Aerospace', 622, 1, 'Premium', 'INACT') ,
(223, 12, 'BB11888', 'BO375-9HBMB', 'Boeing Business Jets', 1888, 1, 'Premium', 'ACT') ,
(224, 12, 'BB21757', 'BÜ992-5DYJF', 'Büttner Propeller', 1757, 2, 'Econ/Premium', 'REP') ,
(225, 12, 'BB31771', 'BU941-5LQKT', 'Burgess', 1771, 3, 'Private', 'INACT') ,
(226, 12, 'BB32422', 'BY208-4FPOG', 'Bye Aerospace', 2422, 3, 'Premium', 'INACT') ,
(227, 12, 'BB32083', 'BU977-2LNVY', 'Buhl', 2083, 3, 'Premium', 'ACT') ,
(228, 12, 'BB21619', 'BÜ667-7AWLH', 'Büttner Propeller', 1619, 2, 'Private', 'INACT') ,
(229, 12, 'BB11801', 'BU869-3LKQA', 'Buethe', 1801, 1, 'Econ', 'ACT') ,
(230, 12, 'BB3896', 'BY732-2YRMW', 'Bye Aerospace', 896, 3, 'Econ/Premium', 'ACT') ,
(231, 12, 'BB1753', 'BU040-8WBTB', 'Burnelli', 753, 1, 'Private', 'REP') ,
(232, 12, 'BB11673', 'BÜ200-1LMUI', 'Büttner Propeller', 1673, 1, 'Econ', 'INACT') ,
(233, 12, 'GG21984', 'GU699-6TLUQ', 'Gulfstream Aerospace', 1984, 2, 'Private', 'INACT') ,
(234, 12, 'BB21194', 'BU760-8ZSGL', 'Buethe', 1194, 2, 'Private', 'INACT') ,
(235, 12, 'BB12375', 'BO716-5MQKS', 'Boeing Business Jets', 2375, 1, 'Premium', 'INACT') ,
(236, 12, 'BB2881', 'BÜ387-5REYZ', 'Büttner Propeller', 881, 2, 'Econ/Premium', 'INACT') ,
(237, 12, 'PP1850', 'PI977-2LNVY', 'Pilatus Business Aircraft', 850, 1, 'Private', 'INACT') ,
(238, 12, 'BB32051', 'BO773-9RRSK', 'Bombardier Aerospace', 2051, 3, 'Private', 'INACT') ,
(239, 12, 'BB2936', 'BU902-0MMNV', "Burl's Aircraft", 936, 2, 'Econ', 'INACT') ,
(240, 12, 'BB21331', 'BU677-2FYOI', 'Burgess', 1331, 2, 'Premium', 'REP') ,
(241, 13, 'BB22250', 'BU750-9QONA', 'Buethe', 2250, 2, 'Econ', 'REP') ,
(242, 13, 'BB32178', 'BU208-4FPOG', 'Buhl', 2178, 3, 'Private', 'ACT') ,
(243, 13, 'BB12455', 'BU651-2LXYQ', "Burl's Aircraft", 2455, 1, 'Econ/Premium', 'INACT') ,
(244, 13, 'BB22149', 'BU750-9QONA', 'Bushby', 2149, 2, 'Private', 'ACT') ,
(245, 13, 'BB31880', 'BO200-8KKUZ', 'Bombardier Aerospace', 1880, 3, 'Premium', 'ACT') ,
(246, 13, 'BB12181', 'BU996-7RTPT', 'Burnelli', 2181, 1, 'Econ/Premium', 'INACT') ,
(247, 13, 'BB11097', 'BU532-8VNYA', 'Burnelli', 1097, 1, 'Econ/Premium', 'ACT') ,
(248, 13, 'DD32232', 'DA477-6HHYX', 'Dassault Falcon', 2232, 3, 'Private', 'ACT') ,
(249, 13, 'BB3975', 'BU671-0BCGZ', 'Bushby', 975, 3, 'Private', 'INACT') ,
(250, 13, 'PP31737', 'PI538-8MVJV', 'Pilatus Business Aircraft', 1737, 3, 'Premium', 'INACT') ,
(251, 13, 'BB11346', 'BU132-9CXSN', "Burl's Aircraft", 1346, 1, 'Premium', 'REP') ,
(252, 13, 'GG31713', 'GU443-5LZYA', 'Gulfstream Aerospace', 1713, 3, 'Premium', 'REP') ,
(253, 13, 'BB32303', 'BY634-3QCUZ', 'Bye Aerospace', 2303, 3, 'Econ', 'ACT') ,
(254, 13, 'BB32452', 'BÜ445-7ZKPG', 'Büttner Propeller', 2452, 3, 'Premium', 'INACT') ,
(255, 13, 'AA21762', 'AI148-4XRPQ', 'Airbus Corporate Jets', 1762, 2, 'Private', 'REP') ,
(256, 13, 'PP32408', 'PI977-2LNVY', 'Pilatus Business Aircraft', 2408, 3, 'Private', 'REP') ,
(257, 13, 'GG1842', 'GU202-9SCLT', 'Gulfstream Aerospace', 842, 1, 'Econ/Premium', 'INACT') ,
(258, 13, 'TT22237', 'TE944-3BDSL', 'Textron Aviation', 2237, 2, 'Econ/Premium', 'REP') ,
(259, 13, 'PP32352', 'PI782-5KCAJ', 'Pilatus Business Aircraft', 2352, 3, 'Econ/Premium', 'INACT') ,
(260, 13, 'TT1835', 'TE714-2HAXR', 'Textron Aviation', 835, 1, 'Premium', 'REP') ,
(261, 14, 'BB32248', 'BÜ750-9QONA', 'Büttner Propeller', 2248, 3, 'Premium', 'REP') ,
(262, 14, 'BB31470', 'BO839-9DOST', 'Boeing Business Jets', 1470, 3, 'Premium', 'REP') ,
(263, 14, 'BB21892', 'BU208-4FPOG', 'Buhl', 1892, 2, 'Econ/Premium', 'INACT') ,
(264, 14, 'BB11902', 'BY551-0RCSM', 'Bye Aerospace', 1902, 1, 'Econ/Premium', 'REP') ,
(265, 14, 'BB21932', 'BU971-1MNGO', "Burl's Aircraft", 1932, 2, 'Premium', 'REP') ,
(266, 14, 'BB2773', 'BÜ996-7RTPT', 'Büttner Propeller', 773, 2, 'Econ/Premium', 'REP') ,
(267, 14, 'BB32132', 'BU220-9JCDF', 'Buhl', 2132, 3, 'Econ', 'REP') ,
(268, 14, 'EE21953', 'EM252-0JCJN', 'Embraer-Empresa Brasileira DR AeronÁutica', 1953, 2, 'Private', 'ACT') ,
(269, 14, 'BB11546', 'BO038-9VMAI', 'Boeing Business Jets', 1546, 1, 'Econ', 'REP') ,
(270, 14, 'BB31828', 'BU950-0RLLI', 'Burgess', 1828, 3, 'Private', 'ACT') ,
(271, 14, 'BB21664', 'BU800-9GCBL', 'Burgess', 1664, 2, 'Private', 'ACT') ,
(272, 14, 'BB22265', 'BU200-1LMUI', 'Bushby', 2265, 2, 'Econ/Premium', 'INACT') ,
(273, 14, 'DD22255', 'DA782-5KCAJ', 'Dassault Falcon', 2255, 2, 'Econ/Premium', 'ACT') ,
(274, 14, 'EE32425', 'EM985-9OCBD', 'Embraer-Empresa Brasileira DR AeronÁutica', 2425, 3, 'Premium', 'ACT') ,
(275, 14, 'BB21648', 'BÜ200-1LMUI', 'Büttner Propeller', 1648, 2, 'Private', 'ACT') ,
(276, 14, 'AA3887', 'AI941-5LQKT', 'Airbus Corporate Jets', 887, 3, 'Premium', 'REP') ,
(277, 14, 'GG22127', 'GU856-3JEYV', 'Gulfstream Aerospace', 2127, 2, 'Premium', 'ACT') ,
(278, 14, 'DD12195', 'DA963-6FRIN', 'Dassault Falcon', 2195, 1, 'Econ/Premium', 'INACT') ,
(279, 14, 'BB11252', 'BU038-9VMAI', 'Buhl', 1252, 1, 'Econ/Premium', 'ACT') ,
(280, 14, 'BB31087', 'BÜ672-9JZZP', 'Büttner Propeller', 1087, 3, 'Econ/Premium', 'ACT') ,
(281, 15, 'BB3790', 'BU040-8WBTB', 'Buethe', 790, 3, 'Private', 'REP') ,
(282, 15, 'AA21938', 'AI189-6HXVJ', 'Airbus Corporate Jets', 1938, 2, 'Econ', 'INACT') ,
(283, 15, 'BB31951', 'BU869-3LKQA', 'Burnelli', 1951, 3, 'Econ/Premium', 'REP') ,
(284, 15, 'BB3681', 'BO038-9VMAI', 'Bombardier Aerospace', 681, 3, 'Econ/Premium', 'ACT') ,
(285, 15, 'BB11441', 'BU445-7ZKPG', 'Buethe', 1441, 1, 'Private', 'REP') ,
(286, 15, 'AA3792', 'AI709-3MKBC', 'Airbus Corporate Jets', 792, 3, 'Econ', 'ACT') ,
(287, 15, 'BB21279', 'BO038-9VMAI', 'Bombardier Aerospace', 1279, 2, 'Econ/Premium', 'REP') ,
(288, 15, 'BB21438', 'BO944-3BDSL', 'Bombardier Aerospace', 1438, 2, 'Econ', 'ACT') ,
(289, 15, 'TT31548', 'TE810-0XOKL', 'Textron Aviation', 1548, 3, 'Econ', 'ACT') ,
(290, 15, 'BB2826', 'BÜ464-3ANYM', 'Büttner Propeller', 826, 2, 'Econ/Premium', 'ACT') ,
(291, 15, 'BB21723', 'BÜ709-3MKBC', 'Büttner Propeller', 1723, 2, 'Econ', 'REP') ,
(292, 15, 'GG32467', 'GU423-7VVTJ', 'Gulfstream Aerospace', 2467, 3, 'Premium', 'REP') ,
(293, 15, 'EE2952', 'EM189-6HXVJ', 'Embraer-Empresa Brasileira DR AeronÁutica', 952, 2, 'Premium', 'REP') ,
(294, 15, 'BB3584', 'BU672-9JZZP', 'Buethe', 584, 3, 'Private', 'INACT') ,
(295, 15, 'BB32189', 'BU856-3JEYV', 'Bushby', 2189, 3, 'Private', 'REP') ,
(296, 15, 'AA21564', 'AI252-0JCJN', 'Airbus Corporate Jets', 1564, 2, 'Econ/Premium', 'ACT') ,
(297, 15, 'BB1757', 'BO200-1LMUI', 'Bombardier Aerospace', 757, 1, 'Private', 'ACT') ,
(298, 15, 'AA31666', 'AI985-9OCBD', 'Airbus Corporate Jets', 1666, 3, 'Premium', 'ACT') ,
(299, 15, 'BB21097', 'BU633-8FMIQ', 'Burgess', 1097, 2, 'Econ/Premium', 'ACT') ,
(300, 15, 'BB31135', 'BU464-3ANYM', 'Burgess', 1135, 3, 'Econ', 'REP') ,
(301, 16, 'BB22170', 'BU677-2FYOI', 'Buhl', 2170, 2, 'Premium', 'ACT') ,
(302, 16, 'BB11665', 'BU208-4FPOG', 'Burnelli', 1665, 1, 'Private', 'REP') ,
(303, 16, 'BB2647', 'BU148-4XRPQ', 'Burnelli', 647, 2, 'Private', 'ACT') ,
(304, 16, 'PP11362', 'PI399-2GHSD', 'Pilatus Business Aircraft', 1362, 1, 'Econ', 'INACT') ,
(305, 16, 'BB21477', 'BO764-3DVVD', 'Bombardier Aerospace', 1477, 2, 'Econ/Premium', 'ACT') ,
(306, 16, 'DD3654', 'DA977-2LNVY', 'Dassault Falcon', 654, 3, 'Private', 'REP') ,
(307, 16, 'BB2677', 'BY034-3IVQO', 'Bye Aerospace', 677, 2, 'Private', 'ACT') ,
(308, 16, 'GG12235', 'GU445-7ZKPG', 'Gulfstream Aerospace', 2235, 1, 'Econ', 'REP') ,
(309, 16, 'BB2987', 'BU634-3QCUZ', 'Buhl', 987, 2, 'Econ', 'REP') ,
(310, 16, 'PP21307', 'PI464-3ANYM', 'Pilatus Business Aircraft', 1307, 2, 'Econ/Premium', 'ACT') ,
(311, 16, 'AA1642', 'AI916-7WHGQ', 'Airbus Corporate Jets', 642, 1, 'Private', 'ACT') ,
(312, 16, 'BB22028', 'BY728-2AFDZ', 'Bye Aerospace', 2028, 2, 'Econ', 'INACT') ,
(313, 16, 'DD12358', 'DA250-3IZRJ', 'Dassault Falcon', 2358, 1, 'Econ/Premium', 'REP') ,
(314, 16, 'BB21555', 'BY760-8ZSGL', 'Bye Aerospace', 1555, 2, 'Premium', 'REP') ,
(315, 16, 'GG21034', 'GU423-7VVTJ', 'Gulfstream Aerospace', 1034, 2, 'Econ/Premium', 'REP') ,
(316, 16, 'GG31895', 'GU520-5QWGV', 'Gulfstream Aerospace', 1895, 3, 'Premium', 'INACT') ,
(317, 16, 'TT11216', 'TE891-9LGJU', 'Textron Aviation', 1216, 1, 'Private', 'ACT') ,
(318, 16, 'BB31447', 'BO782-5KCAJ', 'Boeing Business Jets', 1447, 3, 'Premium', 'INACT') ,
(319, 16, 'BB22015', 'BU832-2DMTK', 'Bushby', 2015, 2, 'Econ', 'ACT') ,
(320, 16, 'GG21117', 'GU200-1LMUI', 'Gulfstream Aerospace', 1117, 2, 'Premium', 'INACT') ,
(321, 17, 'BB31063', 'BÜ699-6TLUQ', 'Büttner Propeller', 1063, 3, 'Premium', 'INACT') ,
(322, 17, 'TT3654', 'TE985-9OCBD', 'Textron Aviation', 654, 3, 'Premium', 'REP') ,
(323, 17, 'BB11958', 'BU551-0RCSM', 'Buhl', 1958, 1, 'Private', 'INACT') ,
(324, 17, 'BB11672', 'BU538-8MVJV', 'Burnelli', 1672, 1, 'Econ', 'ACT') ,
(325, 17, 'EE11446', 'EM477-6HHYX', 'Embraer-Empresa Brasileira DR AeronÁutica', 1446, 1, 'Private', 'INACT') ,
(326, 17, 'BB2811', 'BU800-9GCBL', 'Buhl', 811, 2, 'Premium', 'INACT') ,
(327, 17, 'BB3726', 'BY996-7RTPT', 'Bye Aerospace', 726, 3, 'Econ', 'INACT') ,
(328, 17, 'GG2594', 'GU040-8WBTB', 'Gulfstream Aerospace', 594, 2, 'Econ/Premium', 'REP') ,
(329, 17, 'BB12263', 'BY800-9GCBL', 'Bye Aerospace', 2263, 1, 'Private', 'INACT') ,
(330, 17, 'BB21732', 'BÜ140-1IWYA', 'Büttner Propeller', 1732, 2, 'Private', 'INACT') ,
(331, 17, 'EE31098', 'EM132-9CXSN', 'Embraer-Empresa Brasileira DR AeronÁutica', 1098, 3, 'Econ/Premium', 'INACT') ,
(332, 17, 'BB12346', 'BU477-6HHYX', "Burl's Aircraft", 2346, 1, 'Premium', 'INACT') ,
(333, 17, 'BB31091', 'BU423-7VVTJ', 'Buhl', 1091, 3, 'Private', 'REP') ,
(334, 17, 'BB2567', 'BÜ034-3IVQO', 'Büttner Propeller', 567, 2, 'Premium', 'INACT') ,
(335, 17, 'DD1733', 'DA716-5MQKS', 'Dassault Falcon', 733, 1, 'Private', 'ACT') ,
(336, 17, 'BB31121', 'BÜ732-2YRMW', 'Büttner Propeller', 1121, 3, 'Private', 'ACT') ,
(337, 17, 'BB21059', 'BU132-9CXSN', 'Bushby', 1059, 2, 'Premium', 'ACT') ,
(338, 17, 'BB22366', 'BU941-5LQKT', 'Buhl', 2366, 2, 'Private', 'INACT') ,
(339, 17, 'BB11342', 'BU411-3XVVO', 'Burgess', 1342, 1, 'Private', 'ACT') ,
(340, 17, 'TT31887', 'TE732-2YRMW', 'Textron Aviation', 1887, 3, 'Econ', 'INACT') ,
(341, 18, 'TT11582', 'TE538-8MVJV', 'Textron Aviation', 1582, 1, 'Econ', 'INACT') ,
(342, 18, 'BB12063', 'BU273-2DJVB', 'Bushby', 2063, 1, 'Econ/Premium', 'REP') ,
(343, 18, 'TT31576', 'TE651-2LXYQ', 'Textron Aviation', 1576, 3, 'Private', 'INACT') ,
(344, 18, 'BB32113', 'BU699-6TLUQ', 'Buethe', 2113, 3, 'Premium', 'INACT') ,
(345, 18, 'BB2688', 'BO432-4SAWP', 'Bombardier Aerospace', 688, 2, 'Econ', 'ACT') ,
(346, 18, 'BB3707', 'BÜ532-8VNYA', 'Büttner Propeller', 707, 3, 'Premium', 'REP') ,
(347, 18, 'BB22034', 'BU944-3BDSL', 'Buhl', 2034, 2, 'Econ/Premium', 'REP') ,
(348, 18, 'BB3698', 'BU651-2LXYQ', 'Burgess', 698, 3, 'Private', 'REP') ,
(349, 18, 'PP22478', 'PI866-5SNGB', 'Pilatus Business Aircraft', 2478, 2, 'Premium', 'ACT') ,
(350, 18, 'PP12411', 'PI798-8QYRO', 'Pilatus Business Aircraft', 2411, 1, 'Private', 'INACT') ,
(351, 18, 'EE11853', 'EM663-5XCSJ', 'Embraer-Empresa Brasileira DR AeronÁutica', 1853, 1, 'Econ/Premium', 'REP') ,
(352, 18, 'BB21462', 'BY671-0BCGZ', 'Bye Aerospace', 1462, 2, 'Econ', 'INACT') ,
(353, 18, 'BB31171', 'BU375-9HBMB', 'Burnelli', 1171, 3, 'Private', 'ACT') ,
(354, 18, 'BB31417', 'BU208-4FPOG', "Burl's Aircraft", 1417, 3, 'Econ/Premium', 'INACT') ,
(355, 18, 'BB12340', 'BÜ411-3XVVO', 'Büttner Propeller', 2340, 1, 'Econ/Premium', 'ACT') ,
(356, 18, 'BB32126', 'BO709-3MKBC', 'Boeing Business Jets', 2126, 3, 'Econ/Premium', 'INACT') ,
(357, 18, 'EE21376', 'EM672-9JZZP', 'Embraer-Empresa Brasileira DR AeronÁutica', 1376, 2, 'Econ/Premium', 'INACT') ,
(358, 18, 'BB31937', 'BU166-6EDCR', 'Burgess', 1937, 3, 'Econ/Premium', 'REP') ,
(359, 18, 'BB11678', 'BU671-0BCGZ', 'Bushby', 1678, 1, 'Private', 'INACT') ,
(360, 18, 'BB31126', 'BU667-7AWLH', "Burl's Aircraft", 1126, 3, 'Econ/Premium', 'REP') ,
(361, 19, 'BB31153', 'BO760-8ZSGL', 'Boeing Business Jets', 1153, 3, 'Private', 'REP') ,
(362, 19, 'BB21368', 'BU944-3BDSL', 'Buethe', 1368, 2, 'Private', 'INACT') ,
(363, 19, 'BB21850', 'BO387-5REYZ', 'Boeing Business Jets', 1850, 2, 'Premium', 'INACT') ,
(364, 19, 'BB32229', 'BU132-9CXSN', 'Burgess', 2229, 3, 'Premium', 'INACT') ,
(365, 19, 'GG11835', 'GU944-3BDSL', 'Gulfstream Aerospace', 1835, 1, 'Econ/Premium', 'ACT') ,
(366, 19, 'EE22000', 'EM445-7ZKPG', 'Embraer-Empresa Brasileira DR AeronÁutica', 2000, 2, 'Premium', 'REP') ,
(367, 19, 'TT22157', 'TE445-7ZKPG', 'Textron Aviation', 2157, 2, 'Premium', 'ACT') ,
(368, 19, 'DD21148', 'DA189-6HXVJ', 'Dassault Falcon', 1148, 2, 'Private', 'ACT') ,
(369, 19, 'BB22257', 'BÜ971-1MNGO', 'Büttner Propeller', 2257, 2, 'Econ', 'INACT') ,
(370, 19, 'BB2907', 'BU667-7AWLH', 'Buethe', 907, 2, 'Econ', 'INACT') ,
(371, 19, 'AA1731', 'AI977-2NTHG', 'Airbus Corporate Jets', 731, 1, 'Private', 'ACT') ,
(372, 19, 'PP11764', 'PI873-8YOQU', 'Pilatus Business Aircraft', 1764, 1, 'Premium', 'INACT') ,
(373, 19, 'BB12047', 'BU750-9QONA', 'Burgess', 2047, 1, 'Econ/Premium', 'REP') ,
(374, 19, 'DD12315', 'DA986-6KDJJ', 'Dassault Falcon', 2315, 1, 'Econ', 'REP') ,
(375, 19, 'BB21699', 'BU203-3JCWQ', 'Bushby', 1699, 2, 'Private', 'REP') ,
(376, 19, 'BB21482', 'BU551-0RCSM', 'Burgess', 1482, 2, 'Private', 'ACT') ,
(377, 19, 'PP32323', 'PI832-2DMTK', 'Pilatus Business Aircraft', 2323, 3, 'Premium', 'INACT') ,
(378, 19, 'BB31562', 'BU203-3JCWQ', 'Bushby', 1562, 3, 'Econ', 'INACT') ,
(379, 19, 'BB31219', 'BÜ520-5QWGV', 'Büttner Propeller', 1219, 3, 'Private', 'ACT') ,
(380, 19, 'GG11085', 'GU977-2NTHG', 'Gulfstream Aerospace', 1085, 1, 'Premium', 'REP') ,
(381, 20, 'PP11600', 'PI520-5QWGV', 'Pilatus Business Aircraft', 1600, 1, 'Private', 'REP') ,
(382, 20, 'PP21316', 'PI532-8VNYA', 'Pilatus Business Aircraft', 1316, 2, 'Premium', 'INACT') ,
(383, 20, 'BB11011', 'BO140-1IWYA', 'Bombardier Aerospace', 1011, 1, 'Econ/Premium', 'ACT') ,
(384, 20, 'BB11042', 'BU810-0XOKL', 'Burgess', 1042, 1, 'Econ', 'REP') ,
(385, 20, 'BB11216', 'BY375-9HBMB', 'Bye Aerospace', 1216, 1, 'Private', 'REP') ,
(386, 20, 'BB2716', 'BU673-0UBWG', 'Burnelli', 716, 2, 'Econ', 'ACT') ,
(387, 20, 'TT12408', 'TE985-9OCBD', 'Textron Aviation', 2408, 1, 'Premium', 'ACT') ,
(388, 20, 'EE3717', 'EM634-3QCUZ', 'Embraer-Empresa Brasileira DR AeronÁutica', 717, 3, 'Econ/Premium', 'REP') ,
(389, 20, 'BB11483', 'BU189-6HXVJ', 'Buhl', 1483, 1, 'Econ/Premium', 'INACT') ,
(390, 20, 'BB22128', 'BY532-8VNYA', 'Bye Aerospace', 2128, 2, 'Econ/Premium', 'REP') ,
(391, 20, 'TT12438', 'TE732-2YRMW', 'Textron Aviation', 2438, 1, 'Econ/Premium', 'INACT') ,
(392, 20, 'BB2926', 'BU477-6HHYX', 'Buethe', 926, 2, 'Econ', 'INACT') ,
(393, 20, 'DD2712', 'DA423-7VVTJ', 'Dassault Falcon', 712, 2, 'Econ/Premium', 'INACT') ,
(394, 20, 'BB31046', 'BU677-2FYOI', 'Buethe', 1046, 3, 'Private', 'INACT') ,
(395, 20, 'BB11404', 'BÜ220-9JCDF', 'Büttner Propeller', 1404, 1, 'Econ/Premium', 'REP') ,
(396, 20, 'BB12439', 'BY203-3JCWQ', 'Bye Aerospace', 2439, 1, 'Econ', 'ACT') ,
(397, 20, 'BB11319', 'BO634-3QCUZ', 'Bombardier Aerospace', 1319, 1, 'Premium', 'REP') ,
(398, 20, 'BB22153', 'BU432-4SAWP', 'Buethe', 2153, 2, 'Private', 'INACT') ,
(399, 20, 'GG21683', 'GU445-7ZKPG', 'Gulfstream Aerospace', 1683, 2, 'Econ/Premium', 'INACT') ,
(400, 20, 'BB1865', 'BU773-9RRSK', 'Burgess', 865, 1, 'Private', 'ACT') ,
(401, 21, 'BB21830', 'BO034-3IVQO', 'Bombardier Aerospace', 1830, 2, 'Econ', 'ACT') ,
(402, 21, 'EE1507', 'EM220-9JCDF', 'Embraer-Empresa Brasileira DR AeronÁutica', 507, 1, 'Econ/Premium', 'REP') ,
(403, 21, 'BB32312', 'BÜ672-9JZZP', 'Büttner Propeller', 2312, 3, 'Econ/Premium', 'REP') ,
(404, 21, 'BB1664', 'BO399-2GHSD', 'Boeing Business Jets', 664, 1, 'Econ/Premium', 'INACT') ,
(405, 21, 'BB12326', 'BU782-5KCAJ', "Burl's Aircraft", 2326, 1, 'Private', 'INACT') ,
(406, 21, 'BB12346', 'BU532-8VNYA', 'Burnelli', 2346, 1, 'Econ/Premium', 'INACT') ,
(407, 21, 'BB21344', 'BU250-3IZRJ', "Burl's Aircraft", 1344, 2, 'Econ/Premium', 'ACT') ,
(408, 21, 'DD21143', 'DA971-1MNGO', 'Dassault Falcon', 1143, 2, 'Premium', 'REP') ,
(409, 21, 'AA1630', 'AI148-4XRPQ', 'Airbus Corporate Jets', 630, 1, 'Premium', 'ACT') ,
(410, 21, 'GG2740', 'GU034-3IVQO', 'Gulfstream Aerospace', 740, 2, 'Private', 'ACT') ,
(411, 21, 'GG32468', 'GU399-2GHSD', 'Gulfstream Aerospace', 2468, 3, 'Econ/Premium', 'ACT') ,
(412, 21, 'BB11994', 'BY447-1JCVI', 'Bye Aerospace', 1994, 1, 'Premium', 'REP') ,
(413, 21, 'EE32282', 'EM202-9SCLT', 'Embraer-Empresa Brasileira DR AeronÁutica', 2282, 3, 'Private', 'REP') ,
(414, 21, 'BB31836', 'BO663-5XCSJ', 'Bombardier Aerospace', 1836, 3, 'Private', 'REP') ,
(415, 21, 'BB3700', 'BU313-7TJGA', 'Bushby', 700, 3, 'Econ', 'ACT') ,
(416, 21, 'PP1909', 'PI252-0JCJN', 'Pilatus Business Aircraft', 909, 1, 'Private', 'INACT') ,
(417, 21, 'BB12460', 'BU203-3JCWQ', 'Buhl', 2460, 1, 'Private', 'INACT') ,
(418, 21, 'BB11966', 'BU944-3BDSL', 'Bushby', 1966, 1, 'Econ', 'ACT') ,
(419, 21, 'DD3917', 'DA633-8FMIQ', 'Dassault Falcon', 917, 3, 'Private', 'REP') ,
(420, 21, 'DD31570', 'DA050-9JDGO', 'Dassault Falcon', 1570, 3, 'Premium', 'REP') ,
(421, 22, 'EE2790', 'EM443-5LZYA', 'Embraer-Empresa Brasileira DR AeronÁutica', 790, 2, 'Private', 'INACT') ,
(422, 22, 'BB1754', 'BU651-2LXYQ', 'Bushby', 754, 1, 'Private', 'REP') ,
(423, 22, 'BB2573', 'BO663-5XCSJ', 'Boeing Business Jets', 573, 2, 'Econ', 'ACT') ,
(424, 22, 'EE2932', 'EM148-4XRPQ', 'Embraer-Empresa Brasileira DR AeronÁutica', 932, 2, 'Econ', 'ACT') ,
(425, 22, 'BB3501', 'BU200-8KKUZ', 'Burnelli', 501, 3, 'Econ/Premium', 'INACT') ,
(426, 22, 'AA21826', 'AI423-7VVTJ', 'Airbus Corporate Jets', 1826, 2, 'Econ/Premium', 'ACT') ,
(427, 22, 'BB31557', 'BU944-3BDSL', 'Bushby', 1557, 3, 'Econ/Premium', 'INACT') ,
(428, 22, 'BB3956', 'BO764-3DVVD', 'Boeing Business Jets', 956, 3, 'Econ', 'ACT') ,
(429, 22, 'BB3822', 'BY714-2HAXR', 'Bye Aerospace', 822, 3, 'Premium', 'REP') ,
(430, 22, 'BB31401', 'BU992-5DYJF', 'Buhl', 1401, 3, 'Premium', 'REP') ,
(431, 22, 'BB11141', 'BY004-9VHRK', 'Bye Aerospace', 1141, 1, 'Premium', 'INACT') ,
(432, 22, 'TT11608', 'TE200-1LMUI', 'Textron Aviation', 1608, 1, 'Econ/Premium', 'INACT') ,
(433, 22, 'GG11607', 'GU916-7WHGQ', 'Gulfstream Aerospace', 1607, 1, 'Econ/Premium', 'INACT') ,
(434, 22, 'BB1994', 'BU866-5SNGB', 'Buethe', 994, 1, 'Premium', 'ACT') ,
(435, 22, 'BB31516', 'BU375-9HBMB', 'Bushby', 1516, 3, 'Econ/Premium', 'REP') ,
(436, 22, 'BB12203', 'BO538-8MVJV', 'Bombardier Aerospace', 2203, 1, 'Econ', 'REP') ,
(437, 22, 'BB3538', 'BU464-3ANYM', 'Burgess', 538, 3, 'Private', 'INACT') ,
(438, 22, 'BB21152', 'BÜ941-5LQKT', 'Büttner Propeller', 1152, 2, 'Private', 'REP') ,
(439, 22, 'BB32035', 'BU432-4SAWP', 'Buethe', 2035, 3, 'Econ', 'INACT') ,
(440, 22, 'BB22081', 'BU464-3ANYM', "Burl's Aircraft", 2081, 2, 'Premium', 'REP') ,
(441, 23, 'GG21808', 'GU764-3DVVD', 'Gulfstream Aerospace', 1808, 2, 'Econ', 'ACT') ,
(442, 23, 'AA12083', 'AI798-8QYRO', 'Airbus Corporate Jets', 2083, 1, 'Econ/Premium', 'ACT') ,
(443, 23, 'GG31797', 'GU520-5QWGV', 'Gulfstream Aerospace', 1797, 3, 'Econ', 'INACT') ,
(444, 23, 'BB31476', 'BY977-2NTHG', 'Bye Aerospace', 1476, 3, 'Premium', 'INACT') ,
(445, 23, 'BB1533', 'BU200-1LMUI', "Burl's Aircraft", 533, 1, 'Private', 'INACT') ,
(446, 23, 'BB3846', 'BY728-2AFDZ', 'Bye Aerospace', 846, 3, 'Private', 'REP') ,
(447, 23, 'PP11848', 'PI716-5MQKS', 'Pilatus Business Aircraft', 1848, 1, 'Econ/Premium', 'INACT') ,
(448, 23, 'BB11735', 'BÜ411-3XVVO', 'Büttner Propeller', 1735, 1, 'Private', 'REP') ,
(449, 23, 'AA12395', 'AI856-3JEYV', 'Airbus Corporate Jets', 2395, 1, 'Econ', 'ACT') ,
(450, 23, 'BB11681', 'BU663-5XCSJ', 'Buethe', 1681, 1, 'Premium', 'REP') ,
(451, 23, 'BB1666', 'BY313-7TJGA', 'Bye Aerospace', 666, 1, 'Econ', 'REP') ,
(452, 23, 'BB31703', 'BO992-5DYJF', 'Boeing Business Jets', 1703, 3, 'Premium', 'ACT') ,
(453, 23, 'BB2569', 'BU944-3BDSL', "Burl's Aircraft", 569, 2, 'Econ/Premium', 'REP') ,
(454, 23, 'BB11584', 'BO050-9JDGO', 'Bombardier Aerospace', 1584, 1, 'Premium', 'REP') ,
(455, 23, 'BB3557', 'BU432-4SAWP', 'Buhl', 557, 3, 'Econ', 'REP') ,
(456, 23, 'BB3623', 'BO671-0BCGZ', 'Bombardier Aerospace', 623, 3, 'Econ/Premium', 'REP') ,
(457, 23, 'EE11303', 'EM750-9QONA', 'Embraer-Empresa Brasileira DR AeronÁutica', 1303, 1, 'Econ', 'REP') ,
(458, 23, 'BB2707', 'BU166-6EDCR', 'Burgess', 707, 2, 'Econ/Premium', 'ACT') ,
(459, 23, 'AA21702', 'AI252-0JCJN', 'Airbus Corporate Jets', 1702, 2, 'Econ/Premium', 'ACT') ,
(460, 23, 'TT22116', 'TE050-9JDGO', 'Textron Aviation', 2116, 2, 'Premium', 'ACT') ,
(461, 24, 'BB31948', 'BU673-0UBWG', "Burl's Aircraft", 1948, 3, 'Econ/Premium', 'INACT') ,
(462, 24, 'TT11547', 'TE750-9QONA', 'Textron Aviation', 1547, 1, 'Econ', 'INACT') ,
(463, 24, 'GG11279', 'GU443-5LZYA', 'Gulfstream Aerospace', 1279, 1, 'Premium', 'REP') ,
(464, 24, 'BB31362', 'BO651-2LXYQ', 'Boeing Business Jets', 1362, 3, 'Private', 'REP') ,
(465, 24, 'BB21014', 'BY732-2YRMW', 'Bye Aerospace', 1014, 2, 'Econ/Premium', 'REP') ,
(466, 24, 'BB22213', 'BU375-9HBMB', 'Burgess', 2213, 2, 'Private', 'REP') ,
(467, 24, 'BB31553', 'BO252-0JCJN', 'Boeing Business Jets', 1553, 3, 'Econ', 'INACT') ,
(468, 24, 'TT11185', 'TE985-9OCBD', 'Textron Aviation', 1185, 1, 'Premium', 'REP') ,
(469, 24, 'BB2598', 'BU252-0JCJN', 'Bushby', 598, 2, 'Premium', 'REP') ,
(470, 24, 'BB31590', 'BU950-0RLLI', 'Burgess', 1590, 3, 'Premium', 'INACT') ,
(471, 24, 'BB3892', 'BU839-9DOST', 'Burnelli', 892, 3, 'Econ/Premium', 'ACT') ,
(472, 24, 'BB22439', 'BU220-9JCDF', 'Bushby', 2439, 2, 'Premium', 'ACT') ,
(473, 24, 'GG11114', 'GU873-8YOQU', 'Gulfstream Aerospace', 1114, 1, 'Econ/Premium', 'ACT') ,
(474, 24, 'BB1970', 'BU916-7WHGQ', 'Buethe', 970, 1, 'Premium', 'ACT') ,
(475, 24, 'PP21631', 'PI709-3MKBC', 'Pilatus Business Aircraft', 1631, 2, 'Econ', 'INACT') ,
(476, 24, 'BB1539', 'BU651-2LXYQ', "Burl's Aircraft", 539, 1, 'Econ/Premium', 'REP') ,
(477, 24, 'BB21455', 'BU992-5DYJF', 'Bushby', 1455, 2, 'Econ', 'REP') ,
(478, 24, 'TT22069', 'TE477-6HHYX', 'Textron Aviation', 2069, 2, 'Econ', 'INACT') ,
(479, 24, 'BB22111', 'BU672-9JZZP', 'Burgess', 2111, 2, 'Premium', 'REP') ,
(480, 24, 'BB3637', 'BO477-6HHYX', 'Boeing Business Jets', 637, 3, 'Econ', 'INACT') ,
(481, 25, 'BB21248', 'BO667-7AWLH', 'Boeing Business Jets', 1248, 2, 'Private', 'INACT') ,
(482, 25, 'BB11640', 'BU873-0UVAD', 'Buethe', 1640, 1, 'Premium', 'INACT') ,
(483, 25, 'BB1998', 'BU764-3DVVD', 'Buethe', 998, 1, 'Econ', 'REP') ,
(484, 25, 'BB21392', 'BU782-5KCAJ', "Burl's Aircraft", 1392, 2, 'Private', 'REP') ,
(485, 25, 'BB11091', 'BY714-2HAXR', 'Bye Aerospace', 1091, 1, 'Econ', 'ACT') ,
(486, 25, 'BB21435', 'BU672-9JZZP', 'Buhl', 1435, 2, 'Econ', 'INACT') ,
(487, 25, 'DD12341', 'DA944-3BDSL', 'Dassault Falcon', 2341, 1, 'Econ', 'INACT') ,
(488, 25, 'TT31558', 'TE399-2GHSD', 'Textron Aviation', 1558, 3, 'Econ/Premium', 'INACT') ,
(489, 25, 'TT32280', 'TE916-7WHGQ', 'Textron Aviation', 2280, 3, 'Private', 'INACT') ,
(490, 25, 'AA31068', 'AI651-2LXYQ', 'Airbus Corporate Jets', 1068, 3, 'Econ/Premium', 'INACT') ,
(491, 25, 'GG32169', 'GU538-8MVJV', 'Gulfstream Aerospace', 2169, 3, 'Econ', 'REP') ,
(492, 25, 'TT31764', 'TE732-2YRMW', 'Textron Aviation', 1764, 3, 'Econ', 'ACT') ,
(493, 25, 'BB12131', 'BU399-2GHSD', "Burl's Aircraft", 2131, 1, 'Econ', 'REP') ,
(494, 25, 'BB31719', 'BU551-0RCSM', 'Burnelli', 1719, 3, 'Econ', 'REP') ,
(495, 25, 'BB21966', 'BU663-5XCSJ', 'Buethe', 1966, 2, 'Premium', 'INACT') ,
(496, 25, 'BB32055', 'BU760-8ZSGL', 'Buhl', 2055, 3, 'Private', 'INACT') ,
(497, 25, 'TT3837', 'TE944-3BDSL', 'Textron Aviation', 837, 3, 'Private', 'REP') ,
(498, 25, 'BB3989', 'BU189-6HXVJ', 'Burgess', 989, 3, 'Econ/Premium', 'REP') ,
(499, 25, 'BB11584', 'BÜ250-3IZRJ', 'Büttner Propeller', 1584, 1, 'Econ/Premium', 'INACT') ,
(500, 25, 'BB11807', 'BU273-2DJVB', 'Bushby', 1807, 1, 'Premium', 'INACT')]