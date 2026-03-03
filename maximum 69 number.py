def maximum69number(num):
    num = list(str(num))   
    for i in range(len(num)):
        if num[i] == '6':  
            num[i] = '9'   
            break          
    return int("".join(num)) 
num = 9969 
print(maximum69number(num))