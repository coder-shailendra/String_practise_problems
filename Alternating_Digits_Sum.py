def alternate_digits_sum(n):
    digits =str(n)
    total= 0
    sign = 1
    for d in digits:
        total +=sign * int(d)
        sign *= -1
    return total
print(alternate_digits_sum(521))
print(alternate_digits_sum(111))
print(alternate_digits_sum(886996))
