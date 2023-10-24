"""
Para servicio de parqueo de automóviles con cierta capacidad de autos, para el registro
1. Con el número de la placa del auto
2. la hora de ingreso
3. tipo vehiculo (carro, moto)
4. ticket generado (nros del 1 al 10000)
5. puesto asignado (aleatorio vacio)

imprimir un ticket numerado y una asignacion de donde debe ubicarse. Cabe destacar que existen 40 espacios para carros y 10 para motos, esto lo puede actualizar en el archivo parqueadero.txt. En caso de llenarse debe presentar un mensaje de que no existe espacio para tal vehiculo.

Registre todos los vehiculos en el archivo registros.txt que si ingresaron al parqueadero en el formato: PLACA, HoraIngreso, HoraSalida, PuestoAsignado, NroTicket.

Con el siguiente menú:
1. Ingreso de automovil
2. Retiro de automovil
3. Revisión de estado del parqueadero
4. Revision de Registros
5. Salir
"""
import datetime
import random
import parking #funciones que se crearon la clase anterior

parking.creaParqueadero(30,5) #Si se desea borrar todo

print("Bienvenido a su parqueadero")
print("""Opciones: 
1. Ingreso de automovil
2. Retiro de automovil
3. Revisión de estado del parqueadero
4. Revision de Registros
5. Salir""")
opcion=0
while opcion !=5:
    opcion = input("Seleccione opción: ")
    if opcion.isdigit():
        opcion=int(opcion)
        if opcion not in range(1,6):
            print("Opción incorrecta")
        elif opcion==1:
            tipo = input("Ingrese tipo Auto/Moto: ")
            if parking.validarDisponibilidad(tipo):
                placa = input("Ingrese nro placa: ")
                ingreso = input("Ingrese hora de ingreso: ")
                print(datetime.date)
                ticket = str(random.randint(1,10000))
                print('Nro Ticket:',ticket)
                puesto = parking.asignePosicion(tipo).strip()
                print('Asignación', puesto)
                parking.actualizaDisponibilidad(puesto,placa)
                parking.registrarAutomovil(placa,ingreso,"",puesto,ticket)
            else:
                print("Actualmente no existe parqueo disponible")
        elif opcion==2:
            placa = input("Ingrese nro placa: ")
            puesto = parking.consultarLugarParqueo(placa)
            if puesto!="No":
                salida = input("Ingrese hora de salida: ")
                parking.actualizaDisponibilidad(puesto, '')
                parking.registrarAutomovil(placa,'',salida,puesto,'')
            else:
                print(f"El vehiculo con placa:{placa} no está dentro del parqueadero")
        elif opcion == 3:
            parking.consultarParqueadero('registros.txt')
        elif opcion==4:
            parking.consultarParqueadero('parqueadero.txt')
        elif opcion==5:
            print("Saliendo del sistema")
    else:
        print("El valor ingresado no es un digito")
print("Gracias por usar nuestro servicio")

