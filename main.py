#WRITE YOUR CODE IN THIS FILE
#define function
#add parameters
def close10(x, y):
#if then else
    if abs(x - 10) > abs(y - 10):
        return y
    elif abs(x - 10) < abs(y - 10):
        return x
    else:
        return 0
#run function
print(close10(13, -13))