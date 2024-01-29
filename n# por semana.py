print("ingrese un numero: ")
n=int(input())
match n:
    case 1: print("el numero escrito es: ",n," que es Lunes")
    case 2: print("el numero escrito es: ",n," que es Martes")
    case 3: print("el numero escrito es: ",n," que es Miercoles")
    case 4: print("el numero escrito es: ",n," que es Jueves")
    case 5: print("el numero escrito es: ",n," que es Viernes")
    case 6: print("el numero escrito es: ",n," que es Sabado")
    case 7: print("el numero escrito es: ",n," que es Domingo")
    case _: print("no hay dia existente para el nuemo ",n)

