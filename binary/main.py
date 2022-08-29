import random

numbers = [166, 336, 56, 21, 352, 476, 340, 23, 150, 361, 185, 266, 305, 316, 114, 499, 209, 126, 241, 48, 381, 74, 344, 424, 435, 370, 486, 444, 338, 262, 7, 423, 260, 75, 131, 186, 348, 426, 182, 257, 149, 185, 459, 256, 109, 116, 311, 262, 80,
           167, 427, 259, 157, 177, 131, 384, 149, 243, 179, 407, 331, 108, 99, 27, 326, 58, 124, 272, 239, 452, 101, 48, 368, 451, 320, 105, 124, 280, 462, 477, 411, 400, 216, 422, 7, 403, 224, 174, 56, 113, 265, 466, 164, 181, 93, 282, 41, 64, 460, 368]

numbers.sort()


def binary_search(number_list, number, left, right):
    if left > right:
        return -1
    mid = (left + right) // 2
    if number == number_list[mid]:
        return mid
    elif number < number_list[mid]:
        return binary_search(number_list, number, left, mid-1)
    else:
        return binary_search(number_list, number, mid+1, right)


print(binary_search(numbers, 0, 0, len(numbers)-1))
