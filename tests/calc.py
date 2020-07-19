def add(x,y):
    return x+y


def sub(x,y):
    return x - y

def mult(x,y):
    return x * y   

def devide(x,y):
    if y == 0:
        raise ValueError('cannot devide by zero')
    return x / y 