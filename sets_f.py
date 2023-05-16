numbers = {1, 2, 3, 4, 5, 6}
numbers.add(9)
numbers.remove(4)
print(numbers)

set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

# print all the sets with what they do in comments
print(set_a | set_b)  # all d unique elements 4rm both set_a & set_b are included in d result set, withou any duplicate.
print(set_a & set_b)  # it will only print the common set numbers in set_a and set_b 4, 5
print(set_a - set_b)  # it will only print element that is not common in the set_a 1, 2 and 3
print(set_a ^ set_b)  # this will remove the common numbers from the set 1, 2, 3, 6, 7 and 8

