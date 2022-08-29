# simple coding projects
# a simple program to ask your name
#  charles madhuku


print('please enter your name in the command that follows')
while True:
    name = input('what is your name: ')
    if name == '':
        print('please enter a valid name')
    else:
        print(name + ' thank you')
        break
