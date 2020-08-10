import random
print("Hello..! what's your name..?")
name = input()
print('well,'+name+ ' I am thinking of a number between range of 1 to 20..')
secret_number = random.randint(1,20)
for i in range(1,6):
    print('Take a Guess:')
    guess = int(input())
    if guess > secret_number:
        print('Sorry..! your guess is too high ' +name+'.')
    elif guess < secret_number:
        print('Sorry..! your guess is too low '+name+'.')
    else:
        break
if guess == secret_number:
    print('Good job, '+name+'! you guessed my number in '+str(i)+'guesses.')
else:
    print('Nope, you exceeded guess times. My number is '+str(secret_number)+'.')
