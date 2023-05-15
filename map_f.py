

def add(x):
    return x+2


num_list = [10, 20, 30, 40, 50]
result = list(map(lambda x: x*2, num_list))
print(result)