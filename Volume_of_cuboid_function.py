def get_data():
    a = float(input('Type side a: '))
    b = float(input('Type side b: '))
    H = float(input('Type height H: '))
    data = {'a': a, 'b': b, 'H': H}  #return a, b, H
    return data

def count_volume(a, b, H):
    V = a * b * H
    print('Volume of cuboid is: ',V)


data = get_data()       #get_data()
count_volume(data['a'], data['b'], data['H'])   #count_volume(a, b, H)
