def maximumOddBinaryNumber(s):
    ones = s.count('1')
    zeros = s.count('0')
    return '1' * (ones - 1) + '0' * zeros + '1'
print(maximumOddBinaryNumber("010")) 
print(maximumOddBinaryNumber("0101"))  