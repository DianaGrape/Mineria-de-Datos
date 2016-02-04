import csv
f= open('dataset.csv') # abro el archivo 
lns=csv.reader(f) # guardo todo lo que contiene el archivo 

dataset=list(lns)# guardo los datos en un array

edad="41" # hay que tipear la variable porque en mi arreglo entra como cadena
print("Bienvenido al programa de naive Bayes")
print("Este programa calcula la probabilidad de muerte si se opero de cancer de mama")
print ("Porfavor ingrese los datos solicitados ;) \n\n")
print("Edad: ",end="")
a=input()
print("año que se sometio a la operacion: ",end="")
b=input()
print("Número de ganglios axilares positivos detectados: ",end="")
c=input()
#####     30 64 1

ValoresSi=[0,0,0,0]
ValoresNo=[0,0,0,0]
a=int(a)
b=int(b)
c=int(c)
ValoresPrediccion=[a,b,c]
resultados=[0,0,0]#si,no y suma de si con no
Probabilidad=[0,0]#si, no
contador=0

# print(dataset[1][1])  [fila] y [columna]

###################### Obtencion de los valores de Si y de No
for j in dataset: # convierto todo mi data set a valores numericos 
    dataset[contador][0]=int(dataset[contador][0])
    dataset[contador][1]=int(dataset[contador][1])
    dataset[contador][2]=int(dataset[contador][2])
    dataset[contador][3]=int(dataset[contador][3])
    contador+=1
contador=0

for i in dataset:
 
    if dataset[contador][3]==1:
        ValoresSi[3]+=1       
    else:
        ValoresNo[3]+=1
        
    if dataset[contador][3]==1 and dataset[contador][0]==ValoresPrediccion[0]:
        ValoresSi[0]+=1
        
    if dataset[contador][3]==2 and dataset[contador][0]==ValoresPrediccion[0]:
        ValoresNo[0]+=1
        
    if dataset[contador][3]==1 and dataset[contador][1]==ValoresPrediccion[1]:
        ValoresSi[1]+=1
        
    if dataset[contador][3]==2 and dataset[contador][1]==ValoresPrediccion[1]:
        ValoresNo[1]+=1
        
    if dataset[contador][3]==1 and dataset[contador][2]==ValoresPrediccion[2]:
        ValoresSi[2]+=1
        
    if dataset[contador][3]==2 and dataset[contador][2]==ValoresPrediccion[2]:
        ValoresNo[2]+=1
    
    contador+=1   
#################
#fin del for

resultados[0]=(ValoresSi[0]/ValoresSi[3])*(ValoresSi[1]/ValoresSi[3])*(ValoresSi[2]/ValoresSi[3])*(ValoresSi[3]/contador)        

resultados[1]=(ValoresNo[0]/ValoresNo[3])*(ValoresNo[1]/ValoresNo[3])*(ValoresNo[2]/ValoresNo[3])*(ValoresNo[3]/contador) 

resultados[2]=resultados[0]+resultados[1]

Probabilidad[0]=100*(resultados[0]/resultados[2])
Probabilidad[1]=100*(resultados[1]/resultados[2])

print(contador)
print(ValoresSi)
print(ValoresNo)
print (resultados)
print(Probabilidad)

print ("la probabilidad de sobrevivir mas de 5 años es de: "+str(Probabilidad[0])+"%")
print ("la probabilidad de  no sobrevivir mas de 5 años es de: "+str(Probabilidad[1])+"%")
