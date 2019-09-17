from random import choice
import string

def linesToList(path):
    file = open(path,"r")
    nameList = []

    for line in file:
        line = line.rstrip()      
        if line:                  
            nameList.append(line)

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


def createEmployeeAeropuerto(nameList, lastNameList,idNum):

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

    code = name[0].upper() + name [1].upper() + name[2].upper()

    sched = choice(["De 5 A.M. a 1 A.M.", "De 7 A.M. a 7 P.M.", "De 4 A.M. a 12 M.N.", "24/7"])

    return (idNum,name,phone,location,hours,code)


def createAerolinea(name, idNum):

    code = name[0].upper() + name [1].upper() + name[2].upper()

    return (idNum,code,name)

def createAvion(idNum, manufact, idAero, aeroCode):

    model = ""

    for i in range(4):
        model += choice(string.ascii_uppercase)

    model += manufact[0].upper() + manufact[1].upper()

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

    ind = choice(range(5))

    iniTimes = ["01:00:00", "13:45:00", "17:00:00", "19:00:00"]
    finTimes = ["05:30:00", "17:00:00", "23:00:00", "22:45:00"] 

    time1 = iniTimes[ind]
    time2 = finTimes[ind]

    datetime1 = date+" "+time1
    datetime2 = date+" "+time2

    return (idNum, idAero, idAvion, num, destiny, origin, datetime1, datetime2, price, state)

def createPasajero(idNum, idVuelo, nameList, lastNameList):

    numVuelo = idVuelo
    bags = choice(range(5))
    name = choice(nameList)
    lastname1 = choice(lastNameList)
    lastname2 = choice(lastNameList)
    code = numVuelo + name[0].upper() + lastname1[0].upper() + lastname2[0].upper()
    passport = ""
    for i in range(8):
        passport += str(choice(range(10)))
    phone = ""

    for i in range(8):
        phone += str(choice(range(10)))

    return (idNum, idVuelo,numVuelo,bags,code,name,lastname1,lastname2,passport,phone)

def createEquipaje(idNum, idPasajero, pasCode):

    code = idNum + pasCode

    weight = choice(range(50))

    return (idNum, idPasajero, code, weight)

def createControlador(idNum):
    return (idNum)

def createEmpleadoAerolinea(idEmpl, idAero, job):

    sched = choice(["De 5 A.M. a 1 A.M.", "De 7 A.M. a 7 P.M.", "De 4 A.M. a 12 M.N.", "24/7"])

    return (idEmpl, idAero, sched, job)

def createEmpleadoAeropuerto(idEmpl, idAero, job):

    address = choice(["Alajuela", "Cartago", "San José", "Heredia","Puntarenas","Guanacaste","Limon"])

    return (idEmpl, idAero, address, job)


