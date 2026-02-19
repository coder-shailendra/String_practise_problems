def arraystringareequal(word1,word2):
    str1 = ""
    str2 = ""
    for word in word1:
        str1 += word
    for word in word2:
        str2 += word
    if str1 == str2:
        return True
    else:
        return False
word1 = ["ab", "c"]
word2 = ["a", "bc"]
print(arraystringareequal(word1,word2))
word1 = ["a", "cb"]
word2 = ["ab", "c"]
print(arraystringareequal(word1,word2))