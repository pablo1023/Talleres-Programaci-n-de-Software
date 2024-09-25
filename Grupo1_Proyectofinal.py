# importancion de bibliotecas de creacicion de codigos de reserva y precios de las reservas realizadas por el cliente
import random
#! Importancion de bibliotecas para el uso correcto de las fechas de reserva
import datetime

#! Permite que el valor ingresado por el cliente sea entero
def es_entero(valor):
    try:
        int(valor)
        return True
    except ValueError:
        return False
print(" ")
print("Bienvenidos a la agencia de viajes VIAJESITOS, donde encontraras todo sobre tus viajes internacionales")

#! Base de datos de la empresa guardados en tipo Diccionarios de clientes y paquetes turisticos
clientes = { "93780": {"Nombre":"Pedro","Edad":30,"ID":93308,"Vuelo":"Sudafrica","Aerolinea":"Iberia","Hotel":"Morochitos resort","Fecha de salida":"2024/10/02","Fecha de llegada":"2024/10/31", "Precio a pagar":1000},
            "93790" : {"Nombre":"Andres","Edad":27,"ID":93568,"Vuelo":"Tunez","Aerolinea":"Turkish Airlines","Hotel":"La catedral","Fecha de salida":"2024/10/15","Fecha de llegada":"2024/10/20", "Precio a pagar":2500},
            "93895" : {"Nombre":"Juanito","Edad":40,"ID":93784,"Vuelo":"Kirguistan","Aerolinea":"EVA air","Hotel":"Gengis resort","Fecha de salida":"2024/11/20","Fecha de llegada":"2024/12/03", "Precio a pagar":400},
            }

paquetes = { "1. Familiar": {"Adultos":2,"Niños":2,"Lugar de destino":"Riviera Maya","Aerolinea":"American Airlines","Hotel":"Xcaret","Cantidad dias y noches":"5 dias y 5noches","Alimentacion":"Todo incluido","Precio":4000},
            "2. Pareja": {"Adultos":2,"Lugar de destino":"Paris","Aerolinea":"Iberia","Hotel":"George-V","Cantidad dias y noches":"5 dias y 5noches","Alimentacion":"Todo incluido","Precio":3000},
            "3. Luna de miel": {"Adultos":2,"Lugar de destino":"Dinamarca","Aerolinea":"Scandinavian","Hotel":"Clarion Hotel","Cantidad dias y noches":"5 dias y 5noches","Alimentacion":"Todo incluido","Precio":3500}
            }

#! Esta parte es el menu de opciones que se le muestra al usurio para que ejecute lo que desea comprar
def menu():
    print("\n**** Menu de Opciones ****")
    print("1. Realizar reserva")
    print("2. Comprar paquete de la agencia")
    print("3. Cambiar datos del cliente o fechas del viaje")
    print("4. Anular reserva")
    print("5. Lista de todos los clientes")
    print("6. Salir del sitio web")
    print("\n ************************************")

#! Esla parte del codigo donde el cliente crea el paquete a gusto de el
def agregarCliente():
    numReserva = random.randint(10000,50000)
    numReserva1 = str(numReserva)
    print(f"Numero de reserva: {numReserva1}")
    if numReserva1 in clientes:
            print("La reserva ya tiene un comprador")
    else:
        while True:
            try:
                id = int(input("Por favor ingrese la identificacion del cliente: "))
                break
            except ValueError:
                print("Por favor ingrese un numero de identificacion valido")
                print()
        while True:
            nombre = input("Por favor ingrese el nombre del cliente: ").strip().capitalize()
            if nombre.isdigit() or nombre == "":
                nombre = str(input("Por favor digite su nombre: ")).strip().capitalize()
            while True:
                try:
                    edad = int(input("Por favor ingrese la edad del cliente: "))
                    break
                except ValueError:
                    print("Por favor puede ingresar la edad del cliente valida")
                    print()
            vuelo = input("Por favor ingrese el lugar de destino a donde desea viajar: ").strip().capitalize()
            if vuelo.isdigit() or vuelo == "":
                vuelo = str(input("Por favor digite a donde quiere viajar: "))
            aerolinea = input("Por favor ingrese su aerolinea de preferencia: ").strip().capitalize()
            if aerolinea.isdigit() or aerolinea == "":
                aerolinea = str(input("Por favor digite la aerolinea donde desea viajar: "))
            hotel = input("Por favor ingrese el hotel donde desea hospedarse: ").strip().capitalize()
            if hotel.isdigit() or hotel == "":
                hotel = str(input("Por favor digite el hotel donde se va a hospedar: "))
            while True:
                try:
                    fechaSalida = input("Por favor ingrese su fecha de salida (AÑO/MES/DIA): ")
                    fechaSalida = datetime.datetime.strptime(fechaSalida, '%Y/%m/%d')
                    break
                except ValueError:
                    print("POR FAVOR DEBE DIGITAR UNA FECHA VALIDA CON EL FORMATO AÑ0/MES/DIA")
                    print()
            while True:
                try:
                    fechaLlegada = input("Por favor ingrese su fecha de regreso (AÑO/MES/DIA): ")
                    fechaLlegada = datetime.datetime.strptime(fechaLlegada, '%Y/%m/%d')
                    break
                except ValueError:
                    print("POR FAVOR DEBE DIGITAR UNA FECHA VALIDA CON EL FORMATO AÑ0/MES/DIA")
                    print()
            precio = random.randint(300,4000)
            clientes[numReserva1]={"Nombre":nombre,"Edad":edad,"ID":id,"Vuelo":vuelo,"Aerolinea":aerolinea,"Hotel":hotel,"Fecha de salida":fechaSalida,"Fecha de llegada":fechaLlegada, "Precio a pagar":precio}
            print(f"El cliente {nombre} con numero de ID. {id} realizo su reserva exitosamente")
            break

