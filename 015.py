#write a program that asks the amount of km driven by a rental car and the amount of days it was rented for. calculate how much the person has to pay, knowing the rent is R$60/day and R$0,15/km.
d = float(input('How many days did you rent the car for? '))
km = float(input('How many km did you drive with it? '))
p = (60*d)+(km*0.15)
print('Total to pay is: R${:.2f}'.format(p))