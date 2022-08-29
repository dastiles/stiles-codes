# stiles
import random
from binary_search import  binarySearch
zimNumbers = []

def createPhoneNumber(arr):
    phoneNumber = []
    
    while len(phoneNumber) < 10:
        phoneNumber.append(str(random.choice(arr)))
    phoneNumber[0] = '0'
    phoneNumber[1] = '7'
    phoneNumber[2] = str(random.choice([7,8,1]))
    return ''.join(phoneNumber)

print('Generate Zimbabwean Numbers')

for i in range(100000000):
    zimNumbers.append(int(createPhoneNumber([1,2,3,4,5,6,7,8,9,0])))
 
 
sorted = zimNumbers.sort()  

print(binarySearch(zimNumbers,771315239))
    


