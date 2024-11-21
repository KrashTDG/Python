import sys, time
start_time = time.time()
lis_num = 1000000
try:
    # while lis_num <= 0:
    #     lis_num = int(input("how long you want the list to be "))
    #     if lis_num <= 0:
    #         print('write a positive number')
    
    
    lisst = list(range(1,lis_num))
    # for i in range(lis_num):
    #     num = int(input('write the value for the list '))
    #     lisst.append(num)
    
    num = 999999 #int(input("which number you wanna linearly search for "))
    found = False
    for i in range(lis_num):
        if num == lisst[i]:
            print("it is in the list at index " + str(i))
            found = True      
            break
        
    
    if found == False:
        print('it is not in the list')
    
except KeyboardInterrupt:
    sys.exit()
    
end_time = time.time()
elp_time = end_time - start_time
print(f'Elapsed time for Linear Search is {elp_time:.2f}')

    