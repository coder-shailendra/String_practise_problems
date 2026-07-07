class solution:
    def replacealldigits(self,s:str):
        answer = ""
        for i in range(len(s)):
            if i%2 ==0:
                answer += s[i]
            else:
                answer += chr(ord(s[i-1]) + int(s[i]))
        return answer
obj =solution()
print(obj.replacealldigits("a1c1e1"))
print(obj.replacealldigits("a1b2c3d4e"))