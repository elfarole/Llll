
# conditions
number = float(input('Number: '))

if number > 0: #em pyhton o escopo é definido pela estrutura aninhada, sem {}
    print('The number is positive')
elif number < 0: #elif é o mesmo que else if
    print('The number is negative')    

else:
    print('The number is zero')    

#defing list and atributs

names = ['Harry','Ronne','Hermy','Gynny','Severus']

names.append('Draco')
names.sort()#      Para ordenar em ordem crescente ou alfabética
print(names[4])

#set is another way to set multiple data like list and tuple

name1 = set()

name1.add(1)
name1.add(2)
name1.add(3)
name1.add(4)

print(name1)

#To test loop in python 

for i in ['Ana','Harry','Paul','Thor','Jason']:
    print(i)

for u in range(4,9):#To count a row in sequence of numbers
    print(u)

names2 = ['Ana','Harry','Paul','Thor','Jason']
for name in names2:
    print(name)

names2 = 'Pablo'
for charactere in names2:
    print(charactere)

#Dictionary

houses = {
    'Harry': Gryffindor,
    'Draco': Slytherin
}        
print(houses['Harry'])

house = {
    'Harry': 'Gryffindor',
    'Draco': 'Slytherin'
}        

house['Severo'] = 'Professor' #It is the way to put new element on dictionary

print(house[input()])#With input we can set any element of dictionary

# We can import functions from another py file
from <name of file.py> import <name of functions># Does it works for any especific name into another file.py
        #or
import <names of file.py>        
    print(f'The square of {u} is {<name of file.py>.square(u)}')# it is just another way to import functions from another file
    