# make an algorithm that reads the price of a product and shows its new price, with 5% off.
n = float(input('Price: '))
d = n*0.05
np = n-d
print('The new price is {}.'.format(np))