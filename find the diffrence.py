def findTheDifference(s, t):
    for ch in t:
        if t.count(ch) != s.count(ch):
            return ch
s = "abcd"
t = "abcde"
print(findTheDifference(s, t))