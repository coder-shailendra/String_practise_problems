def final_string(s):
    result = ""
    for ch in s:
        if ch == 'i':
            result = result[::-1]
        else:
            result += ch   
    return result
print(final_string("string"))  
print(final_string("poiinter")) 