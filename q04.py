##
## Imprima la cantidad de registros por cada mes.
##
## 01,3
## 02,4
## 03,2
## 04,4
## 05,3
## 06,3
## 07,5
## 08,6
## 09,3
## 10,2
## 11,2
## 12,3
##
data = open('data.csv','r').readlines()
data = [row.split('\t') for row in data]
data = [row[2] for row in data]
data = [row.split('-') for row in data]
data = [row[1] for row in data]

count = {}
for letter in data:
    if(count.get(letter) != None):
        count[letter] = count[letter] + 1
    else:
        count[letter] = 1

for i in sorted(count.keys()):
    print(f'{i},{count[i]}')