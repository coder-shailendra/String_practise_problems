class Solution:
    def intToRoman(self, num: int):
        values = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
        symbols = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]               
        answer = ""
        for i in range(len(values)):
            while num >= values[i]:
                answer += symbols[i]
                num -= values[i]
        return answer
obj = Solution()
print(obj.intToRoman(3456))
print(obj.intToRoman(45))
print(obj.intToRoman(264))