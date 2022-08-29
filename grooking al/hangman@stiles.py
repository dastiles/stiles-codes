import random
#  made by stiles

questions = [
    'Famous search engine used in chrome',
    'Programing language used in data science',
    'what operating does samsung smartphones use',
    'What software do you use to connect to internet',
    'A portable computer',
    'name of this game',
    'which operating system uses .apk extension',
    'name store for android applications',
    'a big online commerce website',
    'Builds electric cars',
    'Builds rockets to mars',
    'richest man on earth',
]

words = [
    'google',
    'python',
    'android',
    'browser',
    'laptop',
    'hangman',
    'android',
    'playstore',
    'amazon',
    'tesla',
    'spacex',
    'elonmusk'        
]

dashed_words = []
correct_words = []
wrong_words = []
word = ''
question = ''

def chooseQandA():
    global word, question, dashed_words
    index = random.randint(0,len(words))
    word = words[index]
    question = questions[index]
    for i in word:
        dashed_words.append(' - ')


 
chooseQandA()   

tries = 0
while True and tries < 4:
    print(question)
    print()
    for i in dashed_words:
        print(i ,end=' ')
    print()
    letter = input('enter a letter:  ').lower()
    print('\n')
    if len(letter) <= 1:
        if word.count(letter) and correct_words.count(letter) <= 0:           
            for i in range(len(word)):
                if word[i].lower() == letter:
                    dashed_words[i] = letter
                    correct_words.append(letter)
            
        else:
            print('\n')
            print('Wrong letter or you have already entered it')
            tries += 1
            
        if len(correct_words) == len(dashed_words):
            print('\n')
            print(f'You Win!!! congradulations your word is {word}')
            print('Type exit to exit game')
            correct_words = []
            dashed_words = []
            chooseQandA()
            
         
    if letter.lower() == 'exit':
        break   
        
   
   
# hangman game by charles madhuku
# todo: add graphics to be more intresting

