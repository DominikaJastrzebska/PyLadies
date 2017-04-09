a = float(input('Enter the side a of the cuboid: '))
b = float(input('Enter the side b of the cuboid: '))
H = float(input('Enter the height H of the cuboid: '))
V = a*b*H

if a != b and a != H and b != H:
    classification = ''

if (a == b and a != H) or (a == H and b != H) or (b == H and a != H):
    classification = 'The base of cuboid is square.'
elif a == b and b == H and a == H:
    classification = 'Cuboid is a cube'

print('Volume of cuboid is: ', str(V), classification)
