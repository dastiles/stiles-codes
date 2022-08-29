def binarySearch(arr,item):
    start = 0
    end = len(arr) -1
    
    while start <= end:
        mid = (start + end) // 2
        guess = arr[mid]
        if guess == item:
            return guess
        elif guess > item:
            end = mid - 1
        else:
            start = mid + 1
    return None
            
  
  
print(binarySearch([1,2,34,50,100,345,980,1000,1011], 6) )    

num = '009'

numc = int(num) 
print(numc)