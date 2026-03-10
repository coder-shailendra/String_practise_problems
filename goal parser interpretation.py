def interpret(command):
    result = ""
    i = 0
    while i < len(command):
        if command[i] == "G":
            result += "G"
            i += 1
        elif command[i:i+2] == "()":
            result += "o"
            i += 2
        else:  
            result += "al"
            i += 4
    return result
print(interpret("G()(al)"))
print(interpret("G()()()()(al)"))
print(interpret("(al)G(al)()()G"))