#! Es la parte del codigo donde el cliente compra el paquete que afrece la agencia de viajes
def comprarPaquete():
    print()
    print("CARACTERISTICAS DE LOS PAQUETES")
    print()
    print("1. PAQUETE FAMILIAR:")
    for clave, valor in paquetes["1. Familiar"].items():
        print(" "f" {clave}: {valor}")
    print("2. PAQUETE PAREJAS:")
    for clave, valor in paquetes["2. Pareja"].items():
        print(" "f" {clave}: {valor}")
    print("3. PAQUETE LUNA DE MIEL:")
    for clave, valor in paquetes["3. Luna de miel"].items():
        print(" "f" {clave}: {valor}")
    print()
    numReserva = random.randint(10000,50000)
    numReserva1 = str(numReserva)
    print(f"Numero de reserva: {numReserva1}")
    if numReserva1 in clientes:
        print("La reserva ya tiene un comprador")
    else:
        while True:
            try:
                id = int(input("Por favor ingrese la identificacion del cliente: "))
                break
            except ValueError:
                print("Por favor ingrese un numero de identificacion valido")
                print()
        while True:
            nombre = input("Por favor ingrese el nombre del cliente: ").strip().capitalize()
            if nombre.isdigit() or nombre == "":
                nombre = str(input("Por favor digite su nombre: ")).strip().capitalize()
            while True:
                try:
                    edad = int(input("Por favor ingrese la edad del cliente: "))
                    break
                except ValueError:
                    print("Por favor puede ingresar la edad del cliente valida")
                    print()
            while True:
                try:
                    fechaSalida = input("Por favor ingrese su fecha de salida (AÑO/MES/DIA): ")
                    fechaSalida = datetime.datetime.strptime(fechaSalida, '%Y/%m/%d')
                    break
                except ValueError:
                    print("POR FAVOR DEBE DIGITAR UNA FECHA VALIDA CON EL FORMATO AÑ0/MES/DIA")
                    print()
            while True:
                try:
                    fechaLlegada = input("Por favor ingrese su fecha de regreso (AÑO/MES/DIA): ")
                    fechaLlegada = datetime.datetime.strptime(fechaLlegada, '%Y/%m/%d')
                    break
                except ValueError:
                    print("POR FAVOR DEBE DIGITAR UNA FECHA VALIDA CON EL FORMATO AÑ0/MES/DIA")
                    print()
            compraPaquete = input(f"Digite el nombre del paquete a comprar: ").capitalize()
            if compraPaquete == '1' or compraPaquete == 'Familiar':
                paquete = "Paquete Familiar"
                clientes[numReserva1] = {"Nombre":nombre,"Edad":edad,"ID":id,"Vuelo":"Rivera Maya","Aerolinea":"American Airlines","Hotel":"Xcaret","Fecha de salida":fechaSalida,"Fecha de llegada":fechaLlegada, "Precio a pagar":4000}
            elif compraPaquete == '2' or compraPaquete == 'Parejas':
                paquete = "Paquete Parejas"
                clientes[numReserva1] = {"Nombre":nombre,"Edad":edad,"ID":id,"Vuelo":"Paris","Aerolinea":"Iberia","Hotel":"George-V","Fecha de salida":fechaSalida,"Fecha de llegada":fechaLlegada, "Precio a pagar":3000}
            elif compraPaquete == '3' or compraPaquete == 'Luna de miel':
                paquete = "Paquete luna de miel"
                clientes[numReserva1] = {"Nombre":nombre,"Edad":edad,"ID":id,"Vuelo":"Dinamarca","Aerolinea":"Scandinavian","Hotel":"Clarion Hotel","Fecha de salida":fechaSalida,"Fecha de llegada":fechaLlegada, "Precio a pagar":3500}
            print(f"El cliente {nombre} con numero de ID. {id} realizo su reserva exitosamente")
            break

