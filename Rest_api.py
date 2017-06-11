
import requests
import json
from pprint import pprint as pp

#Zad_1
response = requests.get('https://swapi.co/api/planets')
#pp(response.json())

slownik = response.json()
a = slownik['results']

for i in a:
    if i['name'] == 'Alderaan':
        for j in i['residents']:
            response = requests.get(j)
            pp(response.json())

#Zad_1

response = requests.get('https://swapi.co/api/planets/1')
#pp(response.json())

slownik = response.json()

#pp(response.json())

if slownik['name'] == 'Tatooine':
    for i in slownik['residents']:
        response = requests.get(i)
        pp(response.json())


#Zad_2

response = requests.get('http://swapi.co/api/films/')
#pp(response.json())
slownik = response.json()
a = slownik['results']


classification_list = []

for i in a:
    if i['episode_id'] == 5:
        for j in i['species']:
            response = requests.get(j)
            species_dict = response.json()
            classification_list.append(species_dict['classification'])

pp(classification_list)

#Zad_3

response = requests.get('http://swapi.co/api/starships/')
#pp(response.json())

slownik = response.json()
a = slownik['results']

BMI_dict = {}

for i in a:
    if i['name'] == 'Millennium Falcon':
        for j in i['pilots']:
            response = requests.get(j)
            pilots_dict = response.json()
            BMI_dict['name'] = pilots_dict['name']
            BMI_dict['BMI'] = int(pilots_dict['height'])/int((pilots_dict['mass']))**2
            pp(BMI_dict)

#Zad_4

            
        


#Zad_1_1
'''response = requests.post('52.57.96.135/fnt', data=json.dumps({'imie':'Dominika'}))
print(response.status_code)'''


        
