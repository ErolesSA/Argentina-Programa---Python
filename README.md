# Argentina-Programa---Python
Argentina Programa - Python


Curso que forma parte de la propuesta de formación de Argentina Programa y se dicta en el marco de un convenio con la Universidad Nacional de Hurlingham.

Problema:

Enunciado:
Dada la creciente demanda de autos en el estacionamiento de UNAHUR por el regreso a las
clases presenciales, la universidad nos solicitó ayuda para comenzar a tarifar el
estacionamiento.
El estacionamiento tiene una capacidad máxima en general, y a su vez tiene sectores que
tienen su propia capacidad.

● El sector docente tiene 50 lugares y cuesta $10 la hora.
● El sector de alumnos tiene 50 lugares y cuesta $5 la hora.
● Y el sector general, que tiene 100 lugares, cuesta $20 la hora.

Tener en cuenta las siguientes especificaciones:
a) Cada vez que ingresa un auto al estacionamiento, se registra la hora de ingreso y el
sector en donde se estaciona.
b) No se puede exceder la capacidad y se debe manejar esta situación, informando de la
misma.
c) Cuando un auto sale, se registra su hora de salida.
d) No se debe ingresar un auto que esté actualmente en el estacionamiento. Se debe
informar en que sector esta.
e) El estacionamiento, en algún momento, deberá poder responder cuánto dinero
 se recaudó.
Ejemplo:
★ Ingresa el auto en el sector docente AAA111 a las 11 y sale a las 13
★ Ingresa el auto en el sector alumno BBB111 a las 12 y sale a las 15
★ Ingresa el auto en el sector general CCC111 a las 10 y sale a las 13
El total a recaudar es: 2*$10 + 3*$5 + 3*$20 

Se pide Modelar el TDA Estacionamiento, escribiendo la interfaz pública de todos los TDAs
involucrados. En la interfaz se deben indicar de manera prolija los atributos y las operaciones,
usando nombres declara?vos e incluyendo una breve explicación de cada una. Se puede entregar
un txt/pdf adicional al código con esta información.
Tener en cuenta que se debe poder:
I. Registrar el ingreso de un auto con los datos indicados previamente.
II. Consultar si un auto está en el estacionamiento, mediante su patente.
III. Registrar la salida de un auto con los datos indicados.
IV. Calcular el dinero recaudado.
Para lo anterior, se pide:
1. Escribir la interfaz pública de los TDAs involucrados (nombre, atributos y
operaciones principales de cada uno).
2. Implementar los métodos para poder responder las operaciones I...IV indicadas en el
enunciado.
3. Utilizar la función main proporcionada para las pruebas, que no debe ser modificada.

Función main
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
 
 
