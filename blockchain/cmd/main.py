# write a program which add numbers together on the command line


import sys
# for line in sys.stdin:
#     if line.rstrip() == 'q':
#         break
#     sys.stdout.write(f'input : {line}')

# print('exit')

n = len(sys.argv)

sum = 0
for i in range(1, n):
    try:
        num = int(sys.argv[i])
        sum += num
    except ValueError:
        print(sys.argv[i], ': is not number')

print(sum)
print(sys.path)
