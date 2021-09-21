to_devide = input("to devide: ")
#converts to float
to_devide = float(to_devide)

def Get_number(to_devide):
    devider = 1
    
    while True:
        #devides the input number by the devider float
        result = to_devide / devider

        
        #converts the result to string so it can be processed
        result = str(result)
        
        #gets the number technicaly string that is after the dot
        what_is_after_the_dot = result.partition('.')[2]
        
        #converts it to float
        what_is_after_the_dot = float(what_is_after_the_dot)
        
        #prints the result if the number after the dot isn't more than 0
        if not what_is_after_the_dot > 0:
            print(devider, result)
        #else:
            #print('This was ejected', result, 'with devider of: ', devider)
        
        #stops the script if the devider is bigger than the actual number we want to devide
        #this is done so that we don't have infinite loop that is deviding 10 by 400 :D
        if devider > to_devide:
            break
        

        devider += 1
Get_number(to_devide)
