import random

x1=int(input("adivine el numero del 1 al: "))
ra=random.randint(1,x1)
cont=0 
x2=int(input("coloque un numero de intentos: "))

for x in range (1,x2):
    
    cont+=1
    nu=int (input("coloque un numero: "))
    print("inento N#: ",cont)
    
    if(nu==ra):
        print("acertaste el numero")
        break
    else:
        print("no acertaste el numero")


#Ronny Rodriguez