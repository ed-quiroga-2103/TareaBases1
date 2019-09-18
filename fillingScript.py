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

aerolineas = getAeropuertosAndAerolineas()[0]

empleados = getEmpleadosAerolinea()

aerolineaAeropuerto = getAerolineaAeropuerto()

empleadosAerolinea = empleados[1]

empleados = empleados[0]

aviones = getAviones(80)

vuelos = getVuelos()

bodegas = getBodega(aviones)

talleres = getTaller(aviones)

createControladorVuelo(aviones,vuelos)

HEAD