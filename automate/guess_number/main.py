import random

num = random.randint(1, 20)
tries = 0
while True and tries < 6:
    print(tries)
    try:
        guess = int(input('take a guess between number 1 to 20: '))
        if num == guess:
            print('you won you guess correctly ' + str(guess))
            break
        else:
            print('sorry please keep trying')
    except ValueError:
        print('please enter number 1 to 20 only')
    tries += 1
    print(tries)
