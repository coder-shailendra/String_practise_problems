def isSameAfterReversals(num):
    reversed1 = int(str(num)[::-1])
    reversed2 = int(str(reversed1)[::-1])
    return reversed2 == num
print(isSameAfterReversals(526))  
print(isSameAfterReversals(1800))
