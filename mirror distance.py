def mirrordistance(n):
    reverse = int(str(n)[::-1])
    return abs(n-reverse)
print(mirrordistance(25))  
print(mirrordistance(10))  
print(mirrordistance(7))   