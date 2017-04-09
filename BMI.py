#Napisz skrypt, który policzy BMI i w zależności od płci zgodnie z tabelką
#wypisze diagnozę:
#   women                   men
#   BMI     diagnosis       BMI         diagnosis
#   <=16.5  anorexia        <=18.5      anorexia
#   16.5-20 underweight     18.5-22.5   underweight
#   20-25   normal weight   22.5-27.5   normal weight
#   25-30   overweight      27.5-32.5   overweight
#   30+     obesity         32.5+       obesity


s = str(input('Enter sex: m/w '))
w = float(input('Enter weight: '))
h = float(input('Enter height: '))
BMI = w/h**2

if s == 'w':
    if BMI <= 16.5:
        classification = 'anorexia'
    elif 16.5 < BMI <= 20:
        classification = 'underweight'
    elif 20 < BMI <= 25:
        classification = 'normal weight'
    elif 25 < BMI <= 30:
        classification = 'overweight'
    else:
        classification = 'obesity'
elif s == 'm':
    if BMI <= 18.5:
        classification = 'anorexia'
    elif 18.5 < BMI <= 22.5:
        classification = 'underweight'
    elif 22.5 < BMI <= 27.5:
        classification = 'normal weight'
    elif 27.5 < BMI <= 32.5:
        classification = 'overweight'
    else:
        classification = 'obesity'

print(str(round(BMI, 2)), classification)
    
