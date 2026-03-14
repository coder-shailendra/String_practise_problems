def countprefix(words,pref):
    count = 0
    for word in words:
        if word.startswith(pref):
            count += 1
    return count
words = ["pay","attention","practice","attend"]
pref = "at"
print(countprefix(words, pref))
words = ["leetcode","win","loops","success"]
pref = "code"
print(countprefix(words, pref))