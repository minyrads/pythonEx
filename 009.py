# make a program that reads a number and shows on the screen its multiplication table.
n = int(input('Number: '))
for i in range(1, 11):
    print(n, 'x', i, '=', n*i)