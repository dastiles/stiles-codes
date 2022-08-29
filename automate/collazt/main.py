def Collazt(num):
    if num != 1:
        Collazt(int(n))

    if num % 2 == 0:
        print(num // 2)
        return num // 2
    elif num % 2 == 1:
        res = 3 * num + 1
        print(res)
        return res


n = int(input('enter a number: '))
Collazt(n)
# while n != 1:
#     n = Collazt(int(n))
