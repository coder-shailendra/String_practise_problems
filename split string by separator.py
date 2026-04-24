def splitstringseparator(words,separator):
    result = []
    for word in words:
        parts = word.split(separator)
        for p in parts:
            if p != "":
                result.append(p)
    return result
words = ["one.two.three", "four.five", "six"]
separator = "."
print(splitstringseparator(words, separator))