def maxWords(sentences):
    max_count = 0
    for sentence in sentences:
        words = sentence.split()   
        count = len(words)      
        if count > max_count:
            max_count = count
    return max_count
sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]
print(maxWords(sentences))