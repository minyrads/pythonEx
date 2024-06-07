# make a program that reads the height and width of a wall, calculate its area and how much paint will be needed to paint that wall, knowing that each liter of paint paints an area of 2m^2
w = float(input('Width: '))
h = float(input('Height: '))
a = w*h
p = a/2
print('The amount of liters of paint you will need to paint this wall is {}.'.format(p))
