#finds the largest palindrome from the product of two three digit numbers
#two digit numbers: 9009 = 91*99

#checks to see if a number is a palindrome
def checkPalindrome(num):
    start = 0
    end = len(num) - 1

    while start < end:
        if num[start] != num[end]:
            return False
        start += 1
        end -= 1

    return True

largestPalindrome = 0
for numOne in range(100, 1000):
    for numTwo in range(100, 1000):
        #replaces the largest palindrome if the new product is a palindrome and a larger value
        if (checkPalindrome(str(numOne * numTwo)) == True) and (largestPalindrome < (numOne * numTwo)):
            largestPalindrome = numOne * numTwo
       
print(largestPalindrome)



