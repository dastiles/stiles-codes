import random as r

choices = ['charles', 'hacker', 'bitches']
wordb = ''
word = r.choice(choices)
print(word)
wordarray = []
dashed = []
correct = []
wrong = []
# for i in word:
#     wordarray.append(i)
#     dashed.append('__')
tries = 0
cut = True


def buildWord():
    for i in word:
        wordarray.append(i)
        dashed.append('__')


def gameOver(c, w):
    if len(c) == len(w):
        print('You are  a WINNER!')
        re = input('If you wantto play again press Y or any to Quit: ')
        if re.lower() == 'y':
            return 'start'

        else:
            return 'stop'
    return 0


buildWord()
while cut:

   
    print(gameOver(correct, wordarray))
    if tries == 3:
        break
    for i in dashed:
        wordb += i
        wordb += ' '
    print('\n')
    print(wordb)

    letter = input('please enter a letter: \n')
    if correct.count(letter) == 0 and wrong.count(letter) == 0:
        for i in range(len(wordarray)):
            if wordarray[i] == letter:
                dashed[i] = letter
                correct.append(letter)

            else:
                tries += 1
                wrong.append(i)

    else:
        print(letter + ' has been entered please enter another')
    wordb = ''
    if gameOver(correct, wordarray) == 'start':
        word = r.choice(choices)
        wordarray = []
        dashed = []
        correct = []
        wrong = []
        buildWord()
        tries = 0
    elif gameOver(correct, wordarray) == 'stop':
        break
    print(correct)
    print(correct.count(letter))
