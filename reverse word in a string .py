def reversed_words(s):
    words = s.split(" ") 
    reversed_words = []
    for word in words:
        reversed_words.append(word[::-1])
    return " ".join(reversed_words)
print(reversed_words("Let's take LeetCode contest"))
print(reversed_words("Mr Ding"))
print(reversed_words("Mr Shailendra"))