##
## Imprima el valor maximo y minimo por cada letra de la columa 1.
##
## A,9,1
## B,9,1
## C,9,0
## D,7,1
## E,9,1
##
data = open('data.csv','r').readlines()
data = [row.split('\t') for row in data]
data = [[row[0], row[1]] for row in data]

count = {}
for letter in data:
    let = letter[0]
    if(count.get(let) != None):
        if(int(count.get(let)[0]) < int(letter[1])):
            count[let][0] = letter[1]
        elif(int(count.get(let)[1]) > int(letter[1])):
            count[let][1] = letter[1]
    else:
        count[let] = [int(letter[1]),int(letter[1])]

for i in sorted(count.keys()):
    print(f'{i},{count[i][0]},{count[i][1]}')