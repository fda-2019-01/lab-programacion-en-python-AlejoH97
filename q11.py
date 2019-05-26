##
## Imprima una tabla en formato CSV que contenga por registro,
## la cantidad de elementos de las columnas 4 y 5
## (filas en el archivo)
##
## E,3,5
## A,3,4
## B,4,4
## ...
## C,4,3
## E,2,3
## E,3,3
##
data = open('data.csv','r').readlines()
data = [row.split('\t') for row in data]
data1 = [[row[3].count(',')+1,row[4].count(':')] for row in data]

cont = 0
for i in data:
    print(f'{i[0]},{data1[cont][0]},{data1[cont][1]}')
    cont = cont + 1

