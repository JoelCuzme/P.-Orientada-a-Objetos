#Programacion Tradicional
def calculo_de_temperatura(dia1,dia2,dia3,dia4,dia5,dia6,dia7):
    total= [dia1,dia2,dia3,dia4,dia5,dia6,dia7]
    suma= 0
    for i in total:
        suma += i
    calculo= suma/len(total)
    print("El promedio semanal es de",calculo, "grados")

def pedir_datos():
    dia1= int(input('dia 1: '))
    dia2= int(input('dia 2: '))
    dia3= int(input('dia 3: '))
    dia4= int(input('dia 4: '))
    dia5= int(input('dia 5: '))
    dia6= int(input('dia 6: '))
    dia7= int(input('dia 7: '))
    return dia1,dia2,dia3,dia4,dia5,dia6,dia7

resultado = pedir_datos()
calculo_de_temperatura(resultado[0],resultado[1],resultado[2],resultado[3],resultado[4],resultado[5],resultado[6])

#