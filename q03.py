##
## Imprima la suma de la columna 2 por cada letra de la 
## primera columna, ordneados alfabeticamente.
##
## A,37
## B,36
## C,27
## D,23
## E,67
##
data = open('data.csv','r').readlines()
data = [row.split('\t') for row in data]
data = [[row[0], row[1]] for row in data]

count = {}
for letter in data:
    let = letter[0]
    if(count.get(let) != None):
        count[let] = int(count[let]) + int(letter[1])
    else:
        count[let] = int(letter[1])

for i in sorted(count.keys()):
    print(f'{i},{count[i]}')