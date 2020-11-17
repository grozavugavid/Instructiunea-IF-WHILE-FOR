a=int(input("Introduceti un numar a:"))
b=int(input("Introduceti un numar b:"))
c=int(input("Introduceti un numar c:"))
a+=1
b+=1
c+=1
if (a<b+c) and (b<a+c) and (c<a+b):
    print("exista triunghi")
if (a==b!=c):
    print("triunghiul este isoscel")
if (a==b==c):
    print("triunghiul este echilateral")
if (a!=b!=c):
    print("triunghiul este scalen")