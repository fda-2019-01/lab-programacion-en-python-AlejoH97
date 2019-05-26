##
## Por cada clave de la columna 5 (cadena de tres letras), obtenga
## el valor mas pequeño y el valor mas grande asociado a esa clave.
##
## aaa,0,6
## bbb,4,7
## ccc,0,1
## ddd,5,5
## eee,0,0
## fff,4,9
## ggg,3,3
## hhh,6,8
## iii,2,7
## jjj,2,5
##
data = open('data.csv','r').readlines()
data = [row.split('\t') for row in data]
data2 = [row[1] for row in data]
data = [row[4][:-1] for row in data]
data = [row.split(',') for row in data]

"""count = {}
cont = 0
for i in data:
    for j in i:
        a,b = j.split(':')
        b = data2[cont]
        if(count.get(a) != None):
            if(int(count.get(a)[0]) > int(b)):
                count[a][0] = int(b)
            elif(int(count.get(a)[1]) < int(b)):
                count[a][1] = int(b)
        else:
            count[a] = [int(b),int(b)]
    print(count)
    cont = cont + 1
    
for i in sorted(count.keys()):
    print(f'{i},{count[i][0]},{count[i][1]}')"""


