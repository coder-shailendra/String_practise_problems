def rotatestring(s,goal):
    if len(s) != len(goal):
        return False
    return goal in (s+s)
print(rotatestring("abcde", "cdeab"))  
print(rotatestring("abcde", "abced"))  