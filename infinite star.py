import time,sys
end = False
i = 0
star = '*****'
print(star)
try:
    while end == False: 
        if i == 5:
            while (i > 0):
                i = i - 1
                print(' ' * i + star)
                time.sleep(0.075)
                
                
        while (i < 5):
            i = i + 1
            print(' ' * i + star)
            time.sleep(0.075)
            continue
        
except KeyboardInterrupt:
    sys.exit()