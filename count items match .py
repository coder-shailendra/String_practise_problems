class Solution:
    def countMatches(self, items, ruleKey, ruleValue):
        rules = {
            "type": 0,
            "color": 1,
            "name": 2
        }
        count = 0
        index = rules[ruleKey]
        for item in items:
            if item[index] == ruleValue:
                count += 1
        return count
items = [["phone","blue","pixel"],
         ["computer","silver","lenovo"],
         ["phone","gold","iphone"]]
ruleKey = "color"
ruleValue = "silver"
obj = Solution()
print(obj.countMatches(items, ruleKey, ruleValue))