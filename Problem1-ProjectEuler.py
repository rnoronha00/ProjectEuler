#finds all the multiples of 3 and 5 below 1000 and adds them together

value = 1000
threeFiveSum = 0

for i in range(2, value):
    if (i % 3 == 0) or (i % 5 == 0):
        threeFiveSum += i

print(threeFiveSum)
