def get_data():
    weight = float(input('Enter weight: '))
    height = float(input('Enter height: '))
    data = {'weight':weight, 'height':height}
    return data

def count_BMI(weight, height):
    bmi = weight/height**2
    print('BMI: %s'%(bmi))

data = get_data()

count_BMI(data['weight'],data['height'])
