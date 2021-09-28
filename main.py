#WRITE YOUR CODE IN THIS FILE
def close10(x, y):
    x = abs(x)
    y = abs(y)
    if x - 10 > y - 10:
        return y
    elif x - 10 < y - 10:
        return x
    else:
        return 0
print(close10(-20, -100))