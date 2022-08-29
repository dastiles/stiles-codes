#print('      *       ')
# finally nailed the fucken challange
# num = 5
# sub = 1
# for i in range(5):
#     stars = ' ' * num
#     star = '*' * sub

#    # print(stars + star)
#     sub += 1
#     num += 1

the_string = ''


def AndFunc(items):
    global the_string
    for i in range(len(items)):
        if items[i] != items[-1]:
            the_string += items[i] + ', '
        else:
            the_string += 'and ' + items[i] + '.'


AndFunc(['tofu', 'hard', 'pear'])
print(the_string)
