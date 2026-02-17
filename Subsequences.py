def isSubsequences(s,t):
    i = 0
    j = 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
        j += 1
    return i == len(s)

s1 = "abc"
t1 = "ahbgdc"
s2 = "axc"
t2 = "ahbgdc"

print(isSubsequences(s1,t1))
print(isSubsequences(s2,t2))