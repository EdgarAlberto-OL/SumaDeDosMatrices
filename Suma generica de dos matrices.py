from gettext import npgettext


import numpy as np

m=int(input("#Filas: "))
n=int(input("#Columnas: "))

print("Datos de la Primera Matriz")
A=[]

contm=0
contn=0

while contn<n:
 A=A+[list(np.zeros(n))]
 contn=contn+1



while contm<m:
 contn=0   
 while contn<n:
    print("a",contm+1,contn+1) 
    A[contm][contn]=float(input())   
    contn=contn+1
    

 contm=contm+1   

print("Datos de la Segunda Matriz")
B=[]
contm=0
contn=0

while contn<n:
 B=B+[list(np.zeros(n))]
 contn=contn+1



while contm<m:
 contn=0   
 while contn<n:
    print("b",contm+1,contn+1)  
    B[contm][contn]=float(input())   
    contn=contn+1
    

 contm=contm+1   


print("\n", "Matriz Suma")
print("\n",np.array(A)+np.array(B),"\n")
