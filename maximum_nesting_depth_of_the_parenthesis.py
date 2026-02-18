def max_depth(s):
    current_depth = 0
    max_depth = 0
    for ch in s:
        if ch == "(":
            current_depth += 1
            max_depth = max(max_depth,current_depth)
        elif ch == ")":
            current_depth -= 1
    return max_depth
print(max_depth("(1+(2*3)+((8)/4))+1"))
print(max_depth("(1)+((2))+(((3)))"))
print(max_depth("()(())((()()))"))