#finds the smallest positive number evenly divisible by the numbers 1-20
#number has to be divisible by 20 so by only using those multiples runtime is faster
def getsmallest():
    for i in range(20, 100000000000, 20):
        for j in range(1, 22):
            if(j == 21):
                return i
            elif i % j != 0:
                break
        
    return -1

smallestNum = getsmallest()
print(smallestNum)


            
            
    
