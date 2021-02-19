def add(a, b):
    sum = a + b
    return sum


result = add(20, 30)
print(result)


def large(a, b):
    if a > b:
        return a
    else:
        return b


result = large(20, 30)
print(result)

maximum = large
print(maximum(100, 30))
