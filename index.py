import numpy as np

class Auto:
    def __init__(self, patente, horaIngreso, horaSalida="Ninguno"):
        self.patente = patente
        self.horaIngreso = horaIngreso
        self.horaSalida = horaSalida
    
    # STR
    def __str__(self):
        x = "Patente :" + str(self.patente) + "\n" + "Hora de ingreso:" + str(self.horaIngreso) + "\n" + "Hora de Salida:" + str(self.horaSalida) + "\n"
        return x



class Sector:
    def __init__(self, denominacion,capacidad, valorHora):
        self.__denominacion=denominacion
        self.__capacidad = capacidad
        self.__valorHora = valorHora
        self.__autos = np.zeros(self.__capacidad, Auto)
        self.__actual=0
        self.__recaudacionDia=0

    def __str__(self):
        ret = ""
        for i in range(len(self.__autos)):
            if self.__autos[i] != 0:
                ret += str(self.__autos[i])
        return ret

    def hayLugar(self):
        for i in range(self.__capacidad):
           if self.__autos[i]==0:
               return True
        return False

    def __lugarLibre(self):
        for i in range(self.__capacidad):
            if self.__autos[i] == 0:
                return i          
    def ingresarAuto(self, auto):
        self.__autos[self.__lugarLibre()] = auto
        self.__actual+=1
    
    def buscarAuto(self, patente):
        for i in range(self.__capacidad):
            if self.__autos[i] != 0:
                if self.__autos[i].patente == patente:
                    return True
        return False

    def darPosicion(self, patente):
        for i in range(self.__capacidad):
            if self.__autos[i] != 0:
                if self.__autos[i].patente == patente:
                    return i
            return False


    def egresarAuto(self, patente, horaSalida):
        for i in range(self.__capacidad):
            if self.__autos[i] != 0:
                if self.__autos[i].patente == patente:
                   

                   self.__autos[i].horaSalida = horaSalida

                   x2 = self.calcularPlata(horaSalida, self.__autos[i].horaIngreso)
                   self.__autos[i].patente = 0
                   self.__recaudacionDia += x2
                   
                   return True
            else:
                return False

    
    #metodo que recorre todo el sector calculando lo recaudado
    def calcularPlata(self, s, e):
        x = s - e
        x2 = x*self.__valorHora
        return x2
    
    #metodo que devuelve lo recaudado por sector
    def getRecaudacion(self):
       
        return self.__recaudacionDia 
    
    #verificacion de autos
    def hayAutos(self):
        for i in range(self.__capacidad):
            if self.__autos[i] != 0:
               return True
            else:
               False
       
       


class Estacionamiento:
  def __init__(self, nombre,docente, alumno, general):
    self.__nombre=nombre
    self.__sectorDocente = docente
    self.__sectorAlumno = alumno
    self.__sectorGeneral = general

  def __str__(self):
    cadenaPrint = str(self.__nombre) + " " + str(self.__sectorDocente) + " " + str(self.__sectorAlumno) + " " +  str(self.__sectorGeneral) + ""
    return cadenaPrint

  def getNombre(self):
    return self.__nombre

  def ingresarAuto(self, sector, auto):
    
    if sector == "Docente":
      self.__sectorDocente.ingresarAuto(auto)
    elif sector == "Alumno":
      self.__sectorAlumno.ingresarAuto(auto)
    else:
      self.__sectorGeneral.ingresarAuto(auto)

  def egresarAuto(self, sector, patente, horaSalida):
    if sector == "Docente":
      self.__sectorDocente.egresarAuto(patente,horaSalida)
    elif sector == "Alumno":
      self.__sectorAlumno.egresarAuto(patente,horaSalida)
    else:
      self.__sectorGeneral.egresarAuto(patente,horaSalida)
  
  def buscarAuto(self, patente):

    if self.__sectorDocente.buscarAuto(patente):
      return True
    if self.__sectorAlumno.buscarAuto(patente):
      return True
    if self.__sectorGeneral.buscarAuto(patente):
      return True

    return False

  def hayLugar(self, sector):
    if sector == "Docente":
      return self.__sectorDocente.hayLugar()
    elif sector == "Alumno":
      return self.__sectorAlumno.hayLugar()
    else:
      return self.__sectorGeneral.hayLugar()


  def calcularPlata(self):
    ret = 0
    ret += self.__sectorDocente.getRecaudacion()
    ret += self.__sectorAlumno.getRecaudacion()
    ret += self.__sectorGeneral.getRecaudacion()
    return ret

  def listarPorSector(self):

    if self.__sectorAlumno.hayAutos():
      print("Autos en el Sector Alumno")
      print(self.__sectorAlumno)
    else:
      print("En el Sector Alumno no hay Autos")

    if self.__sectorDocente.hayAutos():
      print("Autos en el Sector Docente")
      print(self.__sectorDocente)
    else:
      print("En el Sector Docente no hay Autos")

    if self.__sectorGeneral.hayAutos():
      print("Autos en el Sector General")
      print(self.__sectorGeneral)
    else:
      print("En el Sector General no hay Autos")


def main():
  secDocente=Sector('Docente',50,10)
  secAlumno=Sector('Alumno',50,5)
  secGeneral=Sector('General',100,20)
  unahur = Estacionamiento('unahur',secDocente,secAlumno,secGeneral)
  unahur.ingresarAuto('Docente',Auto('AAA123',10))
  unahur.ingresarAuto('Alumno', Auto('ABB123',1))
  unahur.ingresarAuto('General',Auto('ABC321',23))
  unahur.listarPorSector()
  unahur.ingresarAuto('Docente', Auto('ZZZ123', 8))
  unahur.ingresarAuto('Alumno', Auto('XXX123', 4))
  if unahur.hayLugar('General'):
    unahur.ingresarAuto('General', Auto('YYY321', 2))
  unahur.ingresarAuto('Docente', Auto('JJJ123', 5))
  unahur.ingresarAuto('Alumno', Auto('HHH123', 6))
  unahur.ingresarAuto('General', Auto('FFF321', 23))
  if unahur.buscarAuto('YYY321'):
    unahur.egresarAuto('General','YYY321',13)
  if unahur.buscarAuto('KKK345'):
    unahur.egresarAuto('Docente','KKK345',2)
  else:
    print(f"El auto no se encuentra en el estacionamiento")
  unahur.egresarAuto('Docente', 'JJJ123', 21)
  unahur.egresarAuto('Alumno', 'HHH123', 8)
  unahur.egresarAuto('General', 'FFF321', 24)
  print(f"Total recaudado {unahur.calcularPlata()}")



main()




