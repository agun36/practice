def square(x):
    return x**2


print(square(4))

result = (lambda y: y**2)(30)
print(result)
result2 = (lambda x: (lambda y:  y + x))(20)(20)
print(result2)
