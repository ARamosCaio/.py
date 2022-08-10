import random

random_number = random.randint(1,20)
user_number = 0


while (user_number != random_number):
	user_number = int(input('Insira seu chute! : '))
	if user_number == random_number+1 or user_number == random_number-1:
		print('That was SO CLOSE')
	elif user_number == random_number+2 or user_number == random_number-2:
		print('Almost got it')
	elif user_number == random_number+3 or user_number == random_number-3:
		print('Try again')
	elif user_number > random_number+4 or user_number < random_number-4:
		print('Ice cold')
print('NICE!! it was ' , random_number)
