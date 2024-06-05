# make a program that takes in how much money in reais someone has on their wallet, and show how many dollars they can buy. consider: USD$1.00 = BR$3.27
r = float(input('How many reais do you have? '))
d = r/3.27
print('The amount of dollars you can be is equal to {:.2f}.'.format(d))