try:
    a = 20
    b = 2
    print(a/b)
except ZeroDivisionError:
    print("There is a divide by zero error")
finally:
    print("This is going t execute no matter what")