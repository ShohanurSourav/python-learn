# multiple exception handling

# try:
#     num1 = int(input("Enter your first number : "))
#     num2 = int(input("Enter your second number : "))
#     result = num1 / num2
#     print(result)
#
# except(ValueError, ZeroDivisionError):
#     print("You have entered incorrect input")
#
# finally:
#     print("Done!")


def voter(age):
    if age < 18:
        raise ValueError("Invalid Voter!")
    return "You are allowed to vote"


try:
    print(voter(18))
except ValueError as e:
    print(e)
