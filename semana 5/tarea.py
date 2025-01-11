#El programa nos da una lista de opciones de trasformacion
def conversion():
    print("Seleccione el tipo de conversion:")
    print("1. De cm a m")
    print("2. De mm a m")
    print("3. De m a Km")
    selecion= int(input("Seleccione una opcion: "))
    #Dependiendo de la opcio escogida se da paso
    if selecion == 1:
        #De centimetros a metros
        cm = int(input("Ingrese el valor a convertir: "))
        Trasfomracion = cm / 100
        print(f"{cm} centimetros es igual a {Trasfomracion} metros")

    elif selecion == 2:
        #De milimetros a metros
        mm = int(input("Ingrese el valor a convertir: "))
        Trasfomracion = mm / 1000
        print(f"{mm} milimetros es igual a {Trasfomracion} metros")

    elif selecion == 3:
        #De metros a Kilometros
        m = int(input("Ingrese el valor a convertir: "))
        Trasfomracion = m / 1000
        print(f"{m} metros es igual a {Trasfomracion} Kilometros")
    else:
        print("Opcion invalida")


conversion()