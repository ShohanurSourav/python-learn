'''
# map

def square(x):
    return x*x
num = [1, 2, 3, 4, 5]

result = list(map(square, num))
print(result)
'''

# list comprehension for map

# num = [1, 2, 3, 4, 5]
# result = [x * x for x in num]
# print(result)


# filter function

num1 = [1, 2, 3, 4, 5]
result1 = list(filter(lambda x: x % 2 == 0, num1))
print(result1)

# list comprehension for filter

# num1 = [1, 2, 3, 4, 5]
# result1 = [y for y in num1 if y % 2 == 0]
# print(result1)

#list comprehension

# fruits = ["apple", "mango", "guava", "lemon", "cherry"]
# newlist = [x for x in fruits if "a" in x]
# print(newlist)
