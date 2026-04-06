def maxproduct(n):
    digits = [int(d) for d in str(n)]
    digits.sort(reverse=True)  
    return digits[0] * digits[1]
print(maxproduct(31)) 
print(maxproduct(22))  