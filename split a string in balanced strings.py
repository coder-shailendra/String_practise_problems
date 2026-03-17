def balancedstringsplit(s):
    balance = 0
    count = 0
    for ch in s:
        if ch == 'R':
            balance += 1
        else:
            balance -= 1
        
        if balance == 0:
            count += 1  
    return count
s = "RLRRLLRLRL"
print(balancedstringsplit(s))
s = "RLRRLLRLRL"
print(balancedstringsplit(s))
s = "LLLLRRRR"
print(balancedstringsplit(s))