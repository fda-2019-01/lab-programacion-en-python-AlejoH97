##
## Imprima la suma de la columna 2 por cada letra 
## de la columna 4, ordnados alfabeticamente.
##
## a,114
## b,40
## c,91
## d,65
## e,79
## f,110
## g,35
##

data = open('data.csv','r').readlines()
data = [row.split('\t') for row in data]
data1 = [[row[3].split(','),row[1]] for row in data]

count={}
for a,b in data1:
    for i in a:
        if(count.get(i) != None):
            count[i] = count[i] + int(b)
        else:
            count[i] = int(b)

for i in sorted(count.keys()):
    print(f'{i},{count[i]}')
