# recursion is  a function that call itself
# 3
# 3*2*1
# factorial 5:
# 5*4*3*2*1
# explain factorial
# rec invocation  is a function that  call itself


def factorial(x):
    if x == 1:
        return 1
    else:
        return x * (factorial(x-1))


results = factorial(5)
print(results)
