#recursively determines the largest prime factor given a number

def checkPrime(num):

    for i in range(2, num):
        if num % i == 0:
            return False

    return True

def findLowest(num):

    for i in range(2, num):
        if num % i == 0:
            return i
    return 5

def primefactor(num):

    if num <= 0:
        return
    
    elif checkPrime(num) == True:
        if num > largestPrime[0]:
            largestPrime[0] = num

    else:
        low = findLowest(num)
        primefactor(low)
        primefactor(int(num / low))

num = int(input("Enter a number: "))
#largest prime number stored as an array
#this way can be referenced outside the scope of the function
largestPrime = [0]
primefactor(num)
print(largestPrime[0])
