def minimizedStringLength(s):
    return len(set(s))
print(minimizedStringLength("aaabc"))   
print(minimizedStringLength("cbbd"))     
print(minimizedStringLength("baadccab"))