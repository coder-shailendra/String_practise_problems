def reversestring(s):
    words = s.split()
    words.reverse()
    return " ".join(words)
print(reversestring("python is a easy language"))
print(reversestring("hello world"))