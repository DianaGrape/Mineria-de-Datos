import csv
import math

# es el mismo data set pero con KNN


f= open('dataset.csv') # abro el archivo 
lns=csv.reader(f) # guardo todo lo que contiene el archivo 

dataset=list(lns)# guardo los datos en un array
print("Bienvenido al programa de Clasificacion con knn ")
print("Este programa calcula la probabilidad de muerte si se opero de cancer de mama")
print ("Porfavor ingrese los datos solicitados ;) \n\n")
print("Edad: ",end="")
a=input()
print("año que se sometio a la operacion: ",end="")
b=input()
print("Número de ganglios axilares positivos detectados: ",end="")
c=input()
print("Numero de Vecinos a considerar: ",end="")
k=input()
k=int(k)
a=int(a)
b=int(b)
c=int(c)
Prediccion=[a,b,c] #34	59	0
aux=0
contador=0
contador1=0
contador2=0

# print(dataset[1][1])  [fila] y [columna]

Matrix=dataset
print(type(Matrix[0][0]))

for j in Matrix: # convierto todo mi data set a valores numericos 
    Matrix[contador][0]=int(Matrix[contador][0])
    Matrix[contador][1]=int(Matrix[contador][1])
    Matrix[contador][2]=int(Matrix[contador][2])
    Matrix[contador][3]=int(Matrix[contador][3])
    contador+=1


####    (pow((Matrix[contador][0]-Prediccion[0]),2))
   
contador=0

for i in Matrix:# realizo la distancia euclidiana
    aux=0
    aux=(pow((Matrix[contador][0]-Prediccion[0]),2))+ (pow((Matrix[contador][1]-Prediccion[1]),2))+ (pow((Matrix[contador][2]-Prediccion[2]),2))
    aux=math.sqrt(
    Matrix[contador].append(aux)
    contador+=1
    
print(Matrix[0][4])

Matrix.sort(key=lambda Matrix: Matrix[4])

print("Vecinos encontrados")
print("1=vivira mas de 5 años")
print("2=vivira menos de 5 años\n")
print(Matrix[0][3])

contador=0
for i in range (k-1):
    if Matrix[contador][3]==1:
        contador2+=1
    else:
        contador1+=1
        
    print(Matrix[contador][3])
    contador+=1
if contador2>contador1:
    print("el nuevo objeto pertenece a la clase 1, vivira mas de 5 años")
else:
       print("el nuevo objeto pertenece a la clase 2,  no vivira mas de 5 años :( ")








