def subtract_product_sum(n):
    product = 1
    total_sum = 0
    for digit in str(n):
        d = int(digit)
        product *= d
        total_sum += d
    return product - total_sum
print(subtract_product_sum(234)) 
print(subtract_product_sum(4421))  