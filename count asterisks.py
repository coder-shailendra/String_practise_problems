def countAsterisks(s):
    count = 0
    inside = False
    for ch in s:
        if ch == '|':
            inside = not inside  
        elif ch == '*' and not inside:
            count += 1

    return count
s = "l|*e*et|c**o|*de|"
print(countAsterisks(s))