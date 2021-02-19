n = input("Enter a text of numbers : ")
list = n.split()
sum = 0

for num in list:
    sum = sum + int(num)
print(sum)


numOfLetters = 0
numOfDigits = 0
numOfWords = 0

text = input("Enter something: ")

for x in text:
    x = x.lower()
    if 'a' <= x <= 'z':
        numOfLetters = numOfLetters + 1
    elif x >= '0' <= '9':
        numOfDigits = numOfDigits + 1
    elif x == ' ':
        numOfWords = numOfWords + 1
print("Number os letters", numOfLetters)
print("Number os digits", numOfDigits)
print("Number os words", numOfWords + 1)
