##
## Imprima por cada fila, la columna 1 y la suma de los valores
## de la columna 5
##
## E,22
## A,14
## B,14
## ....
## C,8
## E,11
## E,16
##
data = open('data.csv','r').readlines()
data = [row.split('\t') for row in data]
data1 = [[row[0],row[4][:-1].split(',')] for row in data]

cont = 0
for i in data1:
    suma = 0
    for a in i[1]:
        suma = suma + int(a[-1])
    print(f'{i[0]},{suma}')
