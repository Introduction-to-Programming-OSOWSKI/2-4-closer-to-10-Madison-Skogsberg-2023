#WRITE YOUR CODE IN THIS FILE
def close10(x, y):
    if abs(x - 10) > abs(y - 10):
        return y
    elif abs(x - 10) < abs(y - 10):
        return x
    else:
        return 0
print(close10(5, -13))