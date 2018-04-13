import random

guessesTaken = 0

print("Hello Vinayagar!, What is your name ? ")
myName = input()

#Vin_Inputno = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
number = random.randint(1,20)

print('Well,' + myName + ', I am thinking of a number between 1 and 20.')

for guessessToken in range(6):
    guessesTaken = guessesTaken + 1
    print('Take a guess.')
    guess = input()
    guess = int(guess)

    if guess < number:
        print ('Your guess is too low')
        #print(number)
        
    if guess > number:
        print('Your guess is too high')
        #print(number)
        
    if guess == number:
        break


if guess == number:
    guessesTaken = str(guessesTaken)
    print('Good job '+ myName + '| You guesses my number in ' +
          guessesTaken + ' guesses!')
    #print(guessesTaken)


if guess != number:
    number = str(number)
    print ('Nope. The number I was thinking of was ' + number + '.')

        
