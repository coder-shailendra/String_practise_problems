def closest_person(x,y,z):
    d1 = abs(x-z)
    d2 = abs(y-z)
    if d1<d2:
        return 1
    elif d1>d2:
        return 2
    else:
        return 0
print(closest_person(2, 7, 4))  
print(closest_person(2, 5, 6))