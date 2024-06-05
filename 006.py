# make an algorithm that reads a number, shows it squared, cubed and its square root.
n = int(input('Please give me a number: '))
s = n**2
c = n**3
r = n**(1/2)
print('{} squared equals {}, cubed equals {}. And its square root equals {}.'.format(n, s, c, r))