#Zadanie: napisz skrypt, który stworzy listę składającą się z trzech list,
#w każdej znajdzie się imię i wiek osoby. Następnie wyświetl listę składającą
#się tylko z imion, tylko z wieku oraz każdą osobę osobno

persons = [[], [], []]
for i in range(3):
    persons[i].append(input('Enter name: '))
    persons[i].append(input('Enter age: '))

for i in range(3):
    print(persons[i][0])

for i in range(3):
    print(persons[i][1])

for i in range(3):
    print(persons[i])


