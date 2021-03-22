#divisibility 
#sorry for bad english i'm from czech republic
#import time
import os



tdevide = input("to devide: ")
print(tdevide)
tdevide = float(tdevide) #converts string to float
print(tdevide)
tsize = len(str(tdevide).replace('.','')) #gets the size of number to devide
dby = 1 #divisor
tsize = tsize + 2
while 1 == 1:
    if dby < tdevide:
        #time.sleep(1) #delay, uncomment only with time
        out = tdevide / dby #deviding
        dby = dby + 1
        outs = len(str(out).replace('.','')) #counting the size of output
        if outs < tsize:
            print(dby - 1, out)
    else:
        quit()
