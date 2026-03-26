def reversestringprefix(s, k):
    return s[:k][::-1] + s[k:]
print(reversestringprefix("abcd", 2))  
print (reversestringprefix("xyz", 3))  