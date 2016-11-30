#takes all the even terms in a fibonacci sequence and adds them together

start = 1
end = 2

sumEven = 2
while end < 4000000:
    newSum = start + end
    if newSum % 2 == 0:
        sumEven += newSum
    
    start = end
    end = newSum

print(sumEven)
