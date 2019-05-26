##
## Imprima la suma de la segunda columna.
##
data = open('data.csv','r').readlines()
data = [row.split('\t') for row in data]
sum = 0
for i in data:
    sum = sum + int(i[1])
print(sum)