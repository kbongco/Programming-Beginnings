print('Welcome to the number guessing game!')
#insert limited amount of tries here
import random
num = random.randint(1,20)
while True:
    print('Guess a number Between 1 and 20!')
    guess = input()
    x = int(guess)
    if x == num:
        print('Congratulations! You guessed correctly!')
        break
    elif x < num:
        print('Thats too low! Try again!')
    elif x > num:
        print('Thats too high! Try again!')
 
        
