#Napisz skrypt, który po policzeniu BMI spyta się czy policzyć
#dla kolejnej osoby

enabled = True
while enabled:

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


    question = input('Do you want to quit? y/n ')
    
    if question == 'y':
        enabled = False

        

    
