'''
reading a file
'''

file = open("student.txt", "r+")
# print(file.writable())

# text = file.readlines()
# print(text)
text = file.read()
print(text)
# text = file.readlines()[1]
# print(text)
size = len(text)
print(size)

# for line in file:
#     print(line)

file.close()
