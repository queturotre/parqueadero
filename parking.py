#Funciones
#validarDisponibilidad(tipoAuto)->True o False
def validarDisponibilidad(tipoAuto):
  archivo = open('parqueadero.txt','r')
  libres = []
  for espacios in archivo:
    ocupado=espacios.split(',')
    if espacios.startswith(tipoAuto[0].upper()) and len(ocupado)==1:
      libres.append(espacios)
  return len(libres)>0

#print(validarDisponibilidad('auto'))

#asignePosicion(tipoAuto) -> retorna cadena
import random as rd
def asignePosicion(tipoAuto):
  archivo = open('parqueadero.txt','r')
  libres = []
  for espacios in archivo:
    ocupado=espacios.strip().split(',')
    if espacios.startswith(tipoAuto[0].upper()) and len(ocupado)==1:
      libres.append(espacios)
  return rd.choice(libres)

#print(asignePosicion('auto'))
#actualizaDisponibilidad(espacio,placa) -> actualiza el archivo
def actualizaDisponibilidad(espacio,placa):
  archivo = open('parqueadero.txt','r+')
  espacios = []
  for linea in archivo:
    datos=linea.strip().split(',')
    if datos[-1]==espacio:
      linea=espacio+','+placa+'\n'
    espacios.append(linea)
  archivo.seek(0)
  archivo.writelines(espacios)
  archivo.close()

#print(actualizaDisponibilidad('M5','MSSM02020'))

def registrarAutomovil(placa, horaIngreso, horaSalida, puestoAsignado, nroTicket):
  archivo = open('registros.txt','r+')
  registrosActuales = []
  linea = f'{placa},{horaIngreso},{horaSalida},{puestoAsignado},{nroTicket}\n'
  msj="Entrada"
  for registro in archivo:
    if placa in registro and puestoAsignado in registro:
      datos = registro.split(',')
      linea = f'{placa},{datos[1]},{horaSalida},{puestoAsignado},{datos[-1]}'
      msj = "Salida"
    else:
      registrosActuales.append(registro)
  registrosActuales.append(linea)
  archivo.seek(0)
  for linea in registrosActuales:
    archivo.write(linea)
  archivo.close()
  print(msj+' registrada')

def consultarParqueadero(log):
  print('\nDatos Registrados:')
  archivo = open(log,'r')
  for espacios in archivo:
    print(espacios,end='')
  print()
  archivo.close()

def consultarLugarParqueo(placa):
  archivo = open('parqueadero.txt', 'r')
  respuesta = "No"
  for espacios in archivo:
    ocupado =espacios.strip().split(',')
    if placa in ocupado:
      respuesta = ocupado[0]
  archivo.close()
  return respuesta

def creaParqueadero(carros,motos):
  archivo = open('parqueadero.txt', 'w')
  for i in range(1,carros+1):
    archivo.write('A' + str(i)+"\n")
  for i in range(1, motos+1):
    archivo.write('M' + str(i)+"\n")
  archivo.close()