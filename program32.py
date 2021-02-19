# stack --> LIFO

books = []
books.append("Learn C")
books.append("Learn C++")
books.append("Learn Python")
books.append("Learn PHP")
print(books)

books.pop()
print(books)
print("Now the top book is : ", books[-1])

books.pop()
print("Now the top book is : ", books[-1])

books.pop()
if not books:
    print("No books left")
else:
    print("Books available and it is : ", books[-1])

# Queue --> FIFO

from collections import deque

bank = deque(["Sourav", "Saikat", "Urmi"])
print(bank)
bank.popleft()
print(bank)
bank.popleft()
bank.popleft()

if not bank:
    print("No person left")

