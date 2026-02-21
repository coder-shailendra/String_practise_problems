def detectcapital(word):
    if word.isupper():
        return True
    elif word.islower():
        return True
    elif word.istitle():
        return True
    else:
        return False
word = "USA"
print(detectcapital(word))
word = "leetcode"
print(detectcapital(word))
word = "FlaG"
print(detectcapital(word))