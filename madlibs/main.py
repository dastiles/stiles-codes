import random

f = open('madlib.txt', 'r')
madlibtext = f.readlines()

prev = ''
while len(madlibtext) > 0:
    madlib = random.choice(madlibtext)
    madlibtext.remove(madlib)
    print(madlib)
    noun = input('enter a noun: ')
    madlib = madlib.replace('blank', noun)
    print(madlib)
    prev += madlib
    # new = madlib + prev

    print(prev)
