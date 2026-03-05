def maximumOddBinaryNumber(s):
    ones = s.count('1')
    zeros = s.count('0')
    result = '1' * (ones - 1) + '0' * zeros + '1'
    return result
s = "010"
print(maximumOddBinaryNumber(s))
s = "0101"
print(maximumOddBinaryNumber(s))