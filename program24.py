n = int(input("Enter the last numnber : "))
sum = 0

for x in range(1, n+1, 1):
    sum = sum + x
print(sum)


for x in range(1, n+1, 1):
    sum = sum + x * x
print(sum)


# for multipy the num is 1
sum1 = 1
for x in range(1, n+1, 1):
    sum1 = sum1 * x
print(sum1)
