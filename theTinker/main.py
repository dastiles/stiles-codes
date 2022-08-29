import random

words = ['jason', 'self', 'opp', 'function']

word = random.choice(words)
wrongLetter = []
correctLetters = []
dashed_word = '_' * len(word)
lives = 3
dashed_arr = list(dashed_word)
print(word)

while True:
    if lives < 1:
        break

    print('Guess the word')
    print(dashed_arr)
    letter = input('Please Input your Letter here: ')
    if len(letter) != 1:
        print('Only 1 letter is Allowed. You Are disqualified')
        break

    check_word = []

    for i in word:
        check_word.append(i)

    if len(correctLetters) == len(check_word):
        print('You win')
        break

    if check_word.count(letter) and (correctLetters.count(letter) == False):
        for i in range(len(word)):
            if word[i] == letter:
                dashed_arr[i] = " " + letter + ' '
                correctLetters.append(letter)

    elif wrongLetter.count(letter) == False:
        lives -= 1
        print('Wrong Letter ....')
        print("Lives:  " + str(lives))
        wrongLetter.append(letter)

    else:
        print('please You Have Already clicked ' + letter)

    if len(correctLetters) == len(check_word):
        print('You win')
        print(word)
        break
