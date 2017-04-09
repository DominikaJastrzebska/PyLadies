#Oblicz BMI wszystkich członków rodziny
#Stwórz program, który spyta o imię, wagę oraz wzrost każdego z
#członków rodziny i wypisze ich BMI.

from pprint import pprint as pp

family = []

enabled = True
while enabled:
    family_member = {}
    family_member['name'] = input('Enter your name: ')
    family_member['sex'] = str(input('Enter sex: m/w '))
    family_member['weight'] = float(input('Enter weight: '))
    family_member['height'] = float(input('Enter height: '))
    family_member['BMI'] = round(family_member['weight']/family_member['height']**2)

    if family_member['sex'] == 'w':
        if family_member['BMI'] <= 16.5:
            classification = 'anorexia'
        elif 16.5 < family_member['BMI'] <= 20:
            classification = 'underweight'
        elif 20 < family_member['BMI'] <= 25:
            classification = 'normal weight'
        elif 25 < family_member['BMI'] <= 30:
            classification = 'overweight'
        else:
            classification = 'obesity'
    elif family_member['sex'] == 'm':
        if family_member['BMI'] <= 18.5:
            classification = 'anorexia'
        elif 18.5 < family_member['BMI'] <= 22.5:
            classification = 'underweight'
        elif 22.5 < family_member['BMI'] <= 27.5:
            classification = 'normal weight'
        elif 27.5 < family_member['BMI'] <= 32.5:
            classification = 'overweight'
        else:
            classification = 'obesity'

    family_member['classification'] = classification

    family.append(family_member)

    question = input(
        'Do you want to calculate BMI for another family member? y/n '
        )
    
    if question == 'n':
        enabled = False

pp(family)

for family_member in family:
    print(family_member['name'],family_member['BMI'],family_member['classification'])

