# def function():
    # counter = 0
    # while counter < 10:
        # yield counter
        # counter += 1


# for x in function():
    # print(x)

def even_numbers(x):
    for i in range(x):
        if i % 2 == 0:
            yield i


print(list(even_numbers(21)))

def odd_numbers(x):
    for i in range(x):
        if i % 2 != 0:
            yield i


print(list(odd_numbers(21)))