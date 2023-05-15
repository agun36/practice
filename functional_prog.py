# writing code in function
# data process 1st and next function
#  passing one function to other function

def add_tem(x):
    return x+10


def twice(func, arg):
    return func(func(arg))


print(twice(add_tem, 10))
