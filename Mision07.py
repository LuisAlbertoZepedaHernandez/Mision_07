#Autor: Luis Alberto Zepeda Hernandez
#Misión 07_Ciclos While



def dividir(dividendo,divisor):
    cociente = 0
    dividendoSave = dividendo
    while dividendo >= divisor:
        cociente += 1
        dividendo = dividendo-divisor

    print(dividendoSave,"/",divisor,"=",cociente,", sobra",dividendo)


def encontrarMayor():
    print("Teclea una serie de números para encotrar el mayor")
    numero = int(input("Teclea un número [-1 para salir]: "))
    numeroMayor = numero
    while numero != -1:
        numero = int(input("Teclea un número [-1 para salir]: "))
        if  numero > numeroMayor:
            numeroMayor = numero
    if  numeroMayor == -1:
        print("No hay valor.")
    else:
        print("El mayor es:",numeroMayor)

def main():
    print("Misión 07. Ciclos While")
    print("Autor: Luis Alberto Zepeda Hernández.")
    print("Matrícula: A01328616")
    print("1.Calcular Divisiones")
    print("2.Encontrar el mayor ")
    print("3.Salir")
    opcion = int(input("Teclea tu opción: "))


    while opcion != 3:
        if opcion == 1:
            dividendo = int(input("Ingresa dividendo: "))
            divisor = int(input("Ingresa divisor: "))
            dividir(dividendo, divisor)
        elif opcion == 2:
            encontrarMayor()
        else:
            print("Error, teclea 1, 2 o 3")
        print()
        print("Misión 07. Ciclos While")
        print("Autor: Luis Alberto Zepeda Hernández.")
        print("Matrícula: A01328616")
        print("1.Calcular Divisiones")
        print("2.Encontrar el mayor ")
        print("3.Salir")
        opcion = int(input("Teclea tu opción: "))

    if opcion == 3:
        print('Gracias por usar este programa, regresa pronto.')









main()