class Solution:
    def countSeniors(self, details):
        count = 0
        for person in details:
            age = int(person[11:13])  
            if age > 60:
                count += 1
        return count
obj = Solution()
print(obj.countSeniors(["7868190130M7522","5303914400F9211","9273338290F4010"]))                       
print(obj.countSeniors(["1313579440F2036","2921522980M5644"]))
                        