num1 = {1, 2, 3, 4, 5, 5}
num2 = set([4, 5, 6])
print(num1)
print(num2)
num2.add(7)
print(num2)
num2.remove(7)
print(num2)
print(7 in num2)

print(num1 | num2) # al value
print(num1 & num2) # only the common value
print(num1 - num2) # remove the common value from set1 by set2
