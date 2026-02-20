def sortSentence(s):
    words = s.split()
    result = [""] * len(words)
    for word in words:
        position = int(word[-1])  
        result[position - 1] = word[:-1]  
    return " ".join(result)
s = "is2 sentence4 This1 a3"
print(sortSentence(s))
s = "Myself2 Me1 I4 and3"
print(sortSentence(s))