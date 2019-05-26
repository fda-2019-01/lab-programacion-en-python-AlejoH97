##
## Genere una lista de tuplas, donde cada tupla contiene en la primera 
## posicion, el valor de la segunda columna; la segunda parte de la 
## tupla es una lista con las letras (ordenadas) de la primera 
## columna que aparecen asociadas a dicho valor de la segunda 
## columna. Esto es:
##
## ('0', ['C'])
## ('1', ['A', 'A', 'B', 'D', 'E', 'E'])
## ('2', ['A', 'D', 'E'])
## ('3', ['A', 'B', 'D', 'E', 'E'])
## ('4', ['B', 'E'])
## ('5', ['B', 'C', 'D', 'D', 'E', 'E', 'E'])
## ('6', ['A', 'B', 'C', 'E'])
## ('7', ['A', 'C', 'D', 'E'])
## ('8', ['A', 'B', 'E', 'E'])
## ('9', ['A', 'B', 'C', 'E'])
##
##
data = open('data.csv','r').readlines()
data = [row.split('\t') for row in data]
data = [[row[0], row[1]] for row in data]

lista = []

for i in range(0,10):
    lista.append((str(i),[]))

for a,b in data:
    lista[int(b)][1].append(str(a))     

sortedList = []
for a,b in lista:
    sortedList.append((a,sorted(b)))

for i in sortedList:
    print(i)