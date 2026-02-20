def find_missing(lst, n):
    total = n * (n + 1) // 2
    return total - sum(lst)
print(find_missing([1,2,4,5], 5))
print(find_missing([1,2,3,4,5,6,7,9],9))
