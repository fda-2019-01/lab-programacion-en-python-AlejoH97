##
## Imprima la cantidad de registros por letra para la 
## primera columna, ordenados alfabeticamente.
##
## A,8
## B,7
## C,5
## D,6
## E,14
##
data = open('data.csv','r').readlines()
data = [row.split('\t') for row in data]
data = [row[0] for row in data]

count = {}
for letter in data:
    if(count.get(letter) != None):
        count[letter] = count[letter] + 1
    else:
        count[letter] = 1

for i in sorted(count.keys()):
    print(f'{i},{count[i]}')