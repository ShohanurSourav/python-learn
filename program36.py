def calculate(a, b):
    return a*a + 2*a*b + b*b


print(calculate(2, 3))


# lambda
# lambda parameter : expression

x = (lambda a, b: a*a + 2*a*b + b*b)(2, 3)
print(x)

print((lambda a, b: a*a + 2*a*b + b*b)(2, 3))
