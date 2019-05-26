##
## Imprima una tabla en formato CSV que contenga por cada clave 
## de la columna 5, la correspondiente cantidad de registros 
## asociados (filas en el archivo)
##
## aaa,13
## bbb,16
## ccc,23
## ddd,23
## eee,15
## fff,20
## ggg,13
## hhh,16
## iii,18
## jjj,18
##
##
data = open('data.csv','r').readlines()
data = [row.split('\t') for row in data]
data = [row[4][:-1] for row in data]
data = [row.split(',') for row in data]
lista = [i[:-2] for key in data for i in key ]

count={}
for i in lista:
    if(count.get(i) != None):
        count[i] = count[i] + 1
    else:
        count[i] = 1

for i in sorted(count.keys()):
    print(f'{i},{count[i]}')