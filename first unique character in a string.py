def firstuniquecharacter(s):
    for i in range(len(s)):
        if s.count(s[i]) == 1:
            return i
    return -1
print(firstuniquecharacter("leetcode"))
print(firstuniquecharacter("loveleetcode"))  
print(firstuniquecharacter("aabb"))          
