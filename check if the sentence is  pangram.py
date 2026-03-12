def checkpangram(sentences):
    return len(set(sentences)) == 26
sentence = "thequickbrownfoxjumpsoverthelazydog"
print(checkpangram(sentence))
sentence = "leetcode"
print(checkpangram(sentence))