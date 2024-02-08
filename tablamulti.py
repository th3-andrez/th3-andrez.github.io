print("tabla del:")
p=int(input())
print("al:")
t=int(input())
r=0
print("has elegido la tabal del: ",p)
for i in range(1, t+1):
    r=i*p
    print(p,"X",i,"=",r)