#! Es la parte del codigo donde permite editar datos personales de las reservas y fechas de salida y llegada de los viajes
def editarDatos():
    numReserva1 = input("Por favor ingrese el numero de reserva del cliente: ")
    if numReserva1 not in clientes:
        print("El cliente no tiene una reserva registrada en la base de datos")
    else:
        id = int(input("Por favor digite el numero de identidad del cliente: "))
        while True:
            try:
                respuesta = input("¿Desea modificar el nombre del cliente? (Si - No): ").strip().capitalize()
                if respuesta == "Si":
                    nombre = input("Por favor digite el nuevo nombre del cliente: ").strip().capitalize()
                    clientes[numReserva1]["Nombre"] = nombre
                    print(f"El nombre del cliente con numero de ID. {id} se actualizo correctamente")
            except ValueError:
                nombre = str(input("Por favor digite su nombre: ")).strip().capitalize()
            break
        while True:
            try:
                respuesta = input("¿Desea modificar la edad del cliente? (Si - No): ").strip().capitalize()
                if respuesta == "Si":
                    edad = input("Por favor digite la nueva edad del cliente: ").strip().capitalize()
                    clientes[numReserva1]["Edad"] = edad
                    print(f"La edad del cliente {clientes[numReserva1]['Nombre']} con numero de ID. {id} se actualizo correctamente")
            except ValueError:
                edad = int(input("Por favor ingrese la edad del cliente: "))
            break
        while True:
            try:
                respuesta = input("¿Desea modificar las fechas del viaje del cliente? (Si - No): ").strip().capitalize()
                if respuesta == "Si":
                    fechaSalida = input("Por favor ingrese su fecha de salida (AÑO/MES/DIA): ")
                    fechaSalida = datetime.datetime.strptime(fechaSalida, '%Y/%m/%d')
                    fechaLlegada = input("Por favor ingrese su fecha de regreso (AÑO/MES/DIA): ")
                    fechaLlegada = datetime.datetime.strptime(fechaLlegada, '%Y/%m/%d')
                    clientes[numReserva1]["Fecha de salida"] = fechaSalida
                    clientes[numReserva1]["Fecha de llegada"] = fechaLlegada
                    print(f"Las fechas del viaje del cliente {clientes[numReserva1]['Nombre']} con numero de ID. {id} se actualizo correctamente")
            except ValueError:
                fechaSalida = input("Por favor ingrese su fecha de salida (AÑO/MES/DIA): ")
                fechaSalida = datetime.datetime.strptime(fechaSalida, '%Y/%m/%d')
                fechaLlegada = input("Por favor ingrese su fecha de regreso (AÑO/MES/DIA): ")
                fechaLlegada = datetime.datetime.strptime(fechaLlegada, '%Y/%m/%d')
            print()
            print("LOS CAMBIOS HAN SIDO GUARDADOS EXITOSAMENTE")
            break

#! Es la parte del codigo donde el cliente o la agencia puede anular su reserva de viaje
def eliminarReserva():
    numReserva = input("Por favor ingrese el numero de reserva que desea anular: ")
    if numReserva in clientes:
        del clientes[numReserva]
        print(f"La reserva del cliente ha sido anulada exitosamente")
        print()
        print("ESTA ES LA LISTA ACTULIZADA DE LOS CLIENTES DE LA AGENCIA")
        for clave,valor in clientes.items():
            print()
            print(f"Informacion del cliente:\n  No. Reserva: {clave}\n  Nombre: {valor['Nombre']}\n  ID: {valor['ID']}\n  Edad: {valor['Edad']}\n  Vuelo: {valor['Vuelo']}\n  Aerolinea: {valor['Aerolinea']}\n  Hotel: {valor['Hotel']}\n  Fecha de Salida: {valor['Fecha de salida']}\n  Fecha de llegada: {valor['Fecha de llegada']}\n  Precio a pagar: ${valor['Precio a pagar']} USD")

#! Es la parte del codigo donde la agencia puede ver el listado de reservas y datos especificos de estas
def listaClientes():
    if clientes:
        print()
        print("Informacion de las reservas de los clientes")
        print()
        for clave, valor in clientes.items():
            print()
            print(f"Informacion del cliente:\n  No. Reserva: {clave}\n  Nombre: {valor['Nombre']}\n  ID: {valor['ID']}\n  Edad: {valor['Edad']}\n  Vuelo: {valor['Vuelo']}\n  Aerolinea: {valor['Aerolinea']}\n  Hotel: {valor['Hotel']}\n  Fecha de Salida: {valor['Fecha de salida']}\n  Fecha de llegada: {valor['Fecha de llegada']}\n  Precio a pagar: ${valor['Precio a pagar']} USD")

#! Es la parte del codigo de interfas de interacion de la pagina de la agencia
while True:
    menu()
    opcion = input("Seleccione una opcion y coloque el numero de esta: ")
    if opcion == "1":
        agregarCliente()
    elif opcion == "2":
        comprarPaquete()
    elif opcion == "3":
        editarDatos()
    elif opcion == "4":
        eliminarReserva()
    elif opcion == "5":
        listaClientes()
    elif opcion == "6":
        print("Saliendo....")
        break
    else:
        print("Opcion no valida, seleccione una opcion del menu")