# write a program that reads a value in meters and convert it into centimetres and millimetres.
n = float(input('Give me a number in meters: '))
c = n*100
ml = n*1000
print('The number you gave me was {}, and its same number in centimetres is {}, and in millimetres {}.'.format(n, c, ml))