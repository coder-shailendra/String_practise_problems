class Solution:
    def arrayStringsAreEqual(self, word1, word2):
        s1 = "".join(word1)
        s2 = "".join(word2)
        return s1 == s2
word1 = ["ab", "c"]
word2 = ["a", "bc"]
obj = Solution()
result = obj.arrayStringsAreEqual(word1, word2)
print(result)