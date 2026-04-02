def firstpalindrome(words):
    for word in words:
        if word == word[::-1]:
            return word
    return ""
print(firstpalindrome(["abc","car","ada","racecar","cool"]))