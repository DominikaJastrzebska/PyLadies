def get_data():
    weight = input('Enter weight: ')
    height = input('Enter height: ')
    data = {'weight':weight, 'height':height}
    return data

def BMI(height, weight):
    BMI = weight/height**2
    print('BMI: '%f)%(bmi)

data = get_data()

BMI(data['weight'],data['height'])
