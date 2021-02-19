# exception handling

try:
    lists = [20, 0, 30]
    result = lists[0] / lists[4]
    print(result)
    print("Done")
except ZeroDivisionError:
    print("Dividing by zero is not possible")
# except IndexError:
#     print("Index error!")
finally:
    print("Exception handling")

# print("Exception handling done")
