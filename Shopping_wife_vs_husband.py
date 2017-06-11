#Stwórz skrypt lista zakupów, który najpierw prosi o 5 rzeczy, po które żona
#wysyła męża, a potem o kolejne 5, które ten mąż kupił, a niekoniecznie
#znajdowały się na liście
wife_list = []
husband_list = []

for i in range(5):
    wife_list.append(input('Enter things, that wife tell to buy: '))
print(wife_list)

for i in range(5):
    husband_list.append(input('Enter things, that husband have bought: '))
print(husband_list)

list_differences_1 = []

for thing in wife_list:
    if thing in husband_list:
        list_differences_1.append(thing)

list_differences_2 = []

for thing in husband_list:
    if thing not in wife_list:
        list_differences_2.append(thing)

list_differences_3 = []

for thing in wife_list:
    if thing not in husband_list:
        list_differences_3.append(thing)

print('Husband bought things, that wife tell: ', list_differences_1)
print(
    'Husband bought extra things, that wife didn\'t tell: ',
    list_differences_2
    )
print('Husband didn\'t bought: ', list_differences_3)
