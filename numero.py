
print("cuantos numeros quiere colocar?")
us=int(input())
s=0
r=0
for i in range(1, us+1):
    print("igrese un numero")
    s=int(input())
    r=r+s
print("su la suma todal es: ", r)