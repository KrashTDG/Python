import time
start_time = time.time()
def findMidpoint(min, max):
    return (min + max) // 2
    

def binarySearch(arr, num):
    min = 0
    max = len(arr) - 1
    
    while min <= max:
        mid_index = findMidpoint(min, max)
        mid_value = arr[mid_index]
        
        if mid_value == num:
            print(f'{num} is present in the list at index {arr[mid_index]}')
            return
        
        elif num < mid_value:
            max = mid_index - 1
            
        else:
            min = mid_index + 1
            
    print(str(num) + ' is not in the list.')
        
arr = list(range(1,1000000))            
binarySearch(arr,999999)

end_time = time.time()
elp_time = end_time - start_time
print(f'Elapsed time for Binary Search is {elp_time:.2f}')