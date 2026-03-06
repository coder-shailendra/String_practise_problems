def finalValueAfterOperations(operations):
    X = 0
    for op in operations:
        if "++" in op:
            X += 1
        else:
            X -= 1
    return X
operations = ["--X","X++","X++"]
print(finalValueAfterOperations(operations